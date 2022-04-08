import warnings
import pandas as pd
warnings.simplefilter(action='ignore', category=FutureWarning)
from data.allteams import teamnames
from web.utils.configCols import columns
import os
import glob

def combineCsvs(path):
    header = "Name,Team Number,Match Number,Did The Team Taxi?,Autonomous High Scored,Autonomous High Missed,Autonomous Low Scored,Autonomous Low Missed,TeleOp High Scored,TeleOp High Missed,TeleOp Low Scored,TeleOp Low Missed,Climb Level,Alliance Partner,Driving Effectiveness,Defense Effectiveness,Additional Notes\n"
    orig = os.getcwd()
    os.chdir(path)
    all_filenames = [i for i in glob.glob('*.{}'.format("csv"))]
    for exclude in (('test.csv', 'final.csv', 'raw.csv')):
        try:
            all_filenames.remove(exclude)
        except:
            pass
		
    alllines = []
    for filen in all_filenames:
        with open(filen, 'r') as temp:
            alllines.append(temp.readlines())
    if alllines[0] != header:
        if header not in alllines:
            alllines = [[header]] + alllines
        else:
            alllines.remove(header)
            alllines = [[header]] + alllines
    flattened = [data for log in alllines for data in log] 
    # print(len(flattened))
    os.remove('final.csv')
    with open('final.csv', 'a') as final:
        for line in flattened:
            final.write(line)
    os.chdir(orig)
    return flattened

def load_data(path="data/fina.csv"):
    print(os.getcwd())
    alldata = pd.read_csv(path,index_col=False)
    
    return alldata

def fix_cols(data):
    alldata = data.rename(columns=columns)
    alldata = alldata.sort_values(["matchNum", "teamNum"], ascending=[True, True])
    alldata = alldata.drop("person", 1).drop("notes", 1).drop("with1086", 1)
    return alldata

    
def new_cols(data):
    def taxiYesNo(word):
        if word.taxiWord == "Yes":
            return 1
        else:
            return 0
    data["taxi"] = data.apply((lambda row: taxiYesNo(row)), axis=1)
    data["taxi"] = data.apply((lambda row: taxiYesNo(row)), axis=1)
    data["autoAcc"] = ((data["autoHighIn"] + data["autoLowIn"]) / (data["autoHighIn"] + data["autoHighOut"] + data["autoLowIn"] + data["autoLowOut"]))
    data["teleAcc"] = ((data["teleHighIn"] + data["teleLowIn"]) / (data["teleHighIn"] + data["teleHighOut"] + data["teleLowIn"] + data["teleLowOut"]))
    data["autoPoints"] = (data["autoHighIn"]*4 + data["autoLowIn"]*2)
    data["telePoints"] = (data["teleHighIn"]*2 + data["teleLowIn"])
    data["teamNum2"] = data["teamNum"]
    data["teamName"] = data.apply(lambda row: teamnames[int(row.teamNum)], axis=1)
    data["highPoints"] = (data["autoHighIn"] + data["teleHighIn"])
    data["lowPoints"] = (data["autoLowIn"] + data["teleLowIn"])
   
    def levelHandler(row):
        try:
            return round(row.highPoints/(row.highPoints+row.lowPoints))
        except ZeroDivisionError:
            return 0
    data["level"] = data.apply((lambda row: levelHandler(row)), axis=1)
    data["climb"] = data.apply(lambda row: [int(s) for s in list(row.climbWord) if s.isdigit()][0], axis=1)
    return data

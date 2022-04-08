import warnings
import pandas as pd
warnings.simplefilter(action='ignore', category=FutureWarning)
from data.allteams import teamnames
from web.utils.configCols import columns

def load_data(path="data/raw.csv"):
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

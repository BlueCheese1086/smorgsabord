import warnings
import pandas as pd
warnings.simplefilter(action='ignore', category=FutureWarning)
from data.allteams import teamnames
from configCols import columns

def load_data(path="data/raw.csv"):
    alldata = pd.read_csv(path)
    alldata = alldata.sort_values(["matchNum", "teamNum"], ascending=[True, True])
    alldata = alldata.drop("name", 1).drop("notes", 1)
    
    return alldata

def fix_cols(data):
    data = data.rename(columns=columns)
    return data

    
def new_cols(data):
    data["autoAcc"] = ((data["autoHighIn"] + data["autoLowIn"]) / (data["autoHighIn"] + data["autoHighOut"] + data["autoLowIn"] + data["autoLowOut"]))
    data["teleAcc"] = ((data["teleHighIn"] + data["teleLowIn"]) / (data["teleHighIn"] + data["teleHighOut"] + data["teleLowIn"] + data["teleLowOut"]))
    data["autoPoints"] = (data["autoHighIn"]*4 + data["autoLowIn"]*2)
    data["telePoints"] = (data["teleHighIn"]*2 + data["teleLowIn"])
    data["teamNum2"] = data["teamNum"]
    data["teamName"] = data.apply(lambda row: teamnames[int(row.teamNum)], axis=1)
    data["highPoints"] = (data["autoHighIn"] + data["teleHighIn"])
    data["lowPoints"] = (data["autoLowIn"] + data["teleLowIn"])
    data["level"] = data.apply(lambda row: round(row.highPoints/(row.highPoints+row.lowPoints)), axis=1)
    return data

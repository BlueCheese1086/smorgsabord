"""Configure column names. The webapp works with the columns:
name,teamNum,matchNum,taxi,autoHighIn,autoHighOut,autoLowIn,autoLowOut,teleHighIn,teleHighOut,teleLowIn,teleLowOut,climb,with1086,drive,defense,notes

Enter the column names EXACTLY as they appear in the csv. For example, if the name column is titled 'scouter', make the appropriate line (line 16) say 'scouter': 'name'. This is case sensitive.
"""
columns = {'Additional Notes': 'notes',
 'Alliance Partner': 'with1086',
 'Autonomous High Missed': 'autoHighOut',
 'Autonomous High Scored': 'autoHighIn',
 'Autonomous Low Missed': 'autoLowOut',
 'Autonomous Low Scored': 'autoLowIn',
 'Climb Level': 'climbWord',
 'Defense Effectiveness': 'defense',
 'Did The Team Taxi?': 'taxiWord',
 'Driving Effectiveness': 'drive',
 'Match Number': 'matchNum',
 'Name': 'person',
 'Team Number': 'teamNum',
 'TeleOp High Missed': 'teleHighOut',
 'TeleOp High Scored': 'teleHighIn',
 'TeleOp Low Missed': 'teleLowOut',
 'TeleOp Low Scored': 'teleLowIn'}

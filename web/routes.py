import pandas as pd
import numpy as np
from flask import render_template, request
from web import app
from web.utils import plotly_plot, newutils
from data.allteams import teamnames

data = newutils.load_data("data/raw.csv")
data = newutils.new_cols(data)
allteams = {}
for num in list(data["teamNum"]):
    allteams[int(num)] = teamnames[num]

@app.route("/")
def main_page():
    auto_average = round(data["autoPoints"].mean(), 2)
    teleop_average = round(data["telePoints"].mean(), 2)
    climb_average = round(data["climb"].mean(), 2)
    auto_accuracy = str(round(data["autoAcc"].mean(), 2)*100) + "%"
    teleop_accuracy = str(round(data["teleAcc"].mean(), 2)*100) + "%"
    matches = data["matchNum"].max()
    teleop_avg_bars = plotly_plot.allperf(data)
    context = {"auto_average": auto_average,
               "teleop_average": teleop_average, "climb_average": climb_average,
            'auto_accuracy': auto_accuracy,
            'teleop_accuracy': teleop_accuracy,'matches': matches, 'teleop_avg': teleop_avg_bars, "team_list": list(allteams.values())}
    return render_template('plotly.html', context=context)


@app.route("/team", methods=['POST'])
def plot_team():
    team = request.form['team_name']
    team = team.split(" ")[0]
    teamSt = allteams[int(team)]
    byteam = lambda x: data[data.teamNum == x]
    teamdata = byteam(int(team))
    if teamdata["highPoints"].sum() > teamdata["lowPoints"].sum():
        level = "High shooter"
    elif teamdata["highPoints"].sum() < teamdata["lowPoints"].sum():
        level = "Low shooter"
    else:
        level = "Shoots high and low"
    
    auto_avg = round(teamdata["autoPoints"].mean(), 2)
    teleop_avg = round(teamdata["telePoints"].mean(), 2)
    climb_avg = round(teamdata["climb"].mean(), 2)
    auto_acc = str(round(teamdata["autoAcc"].mean(), 2)) + "%"
    tele_acc = str(round(teamdata["teleAcc"].mean(), 2)) + "%"
    defense = round(teamdata["defense"].mean(), 2)
    teamgraph = plotly_plot.teamplot(teamdata)
    
    context = {"teamSt": teamSt, "level": level, "auto_avg": auto_avg, "teleop_avg": teleop_avg, "climb_avg": climb_avg, "auto_acc": auto_acc, "tele_acc": tele_acc, "defense": defense, "teamgraph": teamgraph, "team_list": list(allteams.values())}
    
    return render_template('team.html', context=context)

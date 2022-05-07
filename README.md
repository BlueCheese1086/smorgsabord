# smorgasbord
A simple 2022 FRC data visualization app for use with CSVs from our scouting app, built in Flask using the AdminLTE template and Plotly. Made to be usable online as well as offline due to restrictions at the competition venue. Currently hosted at http://dcmp1086.herokuapp.com/

## Installation
### On Mac (tested)
- Download the repository (using git clone or just click on the green code button and Download as zip)
- Unzip the zip file
- Open the Terminal and navigate to the new directory using cd
- Enter `python3 -m venv smorgasbord`
- Enter `source smorgasbord/bin/activate`
- Enter `pip3 install -r requirements.txt` This may take a while.
- This may cause a window to pop up asking if you want to install Developer Tools. Click Accept
- Wait for the packages to install
### On Linux (tested)
- Download the repo
- Navigate inside the folder in the terminal
- Type `pip install -r requirements.txt`
### On Windows (tested)
DOES WORK on HCPS computers, use PowerShell
- Download the repository (using git clone or just click on the green code button and Download as zip)
- Unzip the zip file
- Open the Terminal and navigate to the new directory using cd
- If python is not installed, https://www.python.org/downloads/
- Enter `pip install -r requirements.txt` This may take a while.

## Usage
- Configure the column names in web/config_cols.py
- Edit the datapath variable in routes.py to where the csv with the data is stored
- Enter `flask run` or `python run.py` if flask is not found
- Open the provided web address (http://127.0.0.1:5000) in a web browser
- May need to zoom out or in

## Future ideas
- Clean up code
- Make more easily configurable
- Package on pip?
- Make graphs editable by date data was collected (day 1 only, day 2-3, etc) using slider
- Add match projections and ranking projections tab based on rankings.py, allow match wins and losses to be toggled to see how end rankings are affected
- Take inspiration from Orbit 1690 - https://github.com/Team1690/Scouting-Frontend, https://orbit-scouting-app-viewer.web.app/#/

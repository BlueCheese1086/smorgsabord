# smorgsabord
A simple FRC scouting app for use with CSVs, built in Flask using the AdminLTE HTML/JS/CSS template

## Installation
### On Mac
- Download the repository (using git clone or just click on the green code button and Download as zip)
- Unzip the zip file
- Open the Terminal and navigate to the new directory using cd
- Enter `python3 -m venv smorgsabord`
- Enter `source smorgsabord/bin/activate`
- Enter `pip3 install -r requirements.txt` This may take a while.
- This may cause a window to pop up asking if you want to install Developer Tools. Click Accept
- Wait for the packages to install
### On Linux
- Download the repo
- Navigate inside the folder in the terminal
- Type `pip install -r requirements.txt`

## Usage
- Go to the data/ directory and put in your csv file with all the data. Name it raw.csv
- Exit the data/ directory to the main directory
- Enter `flask run`
- Open the provided web address (http://127.0.0.1:5000) in a web browser
- May need to zoom out or in

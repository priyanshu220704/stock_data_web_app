# stock_data_web_app

Download the dump.csv file from "https://github.com/shaktids/stock_app_test/blob/main/dump.csv".

For Setup

# if venv is not present 

python -m venv venv

# if execution of script is disabled 

Set-ExecutionPolicy Unrestricted -Scope Process

# For activating venv

.\venv\Scripts\Activate

# Ensure that the venv is activated 

pip install flask pandas

# For running the code 

python app.py

it should be running in the local server http://127.0.0.1:5000/

# the structure of the folder is 

stock_project/               # Root folder

│── venv/                    # Virtual environment

│── dump.csv                 # The CSV file with stock data

│── app.py                   # The Flask backend

│── requirements.txt         # (Optional) Dependencies list

│── templates/               # Folder for frontend HTML files

│   ├── index.html           # The main webpage

│── static/                  # (Optional) For CSS/JS files if needed

│── README.md                # Instructions for setup (for GitHub)

# Features

I have made a scroll bar on the left for selecting a stock
and on clicking on the show data button it shows the chart on the right.
I have made a crosshair cursor which on moving on the chart give the exact date and price on the stock at the point.


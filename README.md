This program converts a JSON response generated from Alpaca trade executions to a CSV format suitable for importing into [Portfolio Performance](https://www.portfolio-performance.info/en/).

## Installation instructions

1. Install the [Python 3.10](https://www.python.org/downloads/) interpreter.
2. Navigate to the program folder in the terminal.
3. Create a virtual environment in the program folder using the command `python3 -m venv env`.
4. Activate the virtual environment using the command `source env/bin/activate` if on Linux/MacOS or `env\Scripts\activate.bat` if on Windows.
5. Install the required packages using the command `pip install -r requirements.txt`.
6. Place the json file(s) to be converted in the program folder.
7. Run the program using the command `python converter.py`. The program will convert all the json files in the program folder and output a single .csv file.

## Usage instructions

- Make sure your Portfolio Perfomance locale is set to English and US number format
- Import the generated csv file into Portfolio Performance via `File > Import > CSV Files...`
- During the import process, make sure to select `Type of data: Portfolio Transactions`

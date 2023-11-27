import pandas as pd
import json
import os

full_df = pd.DataFrame()
file_counter = 0
latest_file = ""

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".json"):
        file_counter += 1
        latest_file = filename
        with open(filename, "r") as f:
            data = json.load(f)
        f.close()
        df = pd.DataFrame(data["trade_activities"])
        df = df[df["status"] == "executed"]
        df = df.rename(
            columns={
                "symbol": "Ticker symbol",
                "qty": "Shares",
                "gross_amount": "Value",
                "trade_date": "Date",
            },
        )
        df = df.sort_values(by=["trade_time"], ascending=False)
        df = df[
            [
                "Ticker symbol",
                "Shares",
                "Value",
                "Date",
            ]
        ]
        df["Transaction Currency"] = "USD"
        # the following two lines are needed to make the data compatible with the portfolio performance software way of dealing with buy and sell transactions
        df["Shares"] = df["Shares"].astype(float) * -1
        df["Value"] = df["Value"].astype(float) * -1
        full_df = pd.concat([full_df, df])

csv_name = "output.csv" if file_counter > 1 else latest_file[:-5] + ".csv"
full_df.to_csv(csv_name, index=False)

import pandas as pd

files = [
    ("account_groupings.csv", "account-groupings"),
    ("closed_opportunities_FY24_FY25.csv", "closed-opps"),
    ("open_opportunities_FY26.csv", "open-opps"),
    ("next_steps_history_closed.csv", "next-steps-closed"),
    ("next_steps_history_open.csv", "next-steps-open"),
]

for csv_name, json_name in files:
    df = pd.read_csv(csv_name)
    # you can use head(200) if the file is huge and you only need a sample:
    # df = df.head(200)
    df.to_json(f"{json_name}.json", orient="records")
    print(f"Wrote {json_name}.json")

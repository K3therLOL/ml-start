import pandas as pd


field = pd.read_csv("./data.csv")
lhx, lhy = map(int, input().split())
rlx, rly = map(int, input().split())

print(
    field.loc[
        (field["x"] >= lhx) & (field["x"] <= rlx) &
        (field["y"] <= lhy) & (field["y"] >= rly)
    ]
)

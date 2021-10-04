import os

from os import path
import pandas as pd
DATA_DIR = '/Users/david/OneDrive/Documents/Python Projects/data/'

pnl = pd.read_csv(path.join(DATA_DIR, "leg-pnl.csv"))
print(pnl.shape)

pnl_eq = pnl.loc[pnl["Pool"] == "EQ", ["LegID", "Current VaR(t)", "Pool"]]
print(pnl_eq.head())

pnl_eq["id_and_pool"] = (pnl['LegID'] + "-" + pnl["Pool"])

pnl_eq.to_csv(path.join(DATA_DIR, "leg-pnl.v1.csv"))


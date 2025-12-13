import pandas as pd
import numpy as np

df = pd.read_csv("missing_values.csv")

# print(df.head(5))
# print(df.notna().sum())
# print(df.fillna("No Value"))
# print(df.notna().sum(axis='index'))
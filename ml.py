import pandas as pd
import numpy as np



df = pd.read_csv('hotel_booking_data.txt')
# print(df.head())
print(df.to_string())
# print(df.shape)
# print(df.info())
# print(pd.options.display.max_columns)
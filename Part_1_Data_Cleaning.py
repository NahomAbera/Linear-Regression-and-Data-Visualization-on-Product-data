import pandas as pd

df = pd.read_csv('product_data.csv')
df.fillna(0, inplace=True)
df.dropna(inplace=True)
if len(df) < 300:
    print("Error: Not enough data points after cleaning")
else:
    print("Data cleaning complete")
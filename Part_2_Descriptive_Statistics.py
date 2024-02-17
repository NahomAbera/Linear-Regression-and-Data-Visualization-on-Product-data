import pandas as pd

df = pd.read_csv('product_data.csv')
product_amount_mean = df['Product Amount in Stock'].mean()
product_amount_median = df['Product Amount in Stock'].median()
product_amount_var = df['Product Amount in Stock'].var()
product_amount_std = df['Product Amount in Stock'].std()

price_mean = df['Price of Product'].mean()
price_median = df['Price of Product'].median()
price_var = df['Price of Product'].var()
price_std = df['Price of Product'].std()


print("Product Amount in Stock:")
print(f"Mean: {product_amount_mean}")
print(f"Median: {product_amount_median}")
print(f"Variance: {product_amount_var}")
print(f"Standard deviation: {product_amount_std}")
print("\nPrice of Product:")
print(f"Mean: {price_mean}")
print(f"Median: {price_median}")
print(f"Variance: {price_var}")
print(f"Standard deviation: {price_std}")
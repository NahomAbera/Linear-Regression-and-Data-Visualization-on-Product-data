import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('product_data.csv')

plt.bar(df.index, df['Product Amount in Stock'], color='green')
plt.xlabel('Product index')
plt.ylabel('Amount in Stock')
plt.title('Product Amount in Stock')
plt.show()

plt.plot(df.index, df['Product Amount in Stock'], color='red')
plt.xlabel('Product index')
plt.ylabel('Amount in Stock')
plt.title('Product Amount in Stock')
plt.show()

plt.scatter(df.index, df['Price of Product'], color='blue')
plt.xlabel('Product index')
plt.ylabel('Price')
plt.title('Price of Product')
plt.show()

plt.bar(df.index, df['Price of Product'], color='purple')
plt.xlabel('Product index')
plt.ylabel('Price')
plt.title('Price of Product')
plt.show()
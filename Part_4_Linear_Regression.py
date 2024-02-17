import pandas as pd
import numpy as np

df = pd.read_csv('product_data.csv')

train_size = int(0.8 * len(df))
train_df = df[:train_size]
valid_df = df[train_size:]
X_train = train_df[['Product Item Number', 'Product Amount in Stock']].values
y_train = train_df['Price of Product'].values
X_valid = valid_df[['Product Item Number', 'Product Amount in Stock']].values
y_valid = valid_df['Price of Product'].values
X_train = np.insert(X_train, 0, 1, axis=1)
X_valid = np.insert(X_valid, 0, 1, axis=1)

print('Training set size:', X_train.shape[0])
print('Validation set size:', X_valid.shape[0])
beta = np.dot(np.linalg.inv(np.dot(X_train.T, X_train)), np.dot(X_train.T, y_train))
y_pred = np.dot(X_valid, beta)
mse = np.mean((y_pred - y_valid) ** 2)

print('Mean Squared Error:', mse)
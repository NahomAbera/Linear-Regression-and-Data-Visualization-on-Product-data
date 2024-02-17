# Linear Regression and Data Visualization on Product data
This is a Linear Regression and Data Visualization project made a data containing information on products. 

## Tools
This project is made using Python programming langauge and Jupyter Notebook computing software. 
In addition, I also used three Python libraries: Pandas, NumPy and Matplotlib.

## The Dataset
The dataset is a CSV file containing 464 rows of products and 5 columns. 
The columns are “Product Bar Code”, “Product Item Number”, “Product Amount in Stock”, “Sold Product Amount” and “Price of Product”. 
The first column, “Product Bar Code”, consists of 10-digit long numbers intended to facilitate the selling process. 
The next column, “Product Item Number”, contains 6-digit long numbers that are used to identify products. The third column, “Product Amount in Stock” shows the quantity of every product in the stock. 
The next one, “Sold Product Amount” describes how many items of each product were sold.
The last one, “Price of Product”, shows the price of every individual product. Moreover, each product has a unique Bar Code and Item Number.

## Part 1 - Data Cleaning
To begin the analysis, the CSV data was imported into a Pandas DataFrame using ‘pd.read_csv()’ function. 
Then the imported dataset is cleaned by removing any rows that had missing values by using ‘fillna()’ and ‘dropna()’ methods.          
The code will display an error message if there're fewer than 300 data points remained after the cleaning. 

## Part 2 - Descriptive Statistics
Next, the program calculates the mean, median, variance, and standard deviation of the products for two features(columns), “product amount in stock” and “price of a product”.
These statistics can be used to gain insight into the central tendencies and variability of the data. 

## Part 3 - Data Visualization
After calculating the statistics, the project have four charts to visualize the data. 
These charts are created using the Python Matplotlib library and labeled with appropriate axis labels, titles, and legends. 
The first two charts were a column bar chart and a line chart showing the amount of each product in stock. 
The third and fourth charts were a scatter chart and a bar chart showing the price of each product. 
The colors of the charts were green, red, blue, and purple respectively. 
![image](https://github.com/NahomAbera/Linear-Regression-and-Data-Visualization-on-Product-data/assets/144270821/71b0c823-0b94-4875-b788-14531e55d180)


![image](https://github.com/NahomAbera/Linear-Regression-and-Data-Visualization-on-Product-data/assets/144270821/6b3b7b49-b32d-4032-b8b6-ff831713cf14)

![image](https://github.com/NahomAbera/Linear-Regression-and-Data-Visualization-on-Product-data/assets/144270821/6093e256-f295-432f-bef1-63562cb8946b)

![image](https://github.com/NahomAbera/Linear-Regression-and-Data-Visualization-on-Product-data/assets/144270821/d3ae27ae-eb9a-48fe-9f40-a3545a2aba3a)

## Part 4 - Linear Regression Model
Finally, the data was split into training and validation sets, with 80% of the data used for training and 20% used for validation. 
The training set was used to train a linear regression model, and the validation set was used to test the model's accuracy. 
The variables ‘X_train’, ‘y_train’, ‘X_valid’, and ‘y_valid’ are used to store the input features and output target for each set.
The ‘np.insert()’ function is then used to add a column of ones to the input feature arrays, representing the intercept term in the linear regression equation.
The model then calculates the beta coefficients for the linear regression equation using the normal equation approach.
The ‘np.linalg.inv()’ function is used to compute the inverse of the product of the training input feature matrix and its transpose, and the resulting matrix is multiplied by the product of the training input feature matrix and the output target vector.
Then the model predicts the output target for the validation set using the beta coefficients and the input features.
Finally, the mean squared error was calculated to assess the accuracy of the model. 

## Conclusion
Overall, this project demonstrates how to import and clean a dataset, calculate statistics, visualize data using charts, and train a linear regression model using Python.
The insights gained from the statistics and charts can be used to make informed decisions about managing product inventory and pricing.



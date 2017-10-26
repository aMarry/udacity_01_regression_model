import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

# read data

data = pd.read_fwf('brain_body.txt')
x_train = data[['Brain']]
y_train = data[['Body']]

# train
linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)

# show
plt.scatter(x_train, y_train)
plt.plot(x_train, linear.predict(x_train))
plt.show()
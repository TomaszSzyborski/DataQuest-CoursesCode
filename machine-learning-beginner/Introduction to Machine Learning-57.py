## 3. Introduction to the data ##


columns = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin", "car name"]

cars = pd.read_table("auto-mpg.data", delim_whitespace=True, names=columns)

print(cars.head(5))

## 4. Exploratory data analysis ##


fig = plt.figure()

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

cars.plot("weight", "mpg", kind='scatter', ax=ax1)

cars.plot("acceleration", "mpg", kind='scatter', ax=ax2)

plt.show()

## 6. Scikit-learn ##

import sklearn
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(cars[["weight"]], cars["mpg"])

## 7. Making predictions ##

import sklearn
from sklearn.linear_model import LinearRegression
lr = LinearRegression(fit_intercept=True)
lr.fit(cars[["weight"]], cars["mpg"])
predictions = lr.predict(cars[["weight"]])
print(predictions[0:5])
print(cars["mpg"][0:5])

## 8. Plotting the model ##

plt.scatter(cars["weight"], cars["mpg"], c='red')
plt.scatter(cars["weight"], predictions, c='blue')

## 9. Error metrics ##

lr = LinearRegression()
lr.fit(cars[["weight"]], cars["mpg"])
predictions = lr.predict(cars[["weight"]])
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(cars["mpg"], predictions)
print(mse)

## 10. Root mean squared error ##

mse = mean_squared_error(cars["mpg"], predictions)
rmse = mse ** (1/2)
print(rmse)
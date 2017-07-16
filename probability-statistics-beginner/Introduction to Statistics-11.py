## 1. Introduction to Scales ##

car_speeds = [10,20,30,50,20]
earthquake_intensities = [2,7,4,5,8]
mean_car_speed = sum(car_speeds) / len(car_speeds)
mean_earthquake_intensities = sum(earthquake_intensities) / len(earthquake_intensities)

## 2. Discrete and Continuous Scales ##

day_numbers = [1,2,3,4,5,6,7]
snail_crawl_length = [.5,2,5,10,1,.25,4]
cars_in_parking_lot = [5,6,4,2,1,7,8]

import matplotlib.pyplot as plt
plt.plot(day_numbers, snail_crawl_length)
plt.show()

plt.plot(day_numbers, cars_in_parking_lot)
plt.show()

## 3. Understanding Scale Starting Points ##

fahrenheit_degrees = [32, 64, 78, 102]
yearly_town_population = [100,102,103,110,105,120]
population_zero = yearly_town_population
degrees_zero = [f + 459.67 for f in fahrenheit_degrees]

## 4. Working With Ordinal Scales ##

# Results from our survey on how many cigarettes people smoke per day
survey_responses = ["none", "some", "a lot", "none", "a few", "none", "none"]
survey_scale = ["none", "a few", "some", "a lot"]
survey_numbers = [survey_scale.index(response) for response in survey_responses]
average_smoking = sum(survey_numbers) / len(survey_numbers)

## 5. Grouping Values with Categorical Scales ##

# Let's say that these lists are both columns in a matrix.  Index 0 is the first row in both, and so on.
gender = ["male", "female", "female", "male", "male", "female"]
savings = [1200, 5000, 3400, 2400, 2800, 4100]
male_savings_list = [savings[i] for i in range(0, len(gender)) if gender[i] == "male"]
female_savings_list = [savings[i] for i in range(0, len(gender)) if gender[i] == "female"]

male_savings = sum(male_savings_list) / len(male_savings_list)
female_savings = sum(female_savings_list) / len(female_savings_list)

## 6. Visualizing Counts with Frequency Histograms ##

# Let's say that we watch cars drive by and calculate average speed in miles per hour
average_speed = [10, 20, 25, 27, 28, 22, 15, 18, 17]
import matplotlib.pyplot as plt
plt.hist(average_speed)
plt.show()

# Let's say we measure student test scores from 0-100
student_scores = [15, 80, 95, 100, 45, 75, 65]

## 7. Aggregating Values with Histogram Bins ##

average_speed = [10, 20, 25, 27, 28, 22, 15, 18, 17]
import matplotlib.pyplot as plt
plt.hist(average_speed, bins=6)
plt.show()

# As you can see, matplotlib groups the values in the list into the nearest bins.
# If we have fewer bins, each bin will have a higher count (because there will be fewer bins to group all of the values into).
# If there are more bins, the total for each one will decrease, because each one will contain fewer values.
plt.hist(average_speed, bins=4)
plt.show()

## 8. Measuring Data Skew ##

# We've already loaded in some numpy arrays. We'll make some plots with them.
# The arrays contain student test scores that are on a 0-100 scale.
import matplotlib.pyplot as plt

# See how there's a long slope to the left?
# The data is concentrated in the right part of the distribution, but some people also scored poorly.
# This plot has a negative skew.
plt.hist(test_scores_negative)
plt.show()

# This plot has a long slope to the right.
# Most students did poorly, but a few did really well.
# This plot has a positive skew.
plt.hist(test_scores_positive)
plt.show()

# This plot has no skew either way. Most of the values are in the center, and there is no long slope either way.
# It is an unskewed distribution.
plt.hist(test_scores_normal)
plt.show()

# We can test how skewed a distribution is using the skew function.
# A positive value means positive skew, a negative value means negative skew, and close to zero means no skew.
from scipy.stats import skew
positive_skew = skew(test_scores_positive)
negative_skew = skew(test_scores_negative)
no_skew = skew(test_scores_normal)

## 9. Checking for Outliers with Kurtosis ##

import matplotlib.pyplot as plt

# This plot is short. It is platykurtic.
# Notice how the values are distributed fairly evenly, and there isn't a large cluster in the middle.
# Student performance varied widely.
plt.hist(test_scores_platy)
plt.ylim(0,3500)
plt.xlim(0,1)
plt.show()

# This plot is tall. It is leptokurtic.
# Most students performed similarly.
plt.hist(test_scores_lepto)
plt.ylim(0,3500)
plt.xlim(0,1)
plt.show()

# The height of this plot neither short nor tall. It is mesokurtic.
plt.hist(test_scores_meso)
plt.ylim(0,3500)
plt.xlim(0,1)
plt.show()

# We can measure kurtosis with the kurtosis function.
# Negative values indicate platykurtic distributions, positive values indicate leptokurtic distributions, and values near 0 are mesokurtic.
from scipy.stats import kurtosis
kurt_platy = kurtosis(test_scores_platy)
kurt_lepto = kurtosis(test_scores_lepto)
kurt_meso = kurtosis(test_scores_meso)

## 10. Modality ##

import matplotlib.pyplot as plt

# This plot has one mode. It is unimodal.
plt.hist(test_scores_uni)
plt.show()

# This plot has two peaks. It is bimodal.
# This could happen if one group of students learned the material and another learned something else, for example.
plt.hist(test_scores_bi)
plt.show()

# More than one peak means that the plot is multimodal.
# We can't easily measure the modality of a plot, like we can with kurtosis or skew.
# Often, the best way to detect multimodality is to examine the plot visually.

## 11. Measures of Central Tendency ##

import matplotlib.pyplot as plt
# Let's put a line over our plot that shows the mean.
# This is the same histogram we plotted for skew a few screens ago.
plt.hist(test_scores_normal)
# We can use the .mean() method of a numpy array to compute the mean.
mean_test_score = test_scores_normal.mean()
# The axvline function will plot a vertical line over an existing plot.
plt.axvline(mean_test_score)

# Now we can show the plot and clear the figure.
plt.show()

# When we plot test_scores_negative, which is a very negatively skewed distribution, we see that the small values on the left pull the mean in that direction.
# Very large and very small values can easily skew the mean.
# Very skewed distributions can make the mean misleading.
plt.hist(test_scores_negative)
plt.axvline(test_scores_negative.mean())
plt.show()

# We can do the same with the positive side.
# Notice how the very high values pull the mean to the right more than we would expect.
plt.hist(test_scores_positive)
plt.axvline(test_scores_positive.mean())
plt.show()
mean_normal = test_scores_normal.mean()
mean_negative = test_scores_negative.mean()
mean_positive = test_scores_positive.mean()

## 12. Calculating the Median ##

# Let's plot the mean and median side-by-side in a negatively skewed distribution.
# Unfortunately, arrays don't have a nice median method, so we have to use a numpy function to compute it.
import numpy
import matplotlib.pyplot as plt

# Plot the histogram
plt.hist(test_scores_negative)
# Compute the median
median = numpy.median(test_scores_negative)

# Plot the median in blue (the color argument of "b" means blue)
plt.axvline(median, color="b")

# Plot the mean in red
plt.axvline(test_scores_negative.mean(), color="r")

# Notice how the median is further to the right than the mean.
# It's less sensitive to outliers, and isn't pulled to the left.
plt.show()

## 14. Removing Missing Data ##

import pandas
f = "titanic_survival.csv"
titanic_survival = pandas.read_csv(f)

# Luckily, pandas DataFrames have a method that can drop rows that have missing data
# Let's look at how large the DataFrame is first
print(titanic_survival.shape)

# There were 1,310 passengers on the Titanic, according to our data
# Now let's drop any rows that have missing data
# The DataFrame dropna method will do this for us
# It will remove any rows with that contain missing values
new_titanic_survival = titanic_survival.dropna()

# Hmm, it looks like we were too zealous with dropping rows that contained NA values
# We now have no rows in our DataFrame
# This is because some of the later columns, which aren't immediately relevant to our analysis, contain a lot of missing values
print(new_titanic_survival.shape)

# We can use the subset keyword argument to the dropna method so that it only drops rows if there are NA values in certain columns
# This line of code will drop any row where the embarkation port (where people boarded the Titanic) or cabin number is missing
new_titanic_survival = titanic_survival.dropna(subset=["embarked", "cabin"])

# This result is much better. We've only removed the rows we needed to.
print(new_titanic_survival.shape)
new_titanic_survival = titanic_survival.dropna(subset=["age", "sex"])

## 15. Plotting Age ##

# We've loaded the clean version of the data into the variable new_titanic_survival
import matplotlib.pyplot as plt
import numpy
plt.hist(new_titanic_survival["age"])
plt.axvline(numpy.median(new_titanic_survival["age"]), color="b")
plt.axvline(new_titanic_survival["age"].mean(), color="r")
plt.show()

## 16. Calculating Indexes for Age ##

import numpy
from scipy.stats import skew
from scipy.stats import kurtosis
mean_age = new_titanic_survival["age"].mean()
median_age = numpy.median(new_titanic_survival["age"])
skew_age = skew(new_titanic_survival["age"])
kurtosis_age = kurtosis(new_titanic_survival["age"])
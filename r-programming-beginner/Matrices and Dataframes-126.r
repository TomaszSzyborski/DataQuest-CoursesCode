## 2. Reading Data into R ##

congress <- read.csv("114_congress.csv")
whiteHouse <- read.csv("2015_white_house.csv")

## 4. Creating a Matrix ##

# Create a simple matrix with three rows and two columns
B <- matrix(c(1,2,3,4,5,6), 3, 2)
print(B)
# Create actor matrix with two rows and three columns
C <- matrix(c("Rambo", "Chuck Norris", "Arnold", "Steven Seagal", "John Wayne", "Steve McQueen"), 2, 3)

## 5. Using Indexes to Get a Matrix Element ##

# Print the first column of the second row
print(C[2,1])

# Print the third column of the second row
print(C[2,3])
c22 <- C[2,2]
c13 <- C[1,3]

## 6. Using Indexes to Get Rows and Columns ##

# The first row of C
print(C[1,])

# The first column of C
print(C[,1])
c20 <- C[2,]
c03 <- C[,3]

## 8. Accessing Dataframe Columns ##

# Get the salary column from the whitehouse data
salary <- whiteHouse["Salary"]

# Get the salary of the first employee in our data (from the salary column of the first row)
firstSalary <- whiteHouse[1,"Salary"]
whiteHouseNames <- whiteHouse["Name"]
status5 <- whiteHouse[5, "Status"]

## 9. Finding the Average Salary with the sum and nrow Functions ##

# Enter your code here
averageSalary <- sum(whiteHouse["Salary"]) / nrow(whiteHouse)

## 10. Finding the Highest and Lowest Salaries With min and max ##

# Enter your code here
highestSalary <- max(whiteHouse["Salary"])
lowestSalary <- min(whiteHouse["Salary"])

## 11. Indexing Method Results Have Subtle Differences ##

# Returns a dataframe
salaryFrame <- whiteHouse["Salary"]

# Returns a vector
salaryVector <- whiteHouse[,"Salary"]

whiteHouseNames <- whiteHouse["Name"]

whiteHouseNamesVector <- whiteHouse[,"Name"]

## 12. Finding the Indexes for a Vector's Minimum and Maximum Values ##

# Find the index of the person with the lowest salary
# This is where knowing what kind of indexing returns what value comes in handy  
# We need a vector
minimumIndex <- which.min(whiteHouse[,"Salary"])
# Extract the row containing the lowest salary
minimumSalaryRow <- whiteHouse[minimumIndex,]
# Get the name column from that row
lowestEarner <- minimumSalaryRow["Name"]
# Print the name of the White House employee who earned the least
print(lowestEarner)
maximumIndex <- which.max(whiteHouse[,"Salary"])
maximumSalaryRow <- whiteHouse[maximumIndex,]
highestEarner <- maximumSalaryRow["Name"]
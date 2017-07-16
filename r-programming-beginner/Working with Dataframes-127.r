## 2. Calling Functions ##

# Define the add function
add <- function(a, b){
    return(a + b)
}

# Call the add function with the arguments 1 and 2
print(add(1, 2))
d <- add(5, 10)

## 3. Defining a Function ##

# Enter your code here
subtract <- function(a, b){
        return(a - b)
    }

d <- subtract(50, 10)

## 4. Reading in the Data ##

# Enter your code here
ufos <- read.csv("ufo_sightings.csv")

## 5. Previewing the Dataframe with head and tail ##

# Print the first five rows in the dataframe
print(head(ufos, 5))
print(tail(ufos, 5))

## 6. Calculating UFO Sightings Per Year ##

# Enter your code here
print(str(ufos))

## 7. Converting a Vector's Type ##

dateReported <- as.character(ufos$date.reported)
dateSighted <- as.character(ufos$date.sighted)

## 8. Extracting Part of a Character with the Substring Function ##

# This extracts "2004" from our string
date <- "20040415"
print(substr(date, 1, 4))

# This extracts the year from each string in the vector
dates <- c("20040415", "20080515")
print(substr(dates, 1, 4))
years <- substr(dateSighted, 1, 4)

## 9. Generating a Table of Sightings Per Year ##

# Create a small vector containing a few years
selectedYears <- c("2004", "2002", "1992", "2005", "2006", "2005", "2004")

# Create and print a table
print(table(selectedYears))
print(table(years))

## 10. Working with Dates ##

dateSighted <- as.character(ufos$date.sighted)
dateSighted <- as.Date(dateSighted, "%Y%m%d")
dateReported <- as.character(ufos$date.reported)
dateReported <- as.Date(dateReported, "%Y%m%d")

## 11. Subtracting Vectors ##

# Enter your code here
delay <- dateReported - dateSighted

## 12. Making a Table of Reporting Delays ##

# Enter your code here
print(table(delay))

## 13. Cleaning and Combining the Data ##

# Enter your code here
dates <- data.frame(dateReported, dateSighted)

## 14. Introduction to Boolean Vectors ##

a <- c(1,2,3)
b <- c(5,2,5)

# Find when each element in a is greater than the corresponding element in b
print(a > b)
positiveDelays <- delay > 0

print(positiveDelays)

## 15. Filtering With Boolean Vectors ##

filter <- c(FALSE, FALSE, TRUE, TRUE)
bestIceCreamFlavors <- data.frame(c("Peanut Butter Oreo", "Cookie Dough", "Mint Chocolate Chip", "Peanut Butter Cup"))
twoFlavors <- bestIceCreamFlavors[filter,]
print(twoFlavors)
positiveDates <- dates[positiveDelays,]

## 16. Removing Null Values ##

# Enter your code here
cleanDates <- na.omit(positiveDates)

## 17. Remaking our Table ##

# Enter your code here
delay <- cleanDates$dateReported - cleanDates$dateSighted
print(table(delay))
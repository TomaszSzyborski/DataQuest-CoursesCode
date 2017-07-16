## 2. Introduction ##

SELECT * FROM recent_grads LIMIT 5;

## 4. Calculating Group-Level Summary Statistics ##

SELECT Major_category, AVG(ShareWomen) FROM recent_grads GROUP BY Major_category;

## 5. Renaming Columns With the AS Statement ##

SELECT SUM(Men) AS total_men, SUM(Women) AS total_women FROM recent_grads;

## 6. Practice: Using GROUP BY ##

SELECT Major_category, AVG(Employed) / AVG(Total) AS share_employed FROM recent_grads GROUP BY Major_category;

## 7. Querying Virtual Columns With the HAVING Statement ##

SELECT Major_category, AVG(Low_wage_jobs) / AVG(Total) AS share_low_wage FROM recent_grads GROUP BY Major_category HAVING share_low_wage > .1;

## 8. Rounding Results With the ROUND Function ##

SELECT ROUND(ShareWomen, 4), Major_category FROM recent_grads LIMIT 10;

## 9. Nesting functions ##

SELECT Major_category, ROUND(AVG(College_jobs) / AVG(Total), 3) AS share_degree_jobs FROM recent_grads GROUP BY Major_category HAVING share_degree_jobs < .3;
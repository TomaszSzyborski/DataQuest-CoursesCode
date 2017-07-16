## 4. Querying a SQLite Database ##

SELECT Rank,Major FROM recent_grads;

## 5. Specifying Column Order for Our Results ##

SELECT Major,Rank FROM recent_grads;

## 6. Practice: Selecting Columns With SELECT ##

SELECT Rank,Major_code,Major,Major_category,Total FROM recent_grads;

## 7. Filtering With the WHERE Statement ##

SELECT Major,ShareWomen FROM recent_grads WHERE ShareWomen>0.5;

## 8. Practice: Filtering With WHERE Statements ##

SELECT Major,Employed FROM recent_grads WHERE Employed > 10000;

## 9. Limiting the Number of Results ##

SELECT Major FROM recent_grads WHERE Employed>10000 LIMIT 10;
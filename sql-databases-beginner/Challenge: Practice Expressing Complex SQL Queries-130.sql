## 2. Use SELECT and LIMIT to Filter Results ##

select College_jobs, Median, Unemployment_rate from recent_grads limit 20;

## 3. Use WHERE to Filter Results ##

select major from recent_grads where Major_category='Arts' limit 5;

## 4. Express Criteria With Operators ##

select Major,Total,Median,Unemployment_rate from recent_grads 
where (Major_category != 'Engineering') and (Unemployment_rate > 0.065 or Median <= 50000);

## 5. Order Your Results ##

select major
from recent_grads
where Major_category!='Engineering'
order by major desc
limit 20;
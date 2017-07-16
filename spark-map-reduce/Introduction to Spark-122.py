## 3. Resilient Distributed Data Sets (RDDs) ##

raw_data = sc.textFile("daily_show.tsv")
raw_data.take(5)

## 6. Pipelines ##

daily_show = raw_data.map(lambda line: line.split('\t'))
daily_show.take(5)
# Hit check to see the output

## 8. ReduceByKey() ##

tally = daily_show.map(lambda x: (x[0], 1)).reduceByKey(lambda x,y: x+y)
print(tally)
print(tally.take(5))

## 9. Explanation ##

tally.take(tally.count())

## 10. Filter ##


def filter_year(line):
    if line[0] == 'YEAR':
        return False
    else:
        return True

filtered_daily_show = daily_show.filter(lambda line: filter_year(line))

print(filtered_daily_show.take(5))

## 11. Practice with Pipelines ##

filtered_daily_show.filter(lambda line: line[1] != '') \
                   .map(lambda line: (line[1].lower(), 1)) \
                   .reduceByKey(lambda x,y: x+y) \
                   .take(5)
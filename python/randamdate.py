from datetime import date, timedelta
import numpy as np

# initializing dates ranges 
test_date1, test_date2 = date(2015, 6, 3), date(2015, 7, 1)

# printing dates 
print("The original range : " + str(test_date1) + " " + str(test_date2))

# initializing K
K = 7

# getting days between dates
dates_bet = test_date2 - test_date1
total_days = dates_bet.days

# create an array of total days and select K random values without replacement
randays = np.random.choice(total_days, K, replace=False)

# getting random dates 
res = [test_date1 + timedelta(days=int(day)) for day in randays]

# printing 
print("K random dates in range : " + str(res))

#1
from datetime import datetime as dt, timedelta as diff
today = dt.now()
new_date = today - diff(5)
print("Current Date:", today)
print("Subtract five days from current date: ", new_date)

#2
yesterday = today - diff(1)
tomorrow = today + diff(1) 
print('Yesterday: ',yesterday)
print('Today: ',today)
print('Tomorrow: ',tomorrow)

#3
nomicro = dt.today().replace(microsecond=0)
print("Today without microsecond: ", nomicro)

#4
datestr1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
datestr2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")
date1 = dt.strptime(datestr1, "%Y-%m-%d %H:%M:%S")
date2 = dt.strptime(datestr2, "%Y-%m-%d %H:%M:%S")
time_difference = (date2 - date1).total_seconds()
print("The difference between the two dates is ", time_difference, " seconds.")
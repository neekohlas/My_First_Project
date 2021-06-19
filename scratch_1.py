#Goal: Print the number of days in the year based on the number of days in each month.

#Establish number of days in each month with a list.

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#Create variable for days in year.

num_days_in_year = 0

#For loop with len function. Add each sub-element to num_days and repeat.

for i in range(len(days_in_month)):
    num_days_in_year += days_in_month [i]
#Recall this is code for: num_days_in_year = num_days_in_year + days_in_month [i]

print(num_days_in_year)

#Reset number for v. 2 of this formula
num_days_in_year = 0

#For loop that automatically reads number of sub-elements based on list "days_in_month"

for i in days_in_month:
    num_days_in_year += i

print(num_days_in_year)

#Reset number for v. 3 of this formula
num_days_in_year = 0

#There's a sum function that will do this for you.  Easy!

num_days_in_year = sum(days_in_month)

print(num_days_in_year)
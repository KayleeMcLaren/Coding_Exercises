
#  function to check if a year is a leap year

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# function which checks if input is valid and returns the number of days in a month
# it also calls the is_leap function to check is the year is leap and if the month is '2', or February. If so, it returns 29 days instead of the usual 28 days for February

def days_in_month(year, month):

    if month > 12 or month < 1:
        return "Invalid month"

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]  # the number of days is determined by using the month as the idex in the month_days list, minus 1 as indexing starts at 0. 
                                  # so if the month is entered as 1 (January), 1 - 1 gives the index of 0 which is 31 days for January.


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

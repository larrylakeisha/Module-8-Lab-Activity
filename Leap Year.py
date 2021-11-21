# Lakeisha Larry
# November 21, 2021

# This program returns if the year is a leap year or false if it is not


def is_leap(year):
    leap = False

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    return leap


year = int(input("Enter the year: "))
print(is_leap(year))

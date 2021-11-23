# Lakeisha Larry
# November 21, 2021

# This program takes a list and prints if the value is 5 is in the list

def printValue(value, list):
    for i in list:
        if i == value:
            ans = "The value is five."
            return ans

print(printValue(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

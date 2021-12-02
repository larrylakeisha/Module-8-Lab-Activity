# Lakeisha Larry
# November 21, 2021

# This program takes a list and prints if the value is 5 is in the list
'''
input: list
define function to check whether there is 5 in the list
call function

def printValue(value, list):
    for i in list:
        if i == value:
            ans = "The value is five."
            return ans

print(printValue(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
'''
def checkValue(list):
    value  = 5
    if value in list:
        print('five is in the list')
        print(list)
    else:
        print('five is not the list')

list = [2, 3, 5, 1]
checkValue(list)


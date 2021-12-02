# Lakeisha Larry
# November 21, 2021

# This program takes two inputs and prints if sum is greater and less than or equal to 10
'''
Same as Pb#1
Define function: sum of two inputs are compared to 10
Get input
Call function with passing the two inputs.

def numbercomparsion():
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))

if a == b:
    print("sum of",a, "and", b, "is equal to", a+b)
if a < b:
    print("sum of", a, "and", b, "is greater than 10")
if a > b:
    print("sum of", a, "and", b, "is less than 10")
'''
def numbercomparsion(a, b):
   if a + b > 10:
        print("sum of {} and {} is greater than 10. ".format(a, b))
   elif a + b < 10:
        print("sum of {} and {} is less than 10. ".format(a, b))
   else:
        print("sum of {} and {} is equal to 10. ".format(a, b))

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
numbercomparison(a,b)

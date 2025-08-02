#Program to calculate area of circle.

# import math
# r = float(input('Enter the area of circle: '))
# area = math.pi * r * r
# print("Area of circle: ", area)

#Program to express digit in word.
# num = int(input("Enter the digit to express it in word: "))
# if num == 1:
#     print("one")
# if num == 2:
#     print("two")

#Program to print whether a number is odd or even.
# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#     print("Number is Even.")
# else:
#     print("Number is Odd.")

#Program to know if a number is positive, negetive or zero
# x = int(input("Enter a number:"))
# if (x < 0):
#     print(x, "is negetive number")
# elif x > 0:
#     print(x, "is positive")
# else:
#     print("Entered number is ZERO")

# printing type of x after assingning with interger datatype.
# x = 5
# print(type(x))

#  printing type of y after assingning with input() and entering the value manually.
# y = input("Enter a number")
# print(y)
# print(type(y))

#Program to display numbers between 1 to 10 using while loop:
# 1st way
# x = 10
# while x >= 1:
#     print(x)
#     x -= 1
#     print("-----------")
# print("END")
# #2nd way
# x = 1
# while x <= 10:
#     print(x)
#     x += 1
#     print("-----------")
# print("END")

#Program to print even numbers from 100 to 200
# x = 100
# while x >= 100 and x <= 200:
#     print(x)
#     x += 2

#Program to display characters of a string using for loop
# name = "ADITYA"
# for ch in name:
#     print(ch)  

#using for loop, display odd numbers from 1 to 10 using range 
# for i in range(1,10,2):
#     print(i)

#using for loop, display numbers from 10 to 1 using range.
# for i in range(10,0,-1):
#     print(i)

#program to display and find the sum of a list of numbers using for loop
# lst = [10, 20, 30, 40, 50]
# sum = 0
# for elements in lst:
#     print(elements)
#     sum += elements
# print("Sum of elements of list is : ", sum)

#program to display stars in right angled triangle.
for i in range(1,11):
    for j in range(1,i+1):
        print('*', end='')
    print()
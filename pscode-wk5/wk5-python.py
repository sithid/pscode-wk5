###################################################################################################################
# Name: wk5-python
# Author: James D Glosser
# Last Update: 06/18/2024 @ 12:27 AM
# Notes: I like to code, even just simple excersices.
# Purpose: Convert wk5 excercises from pseudocode to python.
###################################################################################################################

import os, sys
clear = lambda: os.system('cls')

###################################################################################################################
#   Exercise 1:
#       Calculate the sum of two numbers.
#       Print result.
###################################################################################################################

print( "First Task: Find the sum of 2 numbers." )

num1 = input( "Enter your first number: " )
num2 = input( "Enter your second number: " )

sum = int(num1) + int(num2)

print( f"The sum of {num1} and {num2} is {sum}" )

temp = input ("Continue? ( y / n ) ")

if temp == 'n':
    sys.exit(0)

clear()

###################################################################################################################
#   Exercise 2:
#       Check if a number is odd or even.
#       Print result.
###################################################################################################################

print( "Second Task: Decide if the given number is odd or even." )

num1 = int(input( "Enter your number: " ))

if num1 % 2 == 0:
    print( f"{num1} is an even number!" )
else:
    print( f"{num1} is an odd number!" )

temp = input ("Continue? ( y / n ) ")

if temp == 'n':
    sys.exit(0)

clear()

###################################################################################################################
#   Exercise 3: 
#       Write pseudocode that will perform the following:   
#           A) Read in 5 separate numbers.   
#           B) Calculate the average of the five numbers.
#           C) Find the smallest (minimum) and the largest (maximum) of the five entered numbers.
#           D) Write out the results found from steps b and c with a message describing what they are.
####################################################################################################################

print( "Find the average of 5 numbers." )

num = 0
min = 0
max = 0
sum = 0

for i in range(5):
    if i == 0:
        num = int(input ("Enter your first value: "))
    elif i == 4:
        num = int(input ("Enter your last value: "))
    else:
        num = int(input ("Enter your next value: "))

    sum += int(num)

    if num < min or min == 0:
        min = num
    elif num > max or max == 0:
        max = num
else:
    average = sum / 5

print( f"The smallest number is {min}.  The largest number is {max}." )
print( f"The sum of these 5 numbers is {sum}." )
print( f"The average of these 5 numbers is {average}." )

temp = input ("Continue? ( y / n ) ")

if temp == 'n':
    sys.exit(0)

clear()

# FizzBuzz is a challenge that involves writing code that labels numbers divisible by three as “Fizz,”
# four as “Buzz” and numbers divisible by both as “FizzBuzz.” Here’s how to solve it in Python. 
num = int(input ("Enter the number to end after: "))

fizz = 0
buzz = 0
fizzbuzz = 0
none = 0

for i in range(num+1):
    if i % 3 == 0:
        if i %4 == 0:
            print(f"FizzBuzz")
            fizzbuzz += 1
        else:
            print( f"Fizz")
            fizz += 1
    elif i % 4 == 0:
        print( "Buzz")
        buzz += 1
    else:
        print(f"{i}")
        none += 1
else:
    print(f"Divisible by 3: {fizz}, Divisible by 4: {buzz}, Divisible by both: {fizzbuzz}, Divisible by neither: {none}")
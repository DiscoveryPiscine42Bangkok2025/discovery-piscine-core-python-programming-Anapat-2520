#!/usr/bin/env python3
First_number = int(input("Enter the first number : "))
Second_number = int(input("Enter the second number : "))
total = First_number * Second_number
print(total)
if total > 0:
    print("The result is positive.")
if total < 0:
    print("The result is negative.")
if total == 0:
    print("The result is positive and negative.")
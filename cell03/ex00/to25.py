#!/usr/bin/env python3
number = int(input("Enter a number less than 25 : "))
i = number
if number > 25:
    print("Error")
else :
    while i < 26:
        print("Inside the loop, my variable is", i )
        i += 1
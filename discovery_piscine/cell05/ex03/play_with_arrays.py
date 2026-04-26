#!/usr/bin/env python3
number = "2 8 9 48 8 22 -12 2"
array = list(map(int, number.split()))
print(array)
new_array = []
for i in range(len(array)):
    if array[i] > 5:
        new_array.append(array[i] + 2)
print(set(new_array))
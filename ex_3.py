#!/usr/bin/env python3

def f(data):
    for i in range(len(data)):
        data[i] = abs(data[i])
    return sorted(data)

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
# Реализация задания 3
print(data)
print(sorted(data, key = lambda key: abs(key)))
print(sorted(data, key = abs ))




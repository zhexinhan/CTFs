#!/usr/bin/python3.6

import math

def is_prime(number):
    if 2 == number:
        return True
    elif number <= 1:
        return False
    else:
        for i in range(2, math.ceil(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

def get_digit_sum(number):
    sum = 0
    while (number):
        sum += number % 10
        number //= 10
    return sum

first_prime = 0
second_prime = 0
start = 1000000
while (True):
    if is_prime(start) and is_prime(get_digit_sum(start)):
        if first_prime:
            second_prime = start
            break
        else:
            first_prime = start
    start += 1

print(str(first_prime) + str(second_prime))

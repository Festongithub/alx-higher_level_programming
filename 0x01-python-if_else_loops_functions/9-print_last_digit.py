#!/usr/bin/python3

def print_last_digit(number):
    last_digit = number % 10
    print(abs(last_digit), end="")
    return (abs(last_digit) % 10)

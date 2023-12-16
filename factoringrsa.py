#!/usr/bin/python3
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = 2
    y = 2
    d = 1
    f = lambda x: (x ** 2 + 1) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    return d

def factorize_rsa_numbers(numbers):
    factors = []
    for n in numbers:
        factors.append(pollards_rho(n))
    return factors

def append_factors_to_file(filename, numbers, factors):
    with open(filename, 'w') as file:
        for i in range(len(numbers)):
            file.write(f"{numbers[i]}={factors[i]}*{numbers[i] // factors[i]}\n")

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

if __name__ == "__main__":
    input_filename = "tests/test00"
    numbers = read_numbers_from_file(input_filename)
    factors = factorize_rsa_numbers(numbers)
    append_factors_to_file(input_filename, numbers, factors)

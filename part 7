
import math

def calculate_volume(length, width, height):
    return length * width * height

def count_digits(num):
    count = 0
    while num:
        count += 1
        num //= 10
    return count

def reverse_integer(num):
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num

def calculate_sum_up_to_N(N):
    return sum(range(1, N + 1))

def babylonian_sqrt(N, tolerance=1e-7, max_iterations=100):
    x = N / 2.0
    for _ in range(max_iterations):
        next_x = 0.5 * (x + N / x)
        if abs(x - next_x) < tolerance:
            return next_x
        x = next_x
    return x

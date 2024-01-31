import random


def calculate_gcd(num1, num2):
    """finds the greatest common divisor (gcd) using the Euclidean Algorithm"""
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def get_numbers_and_answer():
    """gets numbers and gcd in a str type"""
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    numbers = f'{num1} {num2}'
    gcd = calculate_gcd(num1, num2)

    return numbers, str(gcd)

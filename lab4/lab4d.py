#!/usr/bin/env python3

def first_five(input_string):
    """
    Accepts a single string argument and returns the first five characters.
    """
    return input_string[:5]

def last_seven(input_string):
    """
    Accepts a single string argument and returns the last seven characters.
    """
    return input_string[-7:]

def middle_number(input_number):
    """
    Accepts an integer argument and returns a string containing the second and third characters in the number.
    """
    number_str = str(input_number)  # Convert the integer to a string
    return number_str[1:3]  # Get the second and third characters

def first_three_last_three(arg1, arg2):
    """
    Accepts two string arguments and returns a single string
    that starts with the first three characters of arg1 and ends with
    the last three characters of arg2.
    """
    return arg1[:3] + arg2[-3:]

if __name__ == '__main__':
    # Sample runs
    str1 = 'Hello World!!'
    str2 = 'Seneca College'
    num1 = 1500
    num2 = 1.50

    print(first_five(str1))                   # Output: Hello
    print(first_five(str2))                   # Output: Senec
    print(last_seven(str1))                   # Output: World!!
    print(last_seven(str2))                   # Output: College
    print(middle_number(num1))                 # Output: 50
    print(middle_number(num2))                 # Output: .5
    print(first_three_last_three(str1, str2)) # Output: Helege
    print(first_three_last_three(str2, str1)) # Output: Send!!

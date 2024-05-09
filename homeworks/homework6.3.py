def multiply_digits(number):
    while number > 9:
        digits = [int(digit) for digit in str(number)]
        result = 1
        for digit in digits:
            result *= digit
        number = result
    return number

users_digits = int(input('Write digits: '))
print(multiply_digits(users_digits))


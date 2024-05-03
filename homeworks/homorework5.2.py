print('1.Muliply , 2.Summ , 3.Subtraction , 4.Division ')

while True:
    first_digit = int(input('Write the first digit: '))
    second_digit = int(input('Write the second digit: '))
    action = input('Choose the action (1/2/3/4): ')

    
    if action not in ['1', '2', '3', '4']:
        print("Invalid action. Please choose from 1 to 4.")
        continue
    
    if action == '1':
        print(first_digit * second_digit)
    if action == '2':
        print(first_digit + second_digit)
    if action == '3':
        print(first_digit - second_digit)
    if action == '4':
        if second_digit == 0:
            print('Error, you cannot divide by zero.')
        else:
            print(first_digit / second_digit)
    user_action = input('Do you want to continue calculating? (Y/N): ')
    if user_action.lower() != 'y':
        break


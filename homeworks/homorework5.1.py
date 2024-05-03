import string
import keyword

var_name = input('Write your variable name: ')
if  not var_name.islower():
    if '_' in var_name:
        print('alright')
    else:
        print('error')
elif var_name[0].isdigit():
    if '_' in var_name:
        print('alright')
    else:
        print('error')
elif any(char in string.punctuation for char in var_name):
    if '_' in var_name:
        print('alright')
    else:
        print('error')
elif var_name in keyword.kwlist:
    print('error')
else:
    print('allright')

    
    
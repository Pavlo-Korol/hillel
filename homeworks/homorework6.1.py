import string
users_data = input('Write your letters: ')

def find_letters_range(input_str):
    start_char, end_char  = input_str.split('-')
    letters =  string.ascii_letters
    start_index = letters.index(start_char)
    end_index = letters.index(end_char)
    return letters[start_index:end_index + 1] , start_index , end_index

print(find_letters_range(users_data))

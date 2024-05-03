import string

user_str = input('Write your string: ')

def do_hashtag(user_str):
    for char in string.punctuation:
        user_str = user_str.replace(char,'') 
    cleaned_str = user_str.title().replace(' ','')
    return '#' + cleaned_str[:139]  


print(do_hashtag(user_str))

    

    
        
    
    
            
        
    
    
        
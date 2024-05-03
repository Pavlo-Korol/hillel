import string

user_str = '!h^e@l;:l,o i a!m b,o%b'

def do_hashtag(user_str):
    for char in string.punctuation:
        user_str = user_str.replace(char,'') 
    cleaned_str = user_str.title().replace(' ','')
    return '#' + cleaned_str[:140]  


print(do_hashtag(user_str))

    

    
        
    
    
            
        
    
    
        
def plaindrome(s):
    rev_string=""
    for char in s:
       rev_string = char + rev_string

    if s == rev_string:
        return True
    else:
        return False 
        

text=input('Enter text: ')
print(plaindrome(text))
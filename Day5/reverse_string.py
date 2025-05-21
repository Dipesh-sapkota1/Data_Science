# def reverse(s):
#     if s == 0:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]

# text=input('Enter text: ')

# print(reverse(text))

# def rev(s):
#    return s[::-1]

# text=input('Enter text: ')
# print(f'reversed text :{rev(text)}')


def rev(s):
    reverse_string=""
    for char in s:
       reverse_string = char + reverse_string

    return reverse_string 

text=input('Enter text: ')
print(f'reversed text :{rev(text)}')
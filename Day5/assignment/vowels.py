vowels = ['a', 'e', 'i', 'o', 'u']
consonants = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
    'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
]
 

def sound(s):
    C_vow = 0
    C_const = 0
    for char in (s):
        lower_char = char.lower()
        if lower_char in vowels:
            C_vow += 1
        elif lower_char in consonants:
            C_const += 1
    return C_const, C_vow


text = input("Enter a string: ")
(consonants, vowels) = sound(text)

print(f"Total vowels: {vowels}\nTotal consonants: {consonants}")
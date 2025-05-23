def sum(num):
    numbers = [int(char) for char in num]
    c = 0
    for n in numbers:
        c += n

    return c
    
number = input("Enter number: ")
print(sum(number))

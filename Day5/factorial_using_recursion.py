def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
number=int(input('Enter number: '))
print(f'The factorial of {number} is {fact(number)}')   
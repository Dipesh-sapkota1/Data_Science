def greatest(n):
    n = "".join(sorted(n))
    for char in n:
        n = [int(char) for char in n]
    return n[-1]

number = input("Enter number: ")
print(greatest(number))

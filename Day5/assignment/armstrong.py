def armstrong(n):
    digits = len(n)
    total = 0
    for x in n:
        total += int(x)**digits
    return total


number = input("Enter number: ")

result = armstrong(number)

if (result == int(number)):
    print(True)
else:
    print(False)

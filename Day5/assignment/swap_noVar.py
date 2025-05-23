a = int(input("Enter your first value: "))
b = int(input("Enter your second value: "))


for i in range(a + 1):
    for j in range(b + 1):
        a = j
b = i



print(f"Your fist value is now: {a}")
print(f"Your second value is now: {b}")
# Create a fun to check prime numbers
def prime(n):
    if n > 1:        
        if n % 1 == 1: 
            if n % n == 0:    
                return True
        else:
            return False


x = int(input("Enter starting num: "))
y = int(input("Enter ending num: "))

# print prime numbers in given range 
for i in range(2, y):
    if prime(i):
        print(i)


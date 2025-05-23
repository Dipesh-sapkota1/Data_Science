fib = []

def fibocacci(n):
     a=0
     b=1
     for _ in range(n):
       fib.append(a)
       a,b = b,a+b
     return fib

number = int(input("Enter a number: "))
if number<=0:
    print('Please enter positive integers')
else:
    print(f'The fibonacci series up to nth terms is: {fibocacci(number)}')

# x = lambda a: a + 10
# print(x(5))

# x = lambda a, b : a * b
# print(x(5, 6))


# check_even_odd = lambda x, : 'even' if x % 2 == 0 else "odd"

# def check(x): return 'Neutral' if x == 0 else (
#     "Greater" if x > 0 else "Negative")


# a = float(input("Enter num: "))
# print(check(a))

# make if else ladder m=>90 A-grade, 80 A- >= 70 b+, =>c, 50 = d or below fail
# m = float(input("Enter grade: "))

# if m >= 90:
#     print("Grade: A")
# elif m >= 80:
#     print("Grade: A-")
# elif m >= 70:
#     print("Grade: B+")
# elif m >= 50:
#     print("Grade: D")
# else:
#     print("Failed")


# income = float(input("Enter income: "))


# if  income <= 250000:
#     print("Tax rate: no tax")
# elif  income >= 250001 and income < 500000:
#     print(f"Your income tax is: {0.5 * income}")    
# elif  income >= 500001 and income < 1000000:
#     print(f"Your income tax is: {0.10 * income}") 
# elif  income > 1000000:
#     print(f"Your income tax is: {0.13 * income}")        

# train ticket fair calulator based on distance and class
# write a program talk takes distance in km 

# 1 = first class
# 2 = sec class
# 3 = sleepers class

# fair chart
# perkm = 1st 5$
# perkm = 2st 3$
# perkm = 3rd 1$

# if distance > 500km give 10% dis

# Rate of train class
first = 5
second = 3
sleepers = 1


# Train class input validation
while True:
    train_class = input('Enter class: ')
    if int(train_class) < 3:
        break
    else:
        print("There are only three classes. Please enter class below four only.")

distance = float(input('Enter distance: '))


def tic_calc(distance, Class):
    if Class == '1':
        Class = first
    elif Class == '2':
        Class = second
    elif Class == '3':
        Class = sleepers
    else:
        return                   
    
    fair = distance * Class

    if distance > 500:
      return dis_amt(fair)
    else:
        return fair
    
# Discount function
def dis_amt(f):
    return f - (0.10 * f)


print(f"Your fare is: {tic_calc( distance,train_class,)}$")
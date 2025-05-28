## write a match case if grade > 80 distinction, > 70 1st div, > 60 2nd div , below 60 fail and other invalid.  

g = int(input("Enter grade: "))

def grade(score):
    match score:
        case p if 80 <= p <= 100:
            print("Distinction")
        case p if 70 <= p <= 79:
            print("First division")
        case p if 60 <= p <= 69:
            print("Second division")
        case p if 0 <= p <= 59:
            print("Fail")
        case _:
            print("Invalid input. Please enter a grade between 0 and 100.")

grade(g)

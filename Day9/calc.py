input1 = float(input("Enter first input: "))
input2 = float(input("Enter second input: "))
input3 = input("Enter operator: ")

def eval(a,b,operator):

    match operator:
        case '+':
            add = lambda a,b: a + b
            return add(a,b)
        case '-':
            sub = lambda a,b: a - b
            return sub(a,b)
        case '*':
            mul = lambda a,b: a * b
            return mul(a,b)
        case '/':
            div = lambda a,b: a / b
            return div(a,b)
        
print(f"Evaluation: {eval(input1,input2,input3)}")



    



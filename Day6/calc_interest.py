def simple_int(p,t,r):
    return (p*t*r)/100


def compound_int(p,r,t):
    return p*((1+r/100)**t - 1)
     

principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = int(input("Enter time: "))

diff = compound_int(principal,rate,time) - simple_int(principal,rate,time)

print(f"Compund interest is: {compound_int(principal,rate,time):.2f}")
print(f"Simple interest is: {simple_int(principal,rate,time):.2f}")
print(f"Difference between ci and si : {diff:.2f}")
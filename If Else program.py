print("Program to Simple Interest")
p=eval(input("Principal Amount"))
r=eval(input("Rate of interest"))
t=eval(input("Time period"))

if(r==0):
    print("Simple Interest is zero")
else:
    si=(p*r*t)/100
    print(si)




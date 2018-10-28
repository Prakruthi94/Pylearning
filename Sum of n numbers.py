n=eval(input("Last number"))
if(not isinstance(n,int)):
    print("Wrong input")
else:
    if(n>0):
        sum=(n*(n+1))/2
        print("sum of natural numbers is",sum)
    else:
        print("Error!!")







n=eval(input("Enter any number"))
t=(5,7,9)
if(not isinstance(n,int)):
    print("Incorrect input")
else:
    if(n%t[0]==0 or n%t[1]==0 or n%t[2]==0):
        print("The given number is a multiple ")
    else:
        print("The given number is not a multiple")

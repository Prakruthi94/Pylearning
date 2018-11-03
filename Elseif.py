n=eval(input("Enter any number"))
t=(5,7,9)
if(not isinstance(n,int)):
    print("Incorrect input")
else:
    if(n%t[0]==0 or n%t[1]==0 or n%t[2]==0):
        print("The given number is a multiple ")
    elif(n%t[0]>60 or n%t[1]>60 or n%t[2]>60):
        print("error")
    else:
        print("The given number is not a multiple")

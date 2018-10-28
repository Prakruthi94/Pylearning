n=eval(input("Enter the number you want to check"))
if(not isinstance(n,int)):
    print("Error!!")
else:
    if(n%7==0):
        print("Number is a multiple of 7")
    else:
        print("Number is not a mulptiple of 7")


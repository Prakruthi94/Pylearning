num=eval(input("Enter the number"))
if(isinstance(num,int)):
    for i in range(0,num,2):
        if(i%2==0 and not i%3==0):
            print(i)



for i in range(0,num,2):
    for j in range(1,num,2):
        print(i,j)


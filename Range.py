#print(list(range(0,10)))
#list is the format that has to be entered in python 3.x
#variants of range:
#range(ele) - prints till ele-1
#range(start number, end number) - primts start number till end number-1
#range(start number, end number, incrementor)
#range takes only integer input

num=eval(input("Enter the number"))
if(isinstance(num,int)):
    l1=list(range(0,num,2))
    print(l1)
    print(sum(l1))



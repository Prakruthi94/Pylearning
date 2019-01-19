def main():
    n1=eval(input("Enter the number"))
    l1=[]
    while(n1!=0):
        n1=n1-1
        n2=eval(input("Enter the number to add"))
        if isinstance (n2,int):
         l1.append(n2)
    total=sum(l1)
    print(total)

main()

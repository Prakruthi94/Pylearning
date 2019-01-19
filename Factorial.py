def main():
    n1=eval(input("Enter the number for which you want to find the factorial?"))
    fact=1
    for i in range (1,n1+1):
        fact=fact*i
    print(fact)

main()





def push(mylist):
    ele= eval(input("Enter your element to be pushed to the stack"))
    mylist.append(ele)
    return mylist

def pop(mylist):
    if len(mylist)>0:
        mylist.pop()
        return mylist
    else:
        print("Stack is empty")

def display(mylist):
    return mylist

def main():
    mylist=[]
    while (True):

        print("1.Push")
        print("2.Pop")
        print("3.Display")
        print("4.Exit")

        Option = eval(input("Enter your option"))

        if(Option==1):
            mylist=push(mylist)
            print("The element of stack is",mylist)
        elif(Option==2):
            mylist=pop(mylist)
            print("The element of stack is",mylist)
        elif(Option==3):
            print("The element of stack is", mylist)
        elif(Option==4):
            exit()

main()


















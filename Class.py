class mystack():
    def __init__(self,stack_name,max_ele=5):
        self.l1=[]
        self.max_ele=max_ele
        self.stack_name = stack_name

    def print_attrib(self):
        print("The list is", self.l1)
        print("The list is", self.max_ele)

    def push(self):
        if(len(self.l1) < self.max_ele):
            self.l1=eval(input("Enter the element to add to stack"))
        else:
            print("Stack is full!!")

    def pop(self):
        if(len(self.l1)>0):
            self.l1.pop()
        else:
            print("Stack is empty!!")

    def display(self):
        if(len(self.l1)>0):
            print(self.l1)
        else:
            print("Stack is empty!!!")

    def main():
        max_ele=eval(input("Enter the max element for stack1"))
        while(True):
            stack_name = "stack1"
            s1=mystack(stack_name,max_ele)
            print("Options for",stack_name)
            print("1.Push")
            print("2.Pop")
            print("3.Dispaly")
            print("4.Exit")
            options=eval(input("Enter your choice"))
            if(options==1):
                s1.push()
            elif(options==2):
                s1.pop()
            elif(options==3):
                s1.display()
            elif(options==4):
                return
            else:
                print("Wrong choice")

     main()
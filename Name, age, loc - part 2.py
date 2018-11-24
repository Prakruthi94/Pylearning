def print_personal_details(name,age,loc):
    print("My name is",name)
    print("My age is",age)
    print("My location is",loc)
    return None

def main():
    name=eval(input("Enter the name"))

    if(name=="Prakruthi"):
        print("My age is 8")
        print("My loc is BTM")
    else:
       age=eval(input("Enter the age"))
       loc=eval(input("Enter the location"))
       print_personal_details(name,age,loc)
main()


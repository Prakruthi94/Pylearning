#def print_personal_details(name,age,loc):
 #   print("My name is",name)
  #  print("My age is",age)
   # print("My location is",loc)
    #return None

def print_personal_details(*args):
    print("My name is",args[0])
    print("My age is",args[1])
    print("My location is",args[2])
    return None

def main():
    name=eval(input("Enter the name"))
    age=eval(input("Enter the age"))
    loc=eval(input("Enter the location"))

    print_personal_details(name,age,loc)

main()
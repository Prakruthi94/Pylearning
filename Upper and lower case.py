def get_upper_list(strl):
    l1=[]
    for idx in strl:
        if idx.isupper():
            l1.append(idx)
    return l1

def get_lower_list(strl):
    l1=[]
    for idx in strl:
        if idx.islower():
            l1.append(idx)
    return l1

def main():
    strl=eval(input("Enter the string to scan"))
    print("Enter '1' to scan upper case letters")
    print("Enter '2' to scan lower case letters")
    print("Enter '3' to scan upper/lower case letter")
    choice=eval(input("Enter your choice"))
    if(choice==1):
        upper_list = get_upper_list(strl)
        print(upper_list)
    elif(choice==2):
        lower_list = get_lower_list(strl)
        print(lower_list)
    else:
        upper_list = get_upper_list(strl)
        lower_list = get_lower_list(strl)
        print(upper_list)
        print(lower_list)
main()

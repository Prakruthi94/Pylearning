def swap(ele1,ele2):
    ele1,ele2=ele2,ele1
    return ele1,ele2

def main():
    ele1=eval(input("Enter the element1 to swap"))
    ele2=eval(input("Enter the element2to swap"))
    print("After swap",swap(ele1,ele2))

main()

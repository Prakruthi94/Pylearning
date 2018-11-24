def my_print(*args):
    str1=""
    for ele in args:
        str1=str1+''+str(ele)
    print(str1)
my_print(1, "Python", 3.14)
print(1,"Python",3.14)


def menu():
    print("*"*10+"\t Welcome to calculator\t"+"*"*10+'\n')
    while True:
        print("1. add the number")
        print("2. subtract the number")
        print("3. multipy the number")
        print("4. divide the number")
        print("5. to exit\n")

        choice= int(input("enter the 1 to add \ 2 to subtract \ 3 to multiply \ 4 to divide\ to exit\t "))
        if choice<=4:
            n1=int(input("Enter the number\t"))
            n2=int(input("Enter the number\t"))
        if choice ==1:
            print(f" result is: {add_num(n1,n2)}")
        elif choice==2:
            print(f" result is : {sub_num(n1,n2)}")
        elif choice==3:
            print(f"result is: {mul_num(n1,n2)}")
        elif choice==4:
            print(f"result is: {div_num(n1,n2)}")
        elif choice==5:
            break
def add_num(n1,n2):
    return n1+n2
def sub_num(n1,n2):
    return n1-n2
def mul_num(n1,n2):
    return n1*n2
def div_num(n1,n2):
    try:
        return n1/n2
    except:
        return "enter the non zero number"

menu()

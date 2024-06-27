ch='y'
while(ch=='y' or ch=='Y'):
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    ch=int(input("Enter your choice :"))
    if(ch==1):
        a=int(input("Enter your first number :"))
        b=int(input("Enter your second number :"))
        c=a+b
        print("=======================================")
        print("Sum of  number is :",c)
        print("=======================================")
    elif(ch==2):
        el1=int(input("Enter your first element :"))
        el2=int(input("Enter your second element :"))
        sub=el1-el2
        print("---------------------------------------")
        print("Substraction of nuber is :",sub)
        print("---------------------------------------")
    elif(ch==3):
        n1=int(input("Enter your first number :"))
        n2=int(input("Enter your second number :"))
        mul=n1*n2
        print("**************************************")
        print("Multiplication of number is :",mul)
        print("**************************************")
    elif(ch==4):
        no1=int(input("Enter your first number :"))
        no2=int(input("Enter your second number :"))
        div=no1/no2
        print("......................................")
        print("Division of numberis :",div)
        print("......................................")
    elif(ch==5):
        break
    else:
        print("Thank You!,pls visit again")
    ch=input("Do you want to continue press y/n :")

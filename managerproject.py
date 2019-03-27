from classes import *;
arr=[];

n=-1;
m=-1;
while n!=4:
    print("1. create")
    print("2. Display")
    print("3. Raise Salary")
    print("4. Exit()");
    print("enter choice")
    n=int(input());
    if(n==1):
        while m!=4:
            print("1. Clerk")
            print("2. Programmer")
            print("3. Manager")
            print("4. Exit()");
            m=int(input());
            if(m==1):
                print("Enter name:")
                name=input();
                print("enter Age:");
                age=int(input());
                e1=Clerk(name,age);
                arr.append(e1);
            if(m==2):
                print("Enter name:")
                name=input();
                print("enter Age:");
                age=int(input());
                e1=Programmer(name,age);
                arr.append(e1);
            if(m==3):
                print("\nEnter name:")
                name=input();
                print("\nenter Age:");
                age=int(input());
                e1=Manager(name,age);
                arr.append(e1);
            if(m==4):
                break;
    elif(n==2):
        Employee.display();

    elif(n==4):
        print("\nTotal number of Employee :",Employee.count);
        break;
                      

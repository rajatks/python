def create():
       
    print("enter Id ")
    id1=int(input());
    print("Enter Name")
    name=input();
    print("Enter Age ")
    age=int(input());
    print("Enter salary")
    salary=int(input())
    print("enter Designation ")
    desig=input();
    file="\n"+id1+" "+name+" "+age+" "+salary+" "+desig
    f=open("db.txt","a")
    f.write(file)
    f.close();

def display():
        print("Enter 1 for Id Wise Display")
        print("enter 2 for whole display")
        m=int(input());
        f1=open("db.txt","r")
        if m ==1:
            print("Enter Id")
            p=int(input());
            f1.seek(0)
            d=f1.readlines();
            print(d[p-1])
            #print(f1[0])
        elif m==2:
            for data in f1:
                record=data.split(" ");
                print("\nId: ",record[0]);
                print("Name: ",record[1]);
                print("Age: ",record[2]);
                print("Salary: ",record[3]);
                print("Designation: ",record[4]);
            f1.close();

            

                

n=1
while n:
    print("1. create")
    print("2. Display")
    print("3. Raise Salary")
    print("4. Exit()");
    print("enter choice")
    n=int(input())
    if(n==1):
        create()
    elif(n==2):
        display()
    elif(n==4):
        print("exiting...")
        n=0

           

from projectexception import *;
class Employee:
    count=0;
    m=1;
    while m!=0:
        def __init__(self,salary,desig):
                try:
                    self.name=InputName("Enter Name : ");
                    self.age=InputAge("Enter Age : ");
                    self.salary=salary;
                    self.desig=desig;
                    Employee.count+=1;
                    file="\n"+self.name+" "+str(self.age)+" "+str(self.salary)+" "+self.desig
                    f=open("db.txt","a")
                    f.write(file)
                    f.close();
                except Exception as e:
                    print("Exception :",e);
                else:
                    m=0;
    def display():
        f1=open("db.txt","r")
        for data in f1:
                record=data.split(" ");
                print("\nName: ",record[0]);
                print("Age: ",record[1]);
                print("Salary: ",record[2]);
                print("Designation: ",record[3]);
        f1.close();

    

class Clerk(Employee):
    def __init__(self):
        super().__init__(8000,'clerk');

class Programmer(Employee):
    def __init__(self):
        super().__init__(25000,'programmer');

class Manager(Employee):
    def __init__(self):
        super().__init__(80000,'manager');
        
              
        

class Employee:
    count=0;
    def __init__(self,name,age,salary,desig):
        self.name=name;
        self.age=age;
        self.salary=salary;
        self.desig=desig;
        Employee.count+=1;
        file="\n"+self.name+" "+str(self.age)+" "+str(self.salary)+" "+self.desig
        f=open("db.txt","a")
        f.write(file)
        f.close();
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
    def __init__(self,name,age):
        super().__init__(name,age,8000,'clerk');

class Programmer(Employee):
    def __init__(self,name,age):
        super().__init__(name,age,25000,'programmer');

class Manager(Employee):
    def __init__(self,name,age):
        super().__init__(name,age,80000,'manager');
        
              
        

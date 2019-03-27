class emp:
    count=0;
    def __init__(self,name,age,salary,desig):
        self.name=name;
        self.age=age;
        self.salary=salary;
        self.desig=desig;
        emp.count+=1;  
    def display(self):
        print("\nName : ",self.name);
        print("Age : ",self.age);
        print("Salary : ",self.salary);
        print("Designazation : ",self.desig);
    def set_age(self,age):
        self.age=age;
    def __del__(self):
        print("\nobject with name: '%s'  getting destroy " %self.name);


e1=emp("rajat",21,50000,"developer");
e1.set_age(35);
e1.display();

e2=emp("gauri",23,50000,"developer");
e2.display();
del e1;
#e1.display();


print("\nthe total number of emploiyee :",emp.count);

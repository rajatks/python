class Emp:
    def __init__(self,name,age,state,city,pin):
        self.name=name;
        self.age=age;
        self.addr=Address(state,city,pin);
        self.computer=self.Computer("HP","FS0134","Pentim i5","2GHz","8GB");
    def display(self):
        print("name :",self.name);
        print("Age :",self.age);
        self.addr.display();
        self.computer.display();

    class Computer:
        def __init__(self,company,model,processor,speed,ram):
            self.company=company;
            self.model=model;
            self.processor=processor;
            self.speed=speed;
            self.ram=ram;
        def display(self):
            print("company :",self.company);
            print("Processor :",self.processor);
            print("Speed :",self.speed);
            print("Ram :",self.ram);
                

class Address:
    def __init__(self,state,city,pin):
        self.state=state;
        self.city=city;
        self.pin=pin;
    def display(self):
        print("State :",self.state);
        print("City : ",self.city);
        print("Pin : ",self.pin);

e1=Emp("Rajat",22,"Jhanrkhand","Ranchi",802301)
e1.display();

print("--------------------------");
print("-------------------------");
c1=Emp.Computer("DELL","TYF432","i7","1.8GHz","16GB");
c2=Emp.Computer("DELL","TYF432","i7","1.8GHz","16GB");
c1.display();
c2.display();
print(id(c1));
print(id(c2));

        

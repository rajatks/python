class Abc(Exception):
    def display(self):
        print("custom exception handle:");

a=5;
try:
    for i in range(10):
        print(i);
        #res=a/(a-i);
        if i==8:
            raise Exception;
        if i==3:
            raise Abc;

except ZeroDivisionError:
    print("Demonimator can't be zero");
except Abc as a:
    print("user defined handler");
    a.display();
except Exception as e:
    print("Default exception :",e);
else:
    print("Evry thing is fine");
finally:
    print("always excuted..");

print("program continued");




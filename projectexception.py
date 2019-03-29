def inputnum(str):
    while True:
        try:
            num=int(input(str));
            return num;
        except ValueError:
            print("enter in Range 20 to 60");
            
class AgeException(Exception):
    def display():
        print("Enter in range only 21 to 60 ");

class NameException(Exception):
    def display():
        print("Enter String only in range of 4 to 20 ");

def InputName(str):
    while True:
        name=input();
        val=len(name);
        if val<4 or val>30:
            raise NameException
        return name
    except NameException as a:
        a.display();
        
def InputAge(str):
    while True:
        num=int(input(str));
        if num<21 or num>60;
            raise AgeException
        return num
    except ValueError:
        print("please enter number only ");
    except AgeException as e:
        e.display();

    
        

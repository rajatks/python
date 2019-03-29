class Car:
    def move(self):
        print("car is moving ...");

class Bike:
    def move(self):
        print("Bike is Moving..");

class Bicycle:
    def move(self):
        print("Bycycle is moving..");

class Vechicle:
    def setVehicle(self,obj):
        obj.move();

v1=Vechicle();
v1.setVehicle(Bicycle());
v1.setVehicle(Car());
v1.setVehicle(Bike());

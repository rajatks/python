from threading import *;
import os;
from time import *;
class A(Thread):
    def run(self):
        for i in range(1,21):
            print("i : ",i);
            sleep(3);

class B(Thread):
    def run(self):
        for j in range(1,21):
            print("j : ",j);
            sleep(5);

class C(Thread):
    def run(self):
        for k in range(1,21):
            print("k : ",k);
            sleep(1);

a1=A();
b1=B();
c1=C();
#a1.setDaemon(True);
a1.start();
b1.start();
c1.start();
print(a1.is_alive());
print(b1.isDaemon());
c1.join();
print("Exit Program ..");

class A:
    def abc(self):
        print("HELLO");

class B(A):    #for single inherit A class 
    def xyz(self):
        print("Hi:");

class C(B,A):  #multi Level Inherit and MULTIPLE inheritance are allow ex class C(A,B)
    def atoz(self):
        print("Thanks...");

a1=A();
a1.abc();
b1=B();
b1.xyz();
b1.abc();

c1=C();
c1.abc();
c1.xyz();
c1.atoz();

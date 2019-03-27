class A:
    z=30;
    def __init__(self,x,y):
        self.x=x;
        self.y=y;
    def display(self):
        print("x :",self.x);
        print("y : ",self.y);

    @classmethod
    def abc(cls):
        print("from class method :: ",cls.z);

    @staticmethod
    def xyz(str):
        print("this is fro  static method ..: ",str);

a1=A(10,30);
a1.display();
A.abc();
A.xyz('hey babes');

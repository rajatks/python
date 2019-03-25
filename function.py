
print("hello:");

y=1;
def abc():
    x=1;
    print("x value: ",x);
    x+=1;

def xyz():
    global y;
    print("y value:",y);
    y+=1;

xyz();
xyz();
xyz();
xyz();
xyz();
xyz();
abc();
abc();
abc();
abc();
abc();


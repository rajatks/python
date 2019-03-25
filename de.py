#f1=open("abc.txt","r");
#print(f1.read());
#print(f1.readline(),end="");
#print(f1.readline(),end="");
#f1.seek(50);
#f1.close();

#f2=open('abc.txt','a')
#f2.write("hey ....gfnds")
#f2.append("howaaaa..");
#f2.close()

#f3=open("banking.jpg","rb");
#print(f3.read());

#f4=open("copy.jpg","wb");
#for data in f3:
 #   f4.write(data);

#f4.close();

f5=open("C:\\Users\\768949\\Desktop\\python\\abc.txt","r");
#f5.seek(20);
#print(f5.read());
print(f5.readlines()[2:3]);

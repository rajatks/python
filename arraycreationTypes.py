from numpy import *;

a=array([1,2,3.6,4,5,3],int);
print(a);
print(a.dtype);
print(type(a));

ls=linspace(1, 50, 5);
print(ls);

logs=logspace(1,50,5);
print(logs);

ar=arange(100,50,-2);
print(ar);

z1=zeros(4,int);
print(z1);
z=zeros(4,str);
print(z);

one=ones(5,bool);
print(one);

#r1=a.view();
ar1=a.copy();
a[0]=111;
print(a);
print(ar1);
print(id(a));
print(id(ar1));



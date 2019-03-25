>>> x=10;
>>> y=20;
>>> print(id(x));
1750194496
>>> print(id(y));
1750194656
>>> y=x;
>>> print(id(y));
1750194496
>>> from array import;
SyntaxError: invalid syntax
>>> from array import *
>>> a1=array('i',[11,43,55,66]);
>>> array.reverse(a1);
>>> for i in a1:
	print(i);

	
66
55
43
11
>>> print(type(a1));
<class 'array.array'>
>>> 
 from array import *
>>> a1=array('i',[11,43,55,66]);
>>> array.reverse(a1);
>>> for i in a1:
	print(i);

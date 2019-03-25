import time;
import calendar;
print(time.time());
ms=time.time();
print("Current Time",time.localtime(ms));
print("meaning  Time",time.asctime(time.localtime(ms)));
print(time.daylight);

print("-----------------------");

cal = calendar.month(2019, 5,5);
print(cal);

str="hello EveryBody";
print(str);
print(str.capitalize());
print(str.lower());
print(str.upper());
print(str.swapcase());
print(str.center(30,'-'));

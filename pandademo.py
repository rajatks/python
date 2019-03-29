import pandas as pd;

weather_data={
    'day':['1/3/2019','3/3/2019','4/3/2019','5/3/2019','6/3/2019','8/3/2019','11/3/2019','21/3/2019'],
    'temperature':[25,32,44,51,27,39,24,40],
    'windspeed':[4,8,6,8,3,5,6,5],
    'event':['sunny','raining','snow','spring','sunny','snow','sunny','winter']
    }


df=pd.DataFrame(weather_data);
print(df);

print(df.shape);
rows,columns=df.shape;
print(df.head());

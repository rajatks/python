import pandas as pd;

emp=pd.read_csv("employeeDetails.csv");
#print(df);
'''
print("min Age : ",emp['age'].idxmax());
print("Max Age : ",emp['age'].idxmin());


lar = list(emp['salary'].nlargest(2))
print("second Largest Salary : ",lar[1])

print("\n--------Cost Department Wise-------------")
dept = pd.DataFrame(emp.groupby('dept')['salary'].sum()).reset_index()
print(dept)
print("\n")
'''
print("\n--------Cost Project Wise-------------")
proj = pd.DataFrame(emp.groupby('Project Name')['Salary'].sum()).reset_index()
print(proj)
print("\n")


print("\n--------Employee Based on Project ID-------------")

project_id = dict(list(emp.groupby('Project Id')))

for key, value in project_id.items():
    print(key)
    print(value)
    print("\n")
'''
print("\n--------Employee Based on Manager-------------")
manager = dict(list(emp.groupby('manager')))

for key, value in manager.items():
    print(key)
    print(value)
    print("\n")


print("\n--------Mean Age Department Wise-------------")
age = pd.DataFrame(emp.groupby('dept')['age'].mean()).reset_index()
print(age)
print("\n")


'''



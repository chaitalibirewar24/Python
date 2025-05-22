#pandas

#que1=DataFrame=tabular format
'''
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],      #key=column name 
    'Age': [25, 30, 28],                        #value=column cell
    'Department': ['IT', 'HR', 'Finance']
}
df=pd.DataFrame(data)
print(df)
print("\ndataframe shape",df.shape)
'''

#que2=read_csv=read data and head=first 5 row
'''
file=open("employees.csv","w")
count=int(input("enter number of emp"))
file.write("name"+","+"age\n")
for i in range(0,count):
    name = input("Name: ")
    age = input("Age: ")
    file.write(name +","+ age+"\n")
file.close()

import pandas as pd
df=pd.read_csv("employees.csv")
print(df.head())
'''

#que3
'''
import pandas as pd
data={
    'student':['Jignesh', 'Emma', 'Mamta', 'Sunita'],
    'Math': [85, 79, 90, 88],
    'Science': [78, 85, 88, 92],
    'English': [92, 88, 76, 80]
}

df=pd.DataFrame(data)
print(df)

# print('Marks in maths>80:')
# print(df[df['Math']>80])
print(df[df["Math"]>80])
# print('Marks in maths and science>80:')
# print(df[(df['Math']>80) & (df['Science']>80)])
print(df["Math"])
'''
#que 4
'''
import pandas as pd
data={
    "product":["cake","burger","pizza"],
    "price":[400,70,500],
    "tax":[20,10,50]
}
df=pd.DataFrame(data)
#df['final price]=df['price']+(df['price]*df['tax])
df['Final Price']=df['price']+(df['price']*df['tax'])
print(df)
'''

#que 5
'''
import pandas as pd
data={
    "salesman":["A","B","C"],
    "region":[400,70,500],
    "sales":[20,10,50]
}
df=pd.DataFrame(data)
#sorted=df.sort_values(by='sales',ascending=False)
sorted=df.sort_values(by='sales',ascending=False)
print(sorted)

'''

#numpy

#que3
'''
import numpy as np
student=np.array([80,90,60,30])
print(student)
total=np.sum(student)
print("total marks:",total)
avg=np.average(student)
print("averqage marks:",avg)
maxi=np.max(student)
print("maximum marks:",maxi)
'''

#que 4
'''
import numpy as np
arr1=np.array(list(map(int,input("enter numbers").split())))
arr2=np.array(list(map(int,input("enter number").split())))
print(arr1)
print(arr2)

add=arr1 +arr2
print(add)
multi=arr1*arr2
print(multi)

n=int(input("enter number"))
print("arr1=",arr1*n)
print("arr2=",arr2*n)

sqrt1=np.sqrt(np.max(arr1))
print("arr1 sqrt",sqrt1)
'''
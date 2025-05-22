#que1
'''citizen={}
n=int(input("enter number of citizen"))
for i in range(n):
    name=input("enter name of citizen")
    age=int(input("enter the age of citizen"))
    citizen.update({name:age})
print(citizen)
eligible=dict(filter(lambda x: x[1]>18 ,citizen.items()))
print("eligible citizen for voting:",eligible)'''

#que2
'''
employee={}
def increment_funct(x):
    return x+(x*0.1)
n=int(input("enter number of employee"))
for i in range(n):
    desg=input("enter name of citizen")
    salary=int(input("enter the age of citizen"))
    employee.update({desg:salary})
print(employee)
increment=dict(map(lambda x:(x[1],increment_funct(x[1])),employee.items()))
print("salary after increment:",increment)
'''
'''
emp={"manager":3908309,"engineer":250000}
def increment(x):
    return (x+(x*0.1))
final_salary=dict(map(lambda x:(x[1],increment(x[1])),emp.items()))
print(final_salary)
'''



#que3
'''num=[]
n=int(input("enter number of numbers"))
for i in range(n):
    num.append(int(input("enter number")))
prime=list(filter(lambda x:x>1 and all(x%i!=0 for i in range(2,int(x/2+1))),num))
print("prime numbers:",prime)'''
num=[24,5,7,9]
prime=list(filter(lambda x: x>1 and all(x%i!=0 for i in range(2,int(x/2+1))),num ))
print(prime)

#que4
'''
states={"maha":9283  , "goa" : 83673788858}
# n=int(input("enter number of states"))
# for i in range(n):
#     state=input("enter name of state")
#     gdp=int(input("enter the gdp of states"))
#     states.update({state:gdp})
print(states)
compare=dict(filter((lambda x:x[1]>1000000),states.items()))
print(compare)
'''

#que5
'''
population={"india":2445857492,"china":58685394,"usa":48549}
sort=dict(filter((lambda x:x[1]>823384789),population.items()))
print(sort)
'''
#que6

#same as 1,4,5

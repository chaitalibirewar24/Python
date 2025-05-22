#que1
'''
n=int(input("enter a number"))
square=(lambda x: x*x)
print(square(n))
'''

#que2
'''
a=int(input("enter a number"))
b=int(input("enter a number"))
sum=(lambda x,y:x+y)(a,b)
print(sum)
'''

#que3
'''
n=2
check=(lambda x:"even" if x%2==0 else "odd")(n)
print(check)
'''

#que4
'''
even=[2,4,3,5]
check=list(filter((lambda x:x%2==0),even))
print(check)
'''

#que6
'''
list=[(2,3),(4,1),(4,8),(8,0)]
sort=sorted(list,key=lambda x:x[1])
#sort=sorted(list,key=lambda x:x[1])
print(sort)
'''
#que7
'''
max=lambda x,y,z:x if x>y and x>z else (y if y>z else z)
max=lambda x,y,z:x if x>y and x>z else(y if y>z else z)
print(max(20,10,4))
'''
#que9
'''
n=5
fact=lambda x:1 if x==0 else x*fact(x-1)
print(fact(n))
'''

#que10
'''
list=[{"name":"j","age":42},{"name":"k","age":4},{"name":"c","age":2}]
sort=sorted(list,key=lambda x:x["name"])
print(sort)
sort_age=sorted(list,key=lambda x:x["age"])
print(sort_age)
sort_both=sorted(list,key=lambda x:(x["age"],x["name"]))
print(sort_both)
'''

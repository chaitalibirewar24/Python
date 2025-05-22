#Explore

#file1=open("a.txt","a")
#string1=input("enter from user")
#file1.write(string1)
#print("enter content\n")
#content=file1.write("chaitali birewar is very talented and will make her parents very very proud\n ")
#file1.close()

'''file1=open("a.txt","r")
content=file1.read()
print(content)
file1.close()'''

#overwriting
'''
file1=open("a.txt","wt")
con=file1.write("what to do noww .. is it overwritted\n")
file1.close()
'''
#seek
'''
file1=open("a.txt","w")
content=file1.write("lets use seek now")
file1.seek(0)
content=file1.write("written in the start")
content=file1.write("lets use seek now")
file1.close()
'''

#que3
'''
file1=open("a.txt","w")
contend=file1.write("i am practicing assignment 11\nso what to do now i am tiredd with the dailyb routine\ni want someee excitement\n")
#file1.seek(0)
file1.close()
file1=open("a.txt","r")
data=file1.read()
print(data)
print(file1.mode)
size=int(input("enter size\n"))
print(file1.read(size))
file.close()
'''

#que 4
'''
source=input("enter source file name\n")
target=input("enter target name\n")
bytes_t0_copy=int(input("enter bytes\n"))
src=open(source,"rb")
trg=open(target,"ab")
data=src.read()
trg.write(data)
trg.close()
src.close()
'''

#que5
'''
file1=open("two.txt","w")
count=int(input("enter number of emp"))
for i in range(0,count):
    employee=(input(f"enter name of emp{i+1}"))
    file1.write(employee +"\t")
file1.close()
'''

#que7
'''
file=open("file1.csv","w")
count=int(input("enter number of emp"))
file.write("name\t\tage\t")
for i in range(0,count):
    name = input("Name: ")
    age = input("Age: ")
    file.write(name +"\t\t"+ age+"\n")
file.close()
'''

#que 8
'''
file=open("file1.csv","r")
contend=file.read()
print(contend)
file.close()
'''

#que 9
'''
import csv
filename="file9.csv"
with open(filename,"w",newline="") as file:
    doctor=[]
    #file.write("ndocid\t\tdocname\t\tquali\t\tspeci")
    writer=csv.writer(file)
    writer.writerow(["docid","docname","quali","speci"])
    for i in range(0,2):
        docid=int(input("enter doc id"))
        docname=input("enter doc name")
        quali=input("enter doc quali")
        speci=input("enter doc special")
        writer.writerow([docid,docname,quali,speci])
print(f"\nData successfully written to {filename}")
'''

#que 10
'''
import csv
filename="file9.csv"
with open(filename,"a",newline="") as file:
    writer=csv.writer(file)
    for i in range(0,2):
        docid=int(input("enter doc id"))
        docname=input("enter doc name")
        quali=input("enter doc quali")
        speci=input("enter doc special")
        writer.writerow([docid,docname,quali,speci])
'''

#corrected que4 assign 11
'''
import os
src=input("enter file name")
tgt=input("enter file name")

if not os.path.exists(src):
    print(f"{src} does not exit")
    exit()
 
if not os.path.exists(tgt):
    print(f"{tgt} does not exit")
    exit()

if not os.access(src,os.R_OK):
    print(f"{src} is not readable")
    exit()

if not os.access(tgt,os.W_OK):
    print(f"{tgt} is not writeable")
    exit()
num_bytes = int(input("Enter number of bytes to copy: "))
with open(src,"r") as sorce ,open(tgt,"w") as target:
    data=sorce.read(num_bytes)
    target.write(data)
    print(f"Copied {len(data)} bytes from '{sorce}' to '{target}'.")
sorce.close()
target.close()
'''
#que 9 again
'''
import csv
filename="file9.csv"
with open(filename,"w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["docid,docname"])
    for i in range(0,2):
        docid=int(input("enter id"))
        docname=input("enter name")
        writer.writerow([docid,docname])
    
print(f"\nData successfully written to {filename}")

'''
#corrected que 7 assign 11

import csv
filename="file7.csv"
with open(filename,"w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["name","age"])
    for i in range(0,2):
        docid=int(input("enter age"))
        docname=input("enter name")
        writer.writerow([docid,docname])
print(f"data successfully writen")
    



#que4

import psycopg2

#connect pgsql
connobj=psycopg2.connect(host='localhost',port='5432',database='postgres',user='postgres',password='root123')

#create cursor
curobj=connobj.cursor()
curobj.execute('''CREATE SEQUENCE company_id_seq START 1;''')

#create
comcreate='create table company(id int,comname varchar(50),empno int,comtype varchar(20));'
curobj.execute(comcreate)
connobj.commit()

#insert
count=int(input("enter number of records:"))
for i in range(0,count):
    id=int(input("enter id"))
    comname=input("enter name")
    empno=int(input("enter number of emp"))
    comtype=input("enter typen of company")
    cominsert='insert into company(id,comname,empno,comtype) values(%s ,%s, %s, %s);'
    curobj.commit(cominsert,(id,comname,empno,comtype))
connobj.commit()

#select
comdisplay='select * from company;'
curobj.execute(comdisplay)
datatable=curobj.fetchall()
connobj.commit()

#update
number=int(input("enter number of employee"))
comupdate='''update company set empno=%s where comname="blue";'''
curobj.execute(comupdate,(number))
connobj.commit()

# countquery
comcount='''select count(*) from company where empno>50;'''
curobj.execute(comcount)
count_result = curobj.fetchone()
connobj.commit()

#delete
comdelete='''delete from company where comtype='service type';'''
curobj.execute(comdelete)
connobj.commit()

curobj.close()
connobj.close()
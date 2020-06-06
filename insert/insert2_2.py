import mysql.connector
import random as rd

mydb = mysql.connector.connect(
  host="localhost",
  user="kafka",
  passwd="kafkauser@123",
  database="customer"
)

nation=['IND','AME','CHI','PAK','BRI','JAP','NET','ICE','CAN','ITL','AUS']
posts=['Developer', 'Tester', 'Web', 'Testing', 'HR', 'ProductManager', 'Analyst', 'Junior Analyst', 'Data Scientist', 'Big Data Developer', 'Java Developer', 'Python Developer', 'DataHandler']
typ=['SAV','CUR']

person=['PhnNo','Address','Nationality']
commercial=['JobDesc','Salary']
bank=['AccTyp','AccPasswd','Balance','LastTransDt','LastDebitBal','LastCreditBal']

n=input("Enter number of insertion :")
x=int(input("Enter highest number of customers :"))
for i in range(int(n)):
    sql1=''
    sql2=''
    sql3=''
    c=person[rd.randrange(0,len(person))]
    if(c=='PhnNo'):
        sql1="update cust set "+c+"="+str(rd.randrange(10000000, 999999999,3))+" where CustId="+str(rd.randrange(1,x))+";"
    elif(c=='Nationality'):
        sql1="update cust set "+c+"='"+nation[rd.randrange(0,len(nation))]+"' where CustId="+str(rd.randrange(1,x))+";"
    else:
        sql1="update cust set "+c+"='YYY' where CustId="+str(rd.randrange(1,x))+";"

    print(sql1)
    c=commercial[rd.randrange(0,len(commercial))]
    if(c=='JobDesc'):
        sql2="update cust set "+c+"='"+posts[rd.randrange(0,len(posts))]+"' where CustId="+str(rd.randrange(1,x))+";"
    elif(c=='Salary'):
        sql2="update cust set "+c+"="+str(rd.randrange(10000, 90000,3))+" where CustId="+str(rd.randrange(1,x))+";"

    print(sql2)
    c=bank[rd.randrange(0,len(bank))]
    if(c=='AccTyp'):
        sql3="update cust set "+c+"='"+typ[rd.randrange(0,len(typ))]+"' where CustId="+str(rd.randrange(1,x))+";"
    elif(c=='AccPasswd'):
        sql3="update cust set "+c+"='MMMM' where CustId="+str(rd.randrange(1,x))+";"
    elif(c=='Balance'):
        sql3="update cust set "+c+"="+str(rd.randrange(100000, 9999999,3))+" where CustId="+str(rd.randrange(1,x))+";"
    elif(c=='LastTransDt'):
        sql3="update cust set "+c+"='"+str(rd.randrange(1980,2012,4))+'-'+str(rd.randrange(1,12,2))+'-'+str(rd.randrange(1,29,4))+"' where CustId="+str(rd.randrange(1,x))+";"
    elif(c=='LastDebitBal'):
        sql3="update cust set "+c+"="+str(rd.randrange(10000, 90000,3))+" where CustId="+str(rd.randrange(1,x))+";"
    elif(c=='LastCreditBal'):
        sql3="update cust set "+c+"="+str(rd.randrange(10000, 90000,3))+" where CustId="+str(rd.randrange(1,x))+";"
    
    print(sql3)
    mycursor.execute(sql, val)
    mydb.commit()
 

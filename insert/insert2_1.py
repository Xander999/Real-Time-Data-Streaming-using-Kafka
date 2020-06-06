import mysql.connector
import random as rd

mydb = mysql.connector.connect(
  host="localhost",
  user="kafka",
  passwd="kafkauser@123",
  database="customer"
)
fnames=['Suraj', 'Arkaprabha', 'Agniva', 'Alimpan', 'Debjit', 'Ned', 'Ted', 'Barney', 'Marshall', 'Damian']
mnames=['Kumar','','Mishra','Hopkins','Modak','Joy','Khaa','Binsil']
lnames=['Saha','Shaji','Prabhakaran','Giri','Mukherjee','Prabhakar','Nath','Bansal','Agarwal','Mishra','Wayne']
gen=['Mal','FeM','Oth']
nation=['IND','AME','CHI','PAK','BRI','JAP','NET','ICE','CAN','ITL','AUS']
posts=['Developer', 'Tester', 'Web', 'Testing', 'HR', 'ProductManager', 'Analyst', 'Junior Analyst', 'Data Scientist', 'Big Data Developer', 'Java Developer', 'Python Developer', 'DataHandler']
curr=['DOL','TAK','PAI','YEN','POU']
typ=['SAV','CUR']
des=['Trans was success.','Trans was fail']
f=['D','C']
mycursor = mydb.cursor()
n=input("Enter number of insertion :")
for i in range(n):
    CustFName=fnames[rd.randrange(0,len(fnames))]
    CustMName=mnames[rd.randrange(0,len(mnames))]
    CustLname=lnames[rd.randrange(0,len(lnames))]
    DOB=str(rd.randrange(1980,2012,4))+'-'+str(rd.randrange(1,12,2))+'-'+str(rd.randrange(1,29,4))
    PhnNo=rd.randrange(10000000, 999999999,3)
    Address='XXX'
    Gender=gen[rd.ramdrange(0,len(gen))]
    Nationality=nation[rd.randrange(0,len(nation)]
    JobDesc=posts[rd.randrange(0,len(posts))]
    Salary=rd.randrange(10000, 90000,3)
    AccId='S'+str(rd.randrange(1000,9999,4))
    AccTyp=typ[rd.randrange(0,len(typ))]
    AccPasswd='ftkddfzhsh'
    DebitCardNo=str(rd.randrange(100000000000000,999999999999999,8))
    CreditCardNo=str(rd.randrange(100000000000000,999999999999999,8))
    Balance=rd.randrange(100000, 9999999,3)
    LastTransDt=str(rd.randrange(1980,2012,4))+'-'+str(rd.randrange(1,12,2))+'-'+str(rd.randrange(1,29,4))
    LastDebitBal=rd.randrange(10000, 90000,3)
    LastCreditBal=rd.randrange(10000, 90000,3)
    sql = "insert into cust (CustFName, CustMName, CustLname, DOB, PhnNo, Address, Gender, Nationality, JobDesc, Salary, AccId, AccTyp, AccPasswd, DebitCardNo, CreditCardNo, Balance, LastTransDt, LastDebitBal, LastCreditBal) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    val = (CustFName, CustMName, CustLname, DOB, PhnNo, Address, Gender, Nationality, JobDesc, Salary, AccId, AccTyp, AccPasswd, DebitCardNo, CreditCardNo, Balance, LastTransDt, LastDebitBal, LastCreditBal)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted :",i)

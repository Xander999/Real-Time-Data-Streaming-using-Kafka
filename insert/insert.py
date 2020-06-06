import mysql.connector
import random as rd

mydb = mysql.connector.connect(
  host="localhost",
  user="XANDER",
  passwd="xander21",
  database="exp"
)

mycursor = mydb.cursor()
names=['Suraj', 'Arkaprabha', 'Agniva', 'Alimpan', 'Debjit', 'Ned', 'Ted', 'Barney', 'Marshall', 'Damian']
posts=['Developer', 'Tester', 'Web', 'Testing', 'HR', 'ProductManager', 'Analyst', 'Junior Analyst', 'Data Scientist', 'Big Data Developer', 'Java Developer', 'Python Developer', 'DataHandler']
for i in range(12):
    name=names[rd.randrange(0,len(names))]
    sal=rd.randrange(10000, 90000,3)
    post=posts[rd.randrange(0,len(posts))]    
    sql = 'INSERT INTO employee (ename, esal, edep) VALUES (%s, %s, %s)'
    val = (name, sal, post)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted :",i)




 

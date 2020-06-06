import mysql.connector
import random as rd

mydb = mysql.connector.connect(
  host="localhost",
  user="XANDER",
  passwd="xander21",
  database="bank"
)
curr=['DOL','TAK','PAI','YEN','POU']
typ=['SAV','CUR']
des=['Trans was success.','Trans was fail']
f=['D','C']
mycursor = mydb.cursor()
for i in range(10):
    ServiceId=rd.randrange(10000, 90000,3)
    ChannelId= rd.randrange(10000, 90000,3)
    CreateDt='2019-01-05 03-14-07'
    EffectiveDt='2019-01-06 00-12-01'
    ATMId='ATM'+str(rd.randrange(10,99,3))
    TxnRefNo='TX'+str(rd.randrange(10,99,3))
    Reversal='S' 
    Currency= curr[rd.randrange(0,len(curr))]
    ReturnCode=rd.randrange(10000, 90000,3) 
    ChannelRefNo='CHN'+str(rd.randrange(10,99,3))
    AcctNo= 'AC'+str(rd.randrange(10,99,3))
    AccType= typ[rd.randrange(0,len(typ))]
    TransferAccNo= 'AC'+str(rd.randrange(10,99,3))
    CustomerId= 'CU'+str(rd.randrange(10,99,3))
    Amt=rd.randrange(10000, 90000,3)
    AvailBal= rd.randrange(10000, 90000,3)
    Description=des[rd.randrange(0,1)]
    TranStatus='Tran done.'
    BranchNo= rd.randrange(10000, 90000,3)
    DebitCreditFlag=f[rd.randrange(0,1)]
    sql = "insert into trans (ServiceId, ChannelId, CreateDt, EffectiveDt, ATMId, TxnRefNo, Reversal, Currency, ReturnCode, ChannelRefNo, AcctNo, AccType, TransferAccNo, CustomerId, Amt, AvailBal, Description, TranStatus, BranchNo, DebitCreditFlag) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (ServiceId, ChannelId, CreateDt, EffectiveDt, ATMId, TxnRefNo, Reversal, Currency, ReturnCode, ChannelRefNo, AcctNo, AccType, TransferAccNo, CustomerId, Amt, AvailBal, Description, TranStatus, BranchNo, DebitCreditFlag)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted :",i)

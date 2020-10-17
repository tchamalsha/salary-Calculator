import mysql.connector

def read_info():
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="tharushi",
  database="factory"
  )
  mycursor = mydb.cursor()
  sql_select="Select * from info"
  mycursor.execute(sql_select)
  records=mycursor.fetchall()
  for row in records:
     print("Employee ID: ",row[0])
     print("Employee Name: ",row[1])
     print("Employee Basic: ",row[2])
     print("Employee OT rate: ",row[3])
  

def read_data_entry():
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="tharushi",
  database="factory"
  )
  mycursor = mydb.cursor()
  sql_select="Select * from data_entry"
  mycursor.execute(sql_select)
  records=mycursor.fetchall()
  for row in records:
     print("Employee ID: ",row[0])
     print("Employee no pay: ",row[1])
     print("Employee Attendance Bonus: ",row[2])
     print("Employee OT hours: ",row[3])
     print("Employee sundays: ",row[4])
     
def insert(emp_id, NO_pay, AT_BONUS, OT, SUNDAYS):
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="tharushi",
  database="factory"
  )
  mycursor = mydb.cursor()

  sql = "INSERT INTO data_entry (emp_id, NO_pay, AT_BONUS, OT, SUNDAYS) VALUES (%s, %s, %s, %s, %s)"
  val=(emp_id, NO_pay, AT_BONUS, OT, SUNDAYS)


  mycursor.execute(sql,val)
  mydb.commit()

  print(mycursor.rowcount, "record inserted.")


##
##for x in range(3):
##  emp_id=int(input("Enter the id number: "))
##  NO_pay=int(input("Number of nopay days: "))
##  AT_BONUS=int(input("Attendance bonus: "))
##  OT=int(input("Number of OT hours: "))
##  SUNDAYS=int(input("Number of sundays: "))
##  insert(emp_id, NO_pay, AT_BONUS, OT, SUNDAYS)

print("Empoyees Information")
read_info()
print("Entered data")
read_data_entry()

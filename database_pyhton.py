import mysql.connector
def Creating_a_Database():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE mydatabase")

def Check_if_Database_Exists():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="")
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")   
    for x in mycursor:
        print(x)
def Creating_a_Table():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="mydatabase")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE customers3 (name VARCHAR(255), address VARCHAR(255))")    

def Check_if_Table_Exists():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="mydatabase")
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)

def Insert_Into_Table():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="mydatabase")
    mycursor = mydb.cursor()
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def Insert_Multiple_Rows():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="mydatabase")
    mycursor = mydb.cursor()
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = [('Peter', 'Lowstreet 4'),
             ('Amy', 'Apple st 652'),
             ('Hannah', 'Mountain 21'),
             ('Michael', 'Valley 345'),
             ('Sandy', 'Ocean blvd 2'),
             ('Betty', 'Green Grass 1'),
             ('Richard', 'Sky st 331'),
             ('Susan', 'One way 98'),
             ('Vicky', 'Yellow Garden 2'),
             ('Ben', 'Park Lane 38'),
             ('William', 'Central st 954'),
             ('Chuck', 'Main Road 989'),
             ('Viola', 'Sideway 1633')]
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record was inserted.")

def Get_Inserted_ID():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="mydatabase")
    mycursor = mydb.cursor()
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("Michelle", "Blue Village")
    mycursor.execute(sql, val)
    mydb.commit()
    print("1 record inserted, ID:", mycursor.lastrowid)
def Select_From_a_Table():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="mydatabase")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
        
def Using_the_fetchone_Method():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="mydatabase")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchone()
    print(myresult)
    myresult = mycursor.fetchone()
    print(myresult)
    myresult = mycursor.fetchone()
    print(myresult)

def Delete_Record_and_Prevent_SQL_Injection():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="mydatabase")
    mycursor = mydb.cursor()
    sql = "DELETE FROM customers WHERE address = %s"
    adr = ("Yellow Garden 2", )
    mycursor.execute(sql, adr)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
def Update_Table_and_Prevent_SQL_Injection():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="mydatabase")
    mycursor = mydb.cursor()
    sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    


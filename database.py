# https://dev.mysql.com/downloads/windows/installer - mysql download
# pip install mysql-connector
# pip install mysql-connector-python
# pip install mysql-connector-python-rf


import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='parolingiz',
    # databaseni korsatmasa umumiy mysql ni korsatadi
    database="Store"
)

mycursor = mydb.cursor()

# BAZADA NIMADIR OZGARSA commit()


# # baza yaratish
# mycursor.execute("CREATE DATABASE IF NOT EXISTS Store")

# # bazalarni korish
# mycursor.execute("SHOW DATABASES")
# # print(mycursor)
# for x in mycursor:
#   print(x)



# # table yaratish
# mycursor.execute("CREATE TABLE IF NOT EXISTS customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# # mavjud tablega column qoshish
# mycursor.execute("ALTER TABLE customers ADD COLUMN old INT")

# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)



# # malumot yozish
# sql = "INSERT INTO customers (name, address, old) VALUES (%s, %s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4', 11),
#   ('Amy', 'Apple st 652', 12),
#   ('Hannah', 'Mountain 21', 16),
#   ('Michael', 'Valley 345', 11),
#   ('Sandy', 'Ocean blvd 2', 11),
#   ('Betty', 'Green Grass 1', 13),
#   ('Richard', 'Sky st 331', 10)
# ]
#
# val2 = ("Michelle", "Blue Village", 32)
#
# # tablega qoshish (execute - bir dona bolsa)
# # mycursor.executemany(sql, val)
# mycursor.execute(sql,val2)
#
# # tableni yangilash(commit-topshirmoq)
# mydb.commit()
#
# # rowcount va boshqa tayyor metodlar
# # print(mycursor.rowcount, "record inserted.")
# print("1 record inserted, ID: ",mycursor.lastrowid)



# SELECT
# mycursor.execute("SELECT * FROM customers")
# mycursor.execute("SELECT name, address FROM customers")
# myresult = mycursor.fetchall()
#
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchone()
# print(myresult)




# # Where
# sql = "SELECT * FROM customers WHERE address ='Highway 21'"
# LIKE - tarkibida bolsin
# sql = "SELECT * FROM customers WHERE address LIKE '%st%'"
# mycursor.execute(sql)

# # ozgaruvchi berish
# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Mountain 21", )
#
# mycursor.execute(sql, adr)
# myresult = mycursor.fetchall()
# print(myresult)



# ORDER BY - ... boyicha sarala
# sql = "SELECT * FROM customers ORDER BY old"
# Teskari
# sql = "SELECT * FROM customers ORDER BY old DESC"

# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)



# DELETE
# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
# mycursor.execute(sql)
# OZGARUVCHILI
# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
#
# mycursor.execute(sql, adr)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")



# DROP
# sql = "DROP TABLE IF EXISTS customers"
# mycursor.execute(sql)



#UPDATE
# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
# mycursor.execute(sql)

# OZGARUVCHIDA
# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")
#
# mycursor.execute(sql, val)
#
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")



# LIMIT - jadvalidagi 5 ta birinchi yozuvni tanlang:
# mycursor.execute("SELECT * FROM customers LIMIT 5")

# 3-pozitsiyadan boshlang va 5 ta yozuvni qaytaring:
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
#
# myresult = mycursor.fetchall()
# print(myresult)



# JOIN - Ikki yoki undan ortiq jadvallar qatorlarini JOIN iborasidan foydalanib, ular orasidagi tegishli ustun asosida birlashtirishingiz mumkin.
# sql = f"SELECT \
#   customers.name, \
#   products.name \
#   FROM customers \
#   INNER JOIN products ON customers.id = products.id+1"

# sql = "SELECT \
#   customers.name AS user, \
#   products.name AS id \
#   FROM customers \
#   INNER JOIN products ON customers.id = products.id"

# sql = "SELECT \
#   customers.name AS user, \
#   products.name AS id \
#   FROM customers \
#   RIGHT JOIN products ON customers.id = products.id"

# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# print(myresult)



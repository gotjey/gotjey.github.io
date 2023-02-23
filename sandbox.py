import mysql.connector

mydb = mysql.connector.connect(
  host="bmk0xxjd8bweo7cysbxc-mysql.services.clever-cloud.com",
  user="bmk0xxjd8bweo7cysbxc",
  password="9yZpIGSea39lbHQEtdzF",
  database="zhevla"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), password VARCHAR(255))")
mydb.commit()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

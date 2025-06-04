import mysql.connector

connect = mysql.connector.connect(
    user='root',
    password='rootroot',
    host='localhost'
)

cursors = connect.cursor()

sql = "create database if not exists test_beijing"

cursors.execute(sql)
print(sql)

sql = "select * from users where uname is zhsan"

print(sql)

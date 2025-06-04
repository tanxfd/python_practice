import mysql.connector
from User import User

connect = mysql.connector.connect(
    user='root',
    password='rootroot',
    database='bank_account'
)

cursor = connect.cursor()

sql = "CREATE TABLE IF NOT EXISTS account(\
id int PRIMARY KEY,\
client_degree INT,\
name CHAR NOT NULL,\
pass INT,\
locate CHAR,\
card_money FLOAT,\
credit_bank CHAR,\
max_exchange INT\
)"

cursor.execute(sql)



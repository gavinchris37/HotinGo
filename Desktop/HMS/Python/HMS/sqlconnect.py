import mysql.connector

# ===================SQL Connectivity=================

# SQL Connection
connection=mysql.connector.connect(host="remotemysql.com", 
                            user="OupAGhC9dM", 
                            password="KYVO7iezPw", 
                            database = "OupAGhC9dM", 
                            port="3306", autocommit=True)

cursor=connection.cursor()

# SQL functions

def checkUser(username, password=None):
    cmd="Select count(username) from login where username='"+username.lower()+(("' and BINARY password='"+password) if password is not None else "")+"';"
    cursor.execute(cmd)
    print(cmd)
    cmd=None
    return cursor.fetchone()[0]>=1

def addUser(username, password, sec_que, sec_ans):
    cmd=f"Insert into login (username, password, sec_que, sec_ans) values ('{username}', '{password}', '{sec_que}', '{sec_ans}');"
    cursor.execute(cmd)
    cmd=f"select count(name) from login where username='{username}' and password='{password}' and sec_que='{sec_que}' and sec_ans='{sec_ans}'"
    cursor.execute(cmd)
    cmd=None
    return cursor.fetchone()[0]>=1

def availableRooms():
    cursor.execute("select count(room_id) from rooms where currently_booked='0';")
    return cursor.fetchone()[0]

print(availableRooms())
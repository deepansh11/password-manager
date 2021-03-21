import mysql.connector as msc
import getpass
import sys
from tabulate import tabulate
import hashing

username_db = "root" # input("Enter username:")
password_db = "pahwadeepansh11" # getpass.getpass("Enter password: ")

try:
    db = msc.connect(host="localhost",database="pwdmanager",user=username_db,password=password_db)
    print("Database ready to use")
    mycursor = db.cursor()
except msc.Error as e:
    print(e)

def view_data():
    mycursor.execute("SELECT * from manager")
    result=mycursor.fetchall()
    print(tabulate(result, headers=['Email', 'Password','Website','Username'], tablefmt='psql'))

def update_data(entry):
    website=input("Enter the website for which you want to change the username: ")
    update_user=input("Enter the username to update: ")
    mycursor.execute("INSERT into manager(username) VALUES(%s) WHERE website=%s",(update_user,website))
    mycursor.execute("SELECT * FROM manager")
    db.commit()

def insert_data():
    print("Please enter username,email,password,website in the respective order: ")
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")
    key=hashing.Hash(password).hashFunc() #need to fix the hashing function
    website = input("Website: ")
    print("If you have entered the correct information please enter y, if you think there is a mistake please enter n")
    x = input()
    if x == 'y':
        print("=========Inserting into the database=========")
        mycursor.execute("INSERT into manager(username,email,password,website) VALUES(%s,%s,%s,%s)",(username,email,key,website))
        db.commit()
        return True;
    elif x=='n':
        print("Returning back to the option menu")
        #Code to re-execute the insert command
        return insert_data()
    else:
        print("Not a valid response")
        sys.exit(1)

def reset_data():
    print("Work in progress")

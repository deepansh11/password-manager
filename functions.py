import mysql.connector as msc
import getpass
import sys
from tabulate import tabulate
import hashing
import pyperclip
import database_backup as backup

data=['username','password','email']

def connection():
    config = {
        "user": "root",
        "password": "<enter your database password>",
        "host": "localhost",
        "database": "pwdmanager"
    } #Please change your database values
    try:
        c = msc.connect(**config)
        return c
    except:
        print("connection error, make sure you have entered correct database values")
        exit(1)

db = connection()
mycursor = db.cursor()

def view_data():
    mycursor.execute("SELECT * from manager")
    result=mycursor.fetchall()
    print(tabulate(result, headers=['Email', 'Password','Website','Username'], tablefmt='psql'))

def update_data(entry,i):
    website=input(f"Enter the website for which you want to change the {data[i]}: ")
    update_query=input(f"Enter the new {data[i]} to update: ")
    mycursor.execute(f"UPDATE manager SET {data[i]} = '{update_query}' WHERE website='{website}'")
    db.commit()
    mycursor.execute("SELECT * FROM manager")
    result=mycursor.fetchall()
    print(tabulate(result, headers=['Email', 'Password','Website','Username'], tablefmt='psql'))

def insert_data():
    print("Please enter username,email,password,website in the respective order: ")
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")
    website = input("Website: ")
    print("If you have entered the correct information please enter y, if you think there is a mistake please enter n")
    x = input()
    if x == 'y':
        print("=========Inserting into the database=========")
        mycursor.execute("INSERT into manager(username,email,password,website) VALUES(%s,%s,%s,%s)",(username,email,key,website,))
        db.commit()
        return True
    elif x=='n':
        print("Returning back to the option menu")
        return insert_data()
    else:
        print("Not a valid response")
        sys.exit(1)

def reset_data():
    website=input("Enter the website for which you want to delete the data of: ")
    mycursor.execute(f"DELETE FROM manager WHERE website='{website}'")
    db.commit()
    print(f"Data for the website {website} deleted")

def reset_all_data():
    print("Please be careful to use this it will delete all the entries from the table")
    table_name=input("Insert the table name to delete: ")
    mycursor.execute(f"DELETE FROM {table_name}")
    db.commit()
    print(f"Data for {table_name} table deleted")

def copy_to_clipboard():
    try:
        website = input("Please enter the website whose password you want to use: ")
        mycursor.execute("SELECT password FROM manager WHERE website=%s",(website,))
        password = mycursor.fetchone()
        pyperclip.copy(password[0])
    except Exception as e:
        print(e)
        exit(1)

def write_file():
    backup_file = open("backup.sql",'w+')
    mycursor.execute("SELECT * FROM manager")
    result = mycursor.fetchall()
    table = tabulate(result, headers=['Email', 'Password','Website','Username'], tablefmt='psql')
    for row in table:
        backup_file.write(row)

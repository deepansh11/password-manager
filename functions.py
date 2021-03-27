import mysql.connector as msc
import getpass
import sys
from tabulate import tabulate
import hashing
import pyperclip

data=['username','password','email']

def connection():
    password = getpass.getpass("Please enter the password to access the database: ")
    config = {
        "user": "root",
        "password": password,
        "host": "localhost",
        "database": "pwdmanager"
    }
    try:
        c = msc.connect(**config)
        return c
    except:
        print("connection error")
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
    key=hashing.hashFunc(password)
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
    print("This will copy password to clipboard and also unhash the existing password to copy")

def backup_data(output_filename):
    print("Create and encrypt a backup file")

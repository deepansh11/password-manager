import argparse
import functions
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-u","--update",help="Update the password manager",choices=['username','password','email'],const='password',nargs='?')
parser.add_argument("-v","--view",help="View database",action="store_true")
parser.add_argument("-c","--copy-password",help="Copy password to clipboard",action="store_true") #need to add this functionality
parser.add_argument("-i","--insert",help="Insert entery into the database",action='store_true')
parser.add_argument("-a","--reset-all",help="Reset the database",action='store_true')
parser.add_argument("-r","--reset",help="Reset the database",action='store_true')
parser.add_argument("-b","--backup",help="Create an encrypted backup of the database",action='store_true') #need to work on this
args = parser.parse_args()

if args.view:
    functions.view_data()

elif args.insert:
    functions.insert_data()

elif args.update == 'username':
    functions.update_data(functions.data,0)

elif args.update == 'password':
    functions.update_data(functions.data,1)

elif args.update == 'email':
    functions.update_data(functions.data,2)

elif args.reset:
    functions.reset_data()

elif args.reset_all:
    functions.reset_all_data()

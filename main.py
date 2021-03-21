import argparse
import functions


parser = argparse.ArgumentParser()
parser.add_argument("-u","--update",help="Update the password manager",choices=['username','password','email'],const='password',nargs='?')
parser.add_argument("-v","--view",help="View database",action="store_true")
parser.add_argument("-i","--insert",help="Insert entery into the database",action='store_true')
parser.add_argument("-r","--reset",help="Reset the database",action='store_true')
args = parser.parse_args()


if args.view:
    functions.view_data()

elif args.insert:
    functions.insert_data()

elif args.update == 'username':
    functions.update_data(username)

elif args.update == 'password':
    functions.update_data(password)

elif args.update == 'email':
    functions.update_data(email)

elif args.reset == 'reset':
    functions.reset_data()

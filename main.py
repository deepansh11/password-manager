import argparse
import functions
import sys
from hashing import SECRET_KEY
import database_backup as backup

parser = argparse.ArgumentParser()
parser.add_argument("-u","--update",help="Update the password manager",choices=['username','password','email'],const='password',nargs='?')
parser.add_argument("-v","--view",help="View database",action="store_true")
parser.add_argument("-c","--copy-password",help="Copy password to clipboard",action="store_true")
parser.add_argument("-i","--insert",help="Insert entery into the database",action='store_true')
parser.add_argument("-a","--reset-all",help="Reset the a single column",action='store_true')
parser.add_argument("-r","--reset",help="Reset the whole password manager table",action='store_true')
parser.add_argument("-g", "--generate-key", dest="generate_key", action="store_true",help="Whether to generate a new key or use existing")
parser.add_argument("-e", "--encrypt", action="store_true",help="Whether to encrypt the file, only -e or -d can be specified.")
parser.add_argument("-d", "--decrypt", action="store_true",help="Whether to decrypt the file, only -e or -d can be specified.")
args = parser.parse_args()

secret = SECRET_KEY
passw = input('Please provide the master password to start using the password manager: ')
if passw == secret:
    file="backup.sql"
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

    elif args.copy_password:
        functions.copy_to_clipboard()

    elif args.generate_key:
        backup.write_key()

    elif args.encrypt and args.decrypt:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")
    elif args.encrypt:
        functions.write_file()
        backup.encrypt(file,backup.load_key())
    elif args.decrypt:
        backup.decrypt(file,backup.load_key())
    else:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")

else:
    print('no luck')
    exit()

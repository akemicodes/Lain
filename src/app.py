"""
File:			app.py
Project:		Lain
Date:			2/20/24
Author:			akemicodes
Description:
"""

from launcher import Launcher
from secret import Secret
from user import User
from entry import Entry
from data import Data
import os

def output_menu():
	print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
	print("1.	Add Entry")
	print("2.	View Entry")
	print("3.	Decrypt Entry")
	print("4.	Exit")
	print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

def get_input():
	user_input = int(input("Please enter an option 1-4: "))
	return user_input

# Main entry point of the program
def main():
	is_running = True
	launcher_instance = Launcher() 
	secret_instance = Secret()
	data_instance = Data()
	fields = list()


	while(is_running):
		output_menu()
		user_in = get_input()

		# Add in insance
		if(user_in == 1):
			user_input = input("Please enter the name of the application: ")
			hash_input = input("Please enter a phrase: ")
			password_input = input("Please enter your password: ")

			hash = secret_instance.generate_hash(hash_input)
			secret = secret_instance.generate_password(hash, password_input)
			entry_instance = Entry(user_input, secret)
			entry_instance.write_entry()
			data_instance.store_key(user_input, secret_instance.parse_secret(hash))
		
		elif(user_in == 2):
			data_instance.output_file()

		# Fetch your password
		elif(user_in == 3):
			field_input = input("Please type the application name: ")
			
			current_field = data_instance.fetch_field(field_input) # -> We want to fetch the field
			if(current_field):
				field = current_field
				key = data_instance.fetch_key(field) # -> We want to fetch the key that's created 
			
				secret = data_instance.fetch_secret(field)
				key = key.encode('utf-8')
				secret = secret.encode('utf-8')
			
				un_secret = secret_instance.parse_secret(secret_instance.decrypt_password(key, secret))
				print("Decrypted password: " + un_secret)
				
			
			else:
				print("Application data not found!")	
		
		elif(user_in == 4):
			print("Exiting... goodbye!")
			is_running = False
	
main()

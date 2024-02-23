"""
File:			data.py
Project:		Lain
Date:			02/23/24
Author:			akemi
Description:
"""
import os

class Data:
	def __init__(self):
		self.current_path = os.path.dirname(os.path.dirname(__file__))
		self.data_dir = os.path.join(self.current_path, "data\data.txt")
		self.key_dir = os.path.join(self.current_path,"keys\\")	

	def write_data(self, value):
		file = open(self.data_dir, "a")
		file.write(value)
		file.close

	def store_key(self, value, key):
		keyPath = "keys\\" + value + ".txt"
		path = os.path.join(self.current_path, keyPath)
		file = open(path, "a")
		file.write(key + "\n")
		file.close()

	def fetch_key(self, field):
		path = self.key_dir + field + ".txt"
		
		if(not os.path.isfile(path)):
			print("Error: Aplication data does not exist")

		else:
			file = open(path, 'r')
			value = file.read()
			return value

		return ""

	def fetch_secret(self, field):
		path  = os.path.join(self.current_path, self.data_dir)

		if(os.path.isfile(path)):
			with open(path, "r") as file:
				for line in file:
					if field in line:
						return line.split()[-1]
	
	
	def fetch_field(self, value):
		path = os.path.join(self.current_path, self.data_dir)	

		if(os.path.isfile(path)):
			with open(path, "r") as file:
				for line in file:
					if value in line:
						return line.strip().split()[0]
				
		return None
		
	def output_file(self):
		file = open(self.data_dir, 'r')

		for line in file:
			print(line)

		file.close()	
	

"""
File:           entry.py
Project:        Lain
Date:           02/23/24
Author:         akemi
Description:
"""
from data import Data

class Entry:
    def __init__(self, field, hash):
        self.field = field
        self.hash = hash
        self.data_instance = Data()
    
    def write_entry(self):
        self.data_instance.write_data(self.field + " " + self.hash.decode("utf-8") + "\n")
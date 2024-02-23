"""
File:			secret.py
Project:		Lain
Date:			2/23/24
Author:			akemi
Description:
"""

import hashlib
import secrets
import base64
import binascii
from cryptography.fernet import Fernet

class Secret:
	def __init__(self):
		self.salt = secrets.token_bytes(16)

	def generate_hash(self, secret):
		salted_secret = self.salt + secret.encode('utf-8') # -> Salt secret
		hashed_secret = hashlib.sha256(salted_secret).hexdigest() # ->  Hash secret using SHA-256
		temp_key = binascii.unhexlify(hashed_secret)
		key_value = base64.urlsafe_b64encode(temp_key)

		return key_value

	def generate_password(self, key, password):
		f = Fernet(key)
		bytes = password.encode('utf-8')
		token = f.encrypt(bytes)
		return token

	def decrypt_password(self, key, password):
		f = Fernet(key)
		token = f.decrypt(password)
		return token

	def parse_secret(self, value):
		return value.decode("utf-8")
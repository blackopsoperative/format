import random as r
import string as s

def uppercase(s:str):
	return s.upper()

def lowercase(s:str):
	return s.lower()

def reverse(s:str):
	return s[::-1]

def numbergen(size=12, chars=s.digits):
	return ''.join(r.choice(chars) for _ in range(size))

import secrets
from passlib.hash import argon2

salt = secrets.token_bytes(32)

def hashFunc(password):
	hash = argon2.using(salt= salt, rounds=8, memory_cost=2048, parallelism=2, type='id', max_threads=16, relaxed=False).hash(password)
	return hash

def unhashFunc():
	print("something")

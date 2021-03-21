import secrets
from passlib.hash import argon2

def hash_argon2(password):
	salt = secrets.token_bytes(32)
	hash = argon2.using(salt= salt, rounds=8, memory_cost=2048, parallelism=2, type='id', max_threads=16, relaxed=False).hash(password)

	return f'\nSalt Used: {salt} ->  \n\nHash: -> {hash}'
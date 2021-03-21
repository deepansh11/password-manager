import hashing

if __name__ == '__main__':
	hash = hashing.hash_argon2('password')
	print(hash)
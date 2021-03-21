import scrypt,secrets

class Hash:
    def __init__(self, password):
        self.password = password

    def hashFunc(self):
        salt = secrets.token_bytes(32)
        scrypt_key = scrypt.hash(self.password,salt,N=2048,r=8,p=1)
        print("Class works, key: ",scrypt_key)

import hashlib
from blockchain import Blockchain

class AuthSystem:
    def __init__(self):
        self.blockchain = Blockchain()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        password_hash = self.hash_password(password)
        if self.blockchain.is_user_valid(username, password_hash):
            print("❌ User already exists!")
            return
        self.blockchain.add_block({"user": username, "pass": password_hash})
        print("✅ User registered successfully.")

    def login_user(self, username, password):
        password_hash = self.hash_password(password)
        if self.blockchain.is_user_valid(username, password_hash):
            print("✅ Login successful!")
        else:
            print("❌ Invalid credentials.")

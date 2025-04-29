import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data  # user info
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        info = f"{self.index}{self.timestamp}{self.data}{self.prev_hash}"
        return hashlib.sha256(info.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), {"user": "genesis", "pass": "root"}, "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        new_block = Block(len(self.chain), time.time(), data, self.get_latest_block().hash)
        self.chain.append(new_block)

    def is_user_valid(self, username, password_hash):
        for block in self.chain[1:]:  # skip genesis
            if block.data["user"] == username and block.data["pass"] == password_hash:
                return True
        return False

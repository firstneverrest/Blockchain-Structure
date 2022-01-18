import datetime
import hashlib
import json

class blockchain:
    def __init__(self):
        self.chain = [] # list of blocks
        self.add_block(nonce=1, previous_hash='0')
        self.add_block(nonce=3, previous_hash='12')

    def add_block(self, nonce, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'nonce': nonce,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

    # return the last block in the chain
    def get_previous_block(self):
        return self.chain[-1]

    # hash the block (sha256) 64 characters
    def hash(self, block):
        encode_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encode_block).hexdigest()

blockchain = blockchain()
print(blockchain.hash(blockchain.chain[0]))
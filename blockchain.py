import datetime

class blockchain:
    def __init__(self):
        self.chain = [] # list of blocks
        self.add_block(nonce=1, previous_hash='0')

    def add_block(self, nonce, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'nonce': nonce,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

blockchain = blockchain()
print(blockchain.chain)
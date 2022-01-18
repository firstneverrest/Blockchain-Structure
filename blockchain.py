import datetime
import hashlib
import json
from flask import Flask, jsonify

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

    # return the last block in the chain
    def get_previous_block(self):
        return self.chain[-1]

    # hash the block (sha256) 64 characters
    def hash(self, block):
        encode_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encode_block).hexdigest()

    # find nonce that will make the hash start with 4 zeros
    def proof_of_work(self, previous_nonce):
        new_nonce = 1
        check_proof = False # check nonce until it equals to target hash (4 zeros)

        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_nonce ** 2 - previous_nonce ** 2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_nonce += 1
        return new_nonce

# web server
app = Flask(__name__)

blockchain = blockchain()

@app.route('/')
def hello():
    return '<h1>Blockchain server is running</h1>'

@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200

@app.route('/mining', methods=['GET'])
def mining_block():
    # get previous nonce
    previous_block = blockchain.get_previous_block()
    previous_nonce = previous_block['nonce']
    # find nonce
    nonce = blockchain.proof_of_work(previous_nonce)
    previous_hash = blockchain.hash(previous_block)
    # add block
    block = blockchain.add_block(nonce, previous_hash)
    response = {
        'message': 'Block added successfully',
        'block': block
    }
    return jsonify(response), 200

# run server
if __name__ == '__main__':
    app.run()
import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask


class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.currentTransactions = []

    def newBlock(self, proof, previousHash=None):
        block = {
            'index' : len(self.chain) + 1,
            'timestamp' : time(),
            'transactions' : self.currentTransactions,
            'proof' : proof,
            'previousHash' : previousHash or self.hash(self.chain[-1])
        }
        self.chain.append(block)

        self.currentTransactions = []

        return block

    def newTransaction(self, sender, recipient, amount):
        self.currentTransactions.append({
            'sender' : sender,
            'recipient' : recipient,
            'amount' : amount
        })
        return self.lastBlock['index'] + 1

    def proofOfWork(self, laskProof):
        proof = 0
        while self.valid_proof(lastProof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def validProof(lastProof, proof):
        guess = f'{lastProof}{proof}'.encode()
        guessHash = hashlib.sha256(guess).hexdigest()
        print(guessHash[:4] == '0000')
        print(guessHash)
        return guessHash[:4] == '0000'

    @property
    def lastBlock(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        blockString = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(blockString).hexdigest()



app = Flask(__name__)

nodeIdentifier str(uuid4()).replace('-', '')

blockchain = BlockChain()


@app.route('/mine', methods=['GET'])
def mine():
    # TODO
    return 'mining'

@app.route('/transactions/new', methods=['POST'])
def newTransaction():
    # TODO
    return 'new transactions'

@app.route('/chain', methods=['GET']):
def fullChain():
    response = {
        'chain'  : blockchain.chain,
        'length' : len(blockchain.chain)
    }
    return jsonify(response), 200

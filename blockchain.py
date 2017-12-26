import hashlib
import json
from time import time

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

    @property
    def lastBlock(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        blockString = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(blockString).hexdigest()

import hashlib
import json
from time import time

#Representing a blockchain

## BLUEPRINT FOR CLASS ##

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

        #Creating the genesis block, this is the first hash with no predecssors
        self.new_block(previous_hash=1, proof=100)
    
    def new_block(self):
        #creates a new block and adds it to the chain
        pass

    def new_transaction(self):
        #adds a new transaction to the list of transactions
        pass

    @staticmethod
    def hash(block):
        #hashes a block
        pass

    @property
    def last_block(self):
        pass

    ## NEW TRANSACTIONS ##

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined block
        :param sender: <str> Address of sender
        :param recipient: <str> address of recipient
        :param amount: <init> amount
        :return: <int> the index of the block that holds transaction
        """
        self.current_transaction.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1
    
    ## CREATING NEW BLOCKS ##
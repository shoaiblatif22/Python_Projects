#Representing a blockchain
#We'll first create a blockhain using a constructor

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []
    
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
        #returns the last block in the chain
        pass
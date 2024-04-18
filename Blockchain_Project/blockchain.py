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
        pass

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined block
        :param sender: <str> Address of sender
        :param recipient: <str> address of recipient
        :param amount: <init> amount
        :return: <int> the index of the block that holds transaction
        """
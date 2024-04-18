#Representing a blockchain
#We'll first create a blockhain using a constructor

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []
        
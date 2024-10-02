import hashlib
import datetime

class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(block_data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", datetime.datetime.now(), "Bloco Gênesis - Registro Inicial")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_data):
        latest_block = self.get_latest_block()
        new_index = latest_block.index + 1
        new_block = Block(new_index, latest_block.hash, datetime.datetime.now(), new_data)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

my_blockchain = Blockchain()

my_blockchain.add_block({
    'nome_aluno': 'João Silva',
    'instituicao': 'Universidade X',
    'curso': 'Ciência da Computação',
    'data_graduacao': '01/12/2024'
})

my_blockchain.add_block({
    'nome_aluno': 'Maria Souza',
    'instituicao': 'Universidade Y',
    'curso': 'Engenharia Civil',
    'data_graduacao': '15/07/2023'
})

for block in my_blockchain.chain:
    print(f"Bloco {block.index}:")
    print(f"Hash: {block.hash}")
    print(f"Hash Anterior: {block.previous_hash}")
    print(f"Data: {block.timestamp}")
    print(f"Dados: {block.data}")
    print("-" * 30)

print(f"Blockchain válida? {my_blockchain.is_chain_valid()}")
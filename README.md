# Trabalho sobre Blockchain - Aula se Segurança da Informação - Prof Bruno Zolotareff

Nesse repositório encontra-se a 1° parte da atividade, que é um fichamento/resumo do artigo científico sobre Blockchain, especificamente, o Blockchain na educação. Assim como, a 2° parte, a mais funcional, que é uma simples aplicação, a qual o código está escrito e descrito mais a seguir, aqui na descrição e conta com um vídeo.

** Linkdin do professor: https://www.linkedin.com/in/bzsantos/

## Artigo
Artigo científico com tema “Uso de Blockchain na Educação: Estado da arte e desafios em aberto”, de Anderson Mero de Morais, 2020, disponível na Revista Científica Multidisciplinar: Núcleo do Conhecimento.
Acesso: https://www.nucleodoconhecimento.com.br/tecnologia/uso-de-blockchain

## Integrantes e Linkdin
- Gabriel Paulino: https://www.linkedin.com/in/gabriel-paulino-568b43330/
- Giovanna Carvalho: www.linkedin.com/in/giovanna-carvalho-silva
- Pietro Enrico: https://www.linkedin.com/in/pietro-guerra-bb6538257/

## Fichamento
O fichamento elaborado sobre o artigo "Uso de Blockchain na Educação: Estado da arte e desafios em aberto" apresenta uma análise da aplicação da tecnologia blockchain no contexto educacional, aborda os conceitos fundamentais do blockchain, suas principais aplicações na educação, os benefícios e desafios associados à sua implementação, a metodologia utilizada na pesquisa e a conclusão, que ressalta a opinião do grupo.

## Aplicação
A aplicação implementa uma blockchain simples em Python para registrar diplomas acadêmicos. O projeto visa demonstrar como a tecnologia blockchain pode ser utilizada para garantir a segurança, transparência e imutabilidade dos registros de diplomas.

### Funcionalidades:
- Adicionar Diplomas: O sistema permite adicionar informações de diplomas, como nome do aluno, instituição, curso e data de graduação, diretamente no código.
- Blockchain: Cada diploma inserido é armazenado em um bloco da blockchain. Cada bloco possui um índice, um hash próprio, o hash do bloco anterior, o timestamp (data e hora), e os dados do diploma.
- Validação da Blockchain: A aplicação também verifica a integridade da blockchain, garantindo que os blocos não foram modificados, mantendo a confiança no sistema.

### Objetivo:
A aplicação tem como objetivo ilustrar o uso prático da tecnologia blockchain no contexto de registros acadêmicos, permitindo que diplomas possam ser validados de forma segura e imutável ao longo do tempo.

## Código da aplicação
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

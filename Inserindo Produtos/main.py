import pymongo


def insert_data():
    """
    função para obter os dados pelo usuário
    """
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preco do produto: "))

    return {"produto": produto, "preco": preco}


# conectando ao database e collection do MongoDB
cliente = pymongo.MongoClient("localhost", 27017)
banco = cliente["crud"]
colecao = banco["mercado"]

while True:
    dados = insert_data()
    colecao.insert_one(dados)
    continua = input("Deseja inserir outro produto? (S/N): ")

    if continua.lower() != "S":
        break

cliente.close()

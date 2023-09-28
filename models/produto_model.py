from db import _execute

class Produto:

    def __init__(self, nome, preco,id = None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.status = 1 #ativo = 1, inativo = 0

        #se a tabela produtos nao exixtir crie-a
        query = "CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, preco REAL, status NUMERIC)"
        _execute(query)

    def save(self):
        query = f"INSERT INTO produtos (nome, preco, status) VALUES ('{self.nome}', {float(self.preco)}, {self.status})"
        _execute(query)

    def update(self):
        query = f"UPDATE produtos SET status={int(self.status)} WHERE id={int(self.id)}"
        _execute(query)

    def delete(self):
        query = f"DELETE FROM produtos WHERE id={int(self.id)}"
        _execute(query)
    
    @staticmethod
    def get_produtos():
        query = "SELECT * FROM produtos"
        produtos = _execute(query)
        return produtos

    
    @staticmethod
    def get_produto(id):
        query = f"SELECT id, nome, preco FROM produtos WHERE id={int(id)}"
        produto = _execute(query)[0]
        produto = Produto(id=produto[0], nome=produto[1], preco=produto[2])
        return produto

    
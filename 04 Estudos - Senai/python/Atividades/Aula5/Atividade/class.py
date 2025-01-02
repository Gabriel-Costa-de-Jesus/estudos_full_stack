class Livro:
    def __init__(self, nome, autor, preco):
        self.nome = nome
        self.autor = autor
        self.preco = preco
        
livro = Livro("Jefté e o pé de Feijão", "João", 60)
print(livro.nome)
print(livro.autor)
print(livro.preco)
   
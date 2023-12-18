"""
Crie uma classe chamada Livro com os seguintes atributos:

titulo (título do livro)
autor (autor do livro)
ano_publicacao (ano de publicação do livro)
status (indicando se o livro está disponível ou emprestado)
Crie uma classe chamada Biblioteca com um atributo:

livros (uma lista que armazena objetos da classe Livro)
A classe Biblioteca deve ter os seguintes métodos:

adicionar_livro(livro): Adiciona um livro à lista de livros da biblioteca.
listar_livros(): Lista todos os livros da biblioteca com seus respectivos títulos, autores e status.
emprestar_livro(titulo): Marca um livro como emprestado se estiver disponível.
devolver_livro(titulo): Marca um livro como disponível se estiver emprestado.
Crie alguns objetos da classe Livro e da classe Biblioteca, em seguida, realize operações como adicionar livros, listar livros, emprestar e devolver livros.
"""

class Livro:

    def __init__(self, titulo, autor, ano_publicado, status):
        self.__titulo = titulo
        self.__autor =  autor
        self.__ano_publicado = ano_publicado
        self.__status =  status
    
    def info(self):
        print(f'Titulo: {self.__titulo}, Autor: {self.__autor}, Ano: {self.__ano_publicado}, Status: {self.__status}]')

    def titulo(self):
        return self.__titulo       

    def status(self):
        return self.__status
    
    def disponivel_indisponivel(self):
        if self.__status == "Disponível":
            self.__status = 'Indisponível'
        else:
            self.__status = "Disponível"
    
class Biblioteca:

    total_de_livros = 0

    def __init__(self):
        self.__livros = []
    
    def adicionar_livro(self, livro):
        self.__livros.append(livro)
        Biblioteca.total_de_livros += 1
    
    def emprestar_livro(self, titulo):
        for livro in self.__livros:
            if livro.titulo() == titulo and livro.status() == 'Disponível':
                livro.disponivel_indisponivel()
                Biblioteca.total_de_livros -= 1
                return

        print(f'Livro: {titulo} esta Indisponível')

    def devolver_livro(self, titulo):
        for livro in self.__livros:
            if livro.titulo() == titulo:
                livro.disponivel_indisponivel()
                Biblioteca.total_de_livros += 1
    
    def listar_livros(self):
        for livro in self.__livros:
            livro.info()

livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899, "Disponível")
livro2 = Livro("1984", "George Orwell", 1949, "Disponível")

biblioteca = Biblioteca()

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)


biblioteca.listar_livros()
biblioteca.emprestar_livro("Dom Casmurro")
biblioteca.emprestar_livro("1984")
print(livro2.status())
biblioteca.emprestar_livro("1984")
biblioteca.devolver_livro('1984')
print(livro2.status())
biblioteca.listar_livros()


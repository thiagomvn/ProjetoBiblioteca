import usuario

class Comentarios:
    def __init__(self, livro, id, nome, comentario): # falta id.usuario e nome.usuario
        self.id = usuario(id)
        self.nome = usuario(nome)
        self.livro = livro
        self.comentario = comentario

    def gerenciar_comentario():
        return
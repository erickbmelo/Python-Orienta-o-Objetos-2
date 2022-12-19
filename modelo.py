class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'


class Playlist:
    def __init__(self, nome_playlist, programas):
        self.nome_playlist = nome_playlist
        self.programas = programas

    def tamanho(self):
        return len(self.programas)


vingadores = Filme('Vingadores - Guerra Infinita', 2018, 160)
atlanta = Serie('atlanta', 2019, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
demolidor.dar_like()
tmep.dar_like()
tmep.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [atlanta, vingadores, demolidor, tmep]

playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

for programa in playlist_fim_de_semana.programas:
    print(programa)

print(playlist_fim_de_semana.tamanho())
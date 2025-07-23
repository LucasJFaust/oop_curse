"""
Agora vamos ver como definir instances attributes para as calsses circulo, retangulo e movie. Vamos considerar que a classe circulo tenha um instance attribute chamado raio.
"""
class Circulo:

    def __init__(self, raio, cor):
        self.raio = raio
        self.cor = "Azul"

class Retangulo:

    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

class Movie:

    def __init__(self, titulo, ano, lingua, nota):
        self.titulo = titulo
        self.ano = ano
        self.lingua = lingua
        self.nota = nota
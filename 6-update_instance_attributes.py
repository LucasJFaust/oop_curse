"""
Aqui vaos mostrar como atualizar atributos da instância de uma classe em Python.
"""

class Backpack:
    def __init__(self, color):
        self.items = []
        self.color = color

# my_backpack = Backpack("Blue")  # Criando uma instância da classe Backpack com a cor "Blue"
# your_backpack = Backpack("Green")  # Criando outra instância com a cor "Green"

# print(my_backpack.color)  # Imprime a cor inicial da mochila
# print(your_backpack.color)  # Imprime a cor da outra mochila

# print("Atualizando atributos da instância... Só da instância my_backpack")
# my_backpack.color = "Red"  # Atualizando o atributo color da instância my_backpack
# print(my_backpack.color)
# print(your_backpack.color)

class Cirulo:
    def __init__(self, raio, cor):
        self.raio = raio
        self.cor = cor

meu_circulo = Cirulo(10, "Vermelho")  # Criando uma instância da classe Cirulo com raio 10 e cor "Vermelho"
print(meu_circulo.raio)
print(meu_circulo.cor)

meu_circulo.raio = 15  # Atualizando o atributo raio da instância meu_circulo
meu_circulo.cor = "Azul"  # Atualizando o atributo cor da instância meu_circulo

print(meu_circulo.raio)  # Imprime 15, o novo valor de raio
print(meu_circulo.cor)   # Imprime "Azul", o novo valor de cor


"""
Aqui vaos mostrar como atualizar atributos da instância de uma classe em Python.
"""

class Backpack:
    def __init__(self, color):
        self.items = []
        self.color = color

my_backpack = Backpack("Blue")  # Criando uma instância da classe Backpack com a cor "Blue"
your_backpack = Backpack("Green")  # Criando outra instância com a cor "Green"

print(my_backpack.color)  # Imprime a cor inicial da mochila
print(your_backpack.color)  # Imprime a cor da outra mochila

print("Atualizando atributos da instância... Só da instância my_backpack")
my_backpack.color = "Red"  # Atualizando o atributo color da instância my_backpack
print(my_backpack.color)
print(your_backpack.color)
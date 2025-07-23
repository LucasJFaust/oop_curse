"""
Para de fato criar uma instância de uma classe, devos usar o nome da classe seguido de parênteses, passando os argumentos necessários para o construtor (__init__). 
Vamos ver como criar instâncias da classe backpack.
"""
class Backpack:

    def __init__(self):
        self.items = []

# Agora vamos criar uma instância da classe Backpack e direcionar a instância para uma variável chamada my_backpack.

my_backpack = Backpack()    # Aqui a minha variável my_backpack agora contém uma instância da classe Backpack. Lembrando que, neste caso, só temos self como parâmetro do construtor, 
                            # então não precisamos passar nenhum argumento ao criar a instância.

class Circulo:

    def __init__(self, raio):
        self.raio = raio

print(my_backpack.items)  # Isso deve imprimir uma lista vazia, pois ainda não adicionamos nenhum item à mochila.
meu_circulo = Circulo(5)  # Aqui criamos uma instância da classe Circulo com raio 5.
print(meu_circulo.raio)

# Multiplos argumentos

class Retangulo:

    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        print(self.comprimento)
        self.largura = largura
        print(self.largura)

meu_retangulo = Retangulo(10, 5)  # Criando uma instância da classe Retangulo com comprimento 10 e largura 5.
# print(meu_retangulo.comprimento, meu_retangulo.largura)  # Imprimindo os atributos da instância do retângulo.
meu_retangulo2 = Retangulo(20, 15)  # Criando outra instância com valores diferentes.
# print(meu_retangulo2.comprimento, meu_retangulo2.largura)  # Imprimindo os atributos da segunda instância do retângulo.


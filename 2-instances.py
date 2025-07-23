"""
Com as nossas blueprints (ou classes) podemos criar instâncias, que são objetos concretos baseados nessas blueprints.
Uma instance é um objeto criado a partir de uma classe. Cada instância tem seus próprios atributos e métodos, que são definidos na classe.
Uma classe é uma representação mais abstrata de um objeto, enquanto uma instância é uma representação concreta desse objeto. Por exemplo, se criarmos uma classe chamada Backpack
esse blueprint pode representar qualquer backpack, mas uma instância dessa classe seria uma mochila específica, como a minha mochila azul.
Insances attributes são independentes de cada instância, ou seja, cada instância pode ter valores diferentes para os mesmos atributos. Eles pertencem a uma objeto específico
e são definidos dentro do método __init__() da classe.

Nos podemos definir instances attributes usando o metodo __init__() da classe, que é chamado quando criamos uma nova instância da classe.
O que é o método __init__()?
O método __init__() é um método especial em Python que é chamado automaticamente quando uma nova instância de uma classe é criada. Ele é usado para inicializar os atributos da instância e
configurar o estado inicial do objeto. O método __init__() recebe o parâmetro self, que é uma referência à instância atual da classe, e pode receber outros parâmetros para definir os
atributos da instância.
Para treinar vamos representaruma classe de casa:
"""
class House:

    def __init__(self, price):    # Aqui estamos definindo o método __init__() da classe House. O método nesse contexto é usado para inicializar os atributos da instância.
        self.price = price        # Aqui estamos definindo um parâmetro price que será usado para inicializar o atributo price da instância. O self.price é um atributo da instância, que é acessível através do objeto criado a partir da classe House.

# Agora vamos definir uma classe para Backpack:
class Backpack:

    def __init__(self, color, size):    # O self deve ser sempre o primeiro parâmetro do método __init__() e de todos os métodos da classe. Ele é usado para referenciar a instância atual da classe.
        self.items = []    # Aqui estamos definindo um atributo items que será uma lista vazia, onde podemos armazenar os itens que estão dentro da mochila.
        self.coler = color
        self.size = size

# O propósito do self é um método genérico que é usado para referenciar a instância atual da classe. Ele permite acessar os atributos e métodos da instância dentro da classe.
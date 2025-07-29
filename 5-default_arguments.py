"""
Os default arguments são valores que podem ser passados para um método ou função, mas não são obrigatórios. Se não forem fornecidos, os valores padrão serão usados.
Isso é útil para evitar a necessidade de especificar todos os argumentos sempre que a função é chamada.
"""

class Circulo:
    def __init__(self, raio=5, cor="Azul"):    # Aqui se omitirmos os argumentos, raio será 5 e cor será "Azul" por padrão.
        self.raio = raio
        self.cor = cor

meu_circulo = Circulo()  # Aqui criamos uma instância da classe Circulo sem passar argumentos, então os valores padrão serão usados.
print(meu_circulo.raio)  # Isso deve imprimir 5, o valor padrão de raio.
print(meu_circulo.cor)   # Isso deve imprimir "Azul", o valor padrão de cor.
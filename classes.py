import random
from palavras import port
import time

class Palavra: # Falta fazer pra qnd erra a palavra
    def __init__(self, y, x):
        self.y = 200 # posicao inicial no eixo y
        self.x = random.randint(200, 800) # posicao no eixo x, fixo mas aleatorio 
        self.speed = 1
        self.texto = ""

    def addSpeed(self):
        self.speed += 0.1

    def moveUm(self):
        alturaMax = 640
        if self.y <= alturaMax:
            self.y += self.speed


    def setTexto(self, string):
        self.texto = string

class PalavraPort(Palavra):
    def __init__(self, y=200, x=random.randint(200, 800)):
        super().__init__(y, x)
        super().setTexto(random.choice(port))


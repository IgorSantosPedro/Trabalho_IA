class No:
    def __init__(self, nome, pai = None, g=0, h=0):
        self.nome = nome
        self.pai = pai
        self.g = g
        self.h = h
        self.f = self.g + self.h

    # Comparar nos
    def __eq__(self, outro):
        return self.nome == outro.nome

    # comparar funcoes
    def __lt__(self, outro):
         return self.f < outro.f

    # represetacao no
    def __repr__(self):
        return (f'({self.nome},{self.f})')
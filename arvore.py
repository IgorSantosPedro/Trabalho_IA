class Arvore:
    def __init__(self):
        self.Arvore_dict = {}

    # caminhos de ida e volta iguais
    def nao_dirigida(self):
        for a in list(self.Arvore_dict.keys()):
            for (b, dist) in self.Arvore_dict[a].items():
                self.Arvore_dict.setdefault(b, {})[a] = dist

    # ligar nos
    def ligar(self, A, B, distancia = 1):
        self.Arvore_dict.setdefault(A, {})[B] = distancia

    # pegar vizinhos
    def get(self, atual, proximo = None):
        adjacentes = self.Arvore_dict.setdefault(atual, {})
        if proximo is None:
            return adjacentes
        else:
            return adjacentes.get(proximo)
            
    # pega todos os nos da arvore
    def nos(self):
        s1 = set([k for k in self.Arvore_dict.keys()])
        s2 = set([k2 for v in self.Arvore_dict.values() for k2, v2 in v.items()])
        nos = s1.union(s2)
        return list(nos)
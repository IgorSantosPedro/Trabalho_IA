from distancias import Distancia
from arvore import Arvore
from estado import No
from cidades import Estádio

def a_estrela(Arvore, base_distancias, inicio, fim, distancia_inicial):

    lista_abertos = []
    lista_fechados = []

    no_inicial = No(nome = inicio, h = distancia_inicial)
    no_final = No(nome = fim)

    lista_abertos.append(no_inicial)

    while len(lista_abertos) > 0:
        print(f'lista abertos: {lista_abertos}\n')

        # organizar a lista em ordem crescente de funcao e pegar o menor
        lista_abertos.sort()
        no_atual = lista_abertos.pop(0)

        # inserir no atual na lista_fechados
        lista_fechados.append(no_atual)
        print(f'lista fechados: {lista_fechados}\n')

        # verificar se chegou no destino
        if no_atual == no_final:
            caminho = []
            while no_atual != no_inicial:
                caminho.append(no_atual.nome + ': ' + str(no_atual.g))
                no_atual = no_atual.pai
            caminho.append(no_inicial.nome + ': ' + str(no_inicial.g))
            return caminho[::-1]

        # verificar vizinhos
        vizinhos = Arvore.get(no_atual.nome)
        print(f'nos vizinhos: {vizinhos}\n')

        # Loop entre vizinhos
        for chave in vizinhos.keys():
            vizinho = No(chave, no_atual)
            if(vizinho in lista_fechados):
                continue
            # calculo do custo acumulado e funcao
            vizinho.g = no_atual.g + Arvore.get(no_atual.nome, vizinho.nome)
            vizinho.h = base_distancias.get(vizinho.nome)
            vizinho.f = vizinho.g + vizinho.h if vizinho.h is not None else vizinho.g
            if(inserir_lista_abertos(lista_abertos, vizinho) == True):
                lista_abertos.append(vizinho)

    # caminho nao encontrado
    return None


# verificar se vizinho deve ser incluido em lista_abertos
def inserir_lista_abertos(lista_abertos, vizinho):
    for aberto in lista_abertos:
        # f do vizinho precisa ser menor
        if (vizinho == aberto and vizinho.f > aberto.f):
            return False
    return True



def main():
    distancia_padrao = Distancia()
    arvore = Arvore()

    lista_estadios = (Estádio()).lista_estadios
    estadios = (Estádio()).estadios_string

    # interacao com user
    opcao_origem = input(f'{estadios}Insira o código da cidade origem: ')
    opcao_origem = lista_estadios[int(opcao_origem) - 1]
    opcao_destino = input(f'{estadios}Insira o código da cidade destino: ')
    opcao_destino = lista_estadios[int(opcao_destino) - 1]
    origem = opcao_origem
    destino = opcao_destino

    # pegando distancias ja configuradas pra montar lista personalizada
    lista_destino = {}
    for item in distancia_padrao.distancias_inadmissivel:
        lista_destino[item] = distancia_padrao.distancias_inadmissivel11[item][destino][0]

    # "criar" grafo de conexoes entre estadios
    arvore.ligar('Estádio_Al_Thumama', 'Estádio_Al_Janoub', distancia_padrao.distancias_inadmissivel11['Estádio_Al_Thumama']['Estádio_Al_Janoub'][1] )
    arvore.ligar('Estádio_Al_Thumama', 'Estádio_Cidade_da_Educação', distancia_padrao.distancias_inadmissivel11['Estádio_Al_Thumama']['Estádio_Cidade_da_Educação'][1] )
    arvore.ligar('Estádio_Al_Thumama', 'Estádio_Ahmad_bin_Ali', distancia_padrao.distancias_inadmissivel11['Estádio_Al_Thumama']['Estádio_Ahmad_bin_Ali'][1] )
    arvore.ligar('Estádio_Al_Thumama', 'Delegação_Francesa_(FFF)_Al_Messila_Resort', distancia_padrao.distancias_inadmissivel11['Estádio_Al_Thumama']['Delegação_Francesa_(FFF)_Al_Messila_Resort'][1] )
    arvore.ligar('Delegação_Francesa_(FFF)_Al_Messila_Resort', 'Estádio_Al_Thumama', distancia_padrao.distancias_inadmissivel11['Delegação_Francesa_(FFF)_Al_Messila_Resort']['Estádio_Al_Thumama'][1] )
    arvore.ligar('Estádio_Al_Janoub', 'Al_Thumama', distancia_padrao.distancias_inadmissivel11['Estádio_Al_Janoub']['Estádio_Al_Thumama'][1] )
    arvore.ligar('Estádio_Cidade_da_Educação', 'Estádio_Al_Thumama', distancia_padrao.distancias_inadmissivel11['Estádio_Cidade_da_Educação']['Estádio_Al_Thumama'][1] )
    arvore.ligar('Estádio_Cidade_da_Educação', 'Estádio_Ahmad_bin_Ali', distancia_padrao.distancias_inadmissivel11['Estádio_Cidade_da_Educação']['Estádio_Ahmad_bin_Ali'][1] )
    arvore.ligar('Estádio_Cidade_da_Educação', 'Estádio_Internacional_Khalifa', distancia_padrao.distancias_inadmissivel11['Estádio_Cidade_da_Educação']['Estádio_Internacional_Khalifa'][1] )
    arvore.ligar('Estádio_Cidade_da_Educação', 'Estádio_974', distancia_padrao.distancias_inadmissivel11['Estádio_Cidade_da_Educação']['Estádio_974'][1] )    
    arvore.ligar('Estádio_Cidade_da_Educação', 'Estádio_Lusail', distancia_padrao.distancias_inadmissivel11['Estádio_Cidade_da_Educação']['Estádio_Lusail'][1] )
    arvore.ligar('Estádio_Cidade_da_Educação', 'Delegação_Brasileira_(CBF)_Westin_Hotel_Doha', distancia_padrao.distancias_inadmissivel11['Estádio_Cidade_da_Educação']['Delegação_Brasileira_(CBF)_Westin_Hotel_Doha'][1] )
    arvore.ligar('Delegação_Brasileira_(CBF)_Westin_Hotel_Doha', 'Estádio_Cidade_da_Educação', distancia_padrao.distancias_inadmissivel11['Delegação_Brasileira_(CBF)_Westin_Hotel_Doha']['Estádio_Cidade_da_Educação'][1] )
    arvore.ligar('Estádio_Ahmad_bin_Ali', 'Estádio_Al_Thumama', distancia_padrao.distancias_inadmissivel11['Estádio_Ahmad_bin_Ali']['Estádio_Al_Thumama'][1] )
    arvore.ligar('Estádio_Ahmad_bin_Ali', 'Estádio_Internacional_Khalifa', distancia_padrao.distancias_inadmissivel11['Estádio_Ahmad_bin_Ali']['Estádio_Internacional_Khalifa'][1] )
    arvore.ligar('Estádio_Ahmad_bin_Ali', 'Estádio_Cidade_da_Educação', distancia_padrao.distancias_inadmissivel11['Estádio_Ahmad_bin_Ali']['Estádio_Cidade_da_Educação'][1] )
    arvore.ligar('Estádio_Internacional_Khalifa', 'Estádio_Ahmad_bin_Ali', distancia_padrao.distancias_inadmissivel11['Estádio_Internacional_Khalifa']['Estádio_Ahmad_bin_Ali'][1] )
    arvore.ligar('Estádio_Internacional_Khalifa', 'Estádio_Cidade_da_Educação', distancia_padrao.distancias_inadmissivel11['Estádio_Internacional_Khalifa']['Estádio_Cidade_da_Educação'][1] )
    arvore.ligar('Estádio_Internacional_Khalifa', 'Estádio_Al_Bayt', distancia_padrao.distancias_inadmissivel11['Estádio_Internacional_Khalifa']['Estádio_Al_Bayt'][1] )    
    arvore.ligar('Estádio_Internacional_Khalifa', 'Estádio_Lusail', distancia_padrao.distancias_inadmissivel11['Estádio_Internacional_Khalifa']['Estádio_Lusail'][1] )
    arvore.ligar('Estádio_Internacional_Khalifa', 'Delegação_Alemã_(DFB)_Zulal_Wellness_Resort', distancia_padrao.distancias_inadmissivel11['Estádio_Internacional_Khalifa']['Delegação_Alemã_(DFB)_Zulal_Wellness_Resort'][1] )
    arvore.ligar('Delegação_Alemã_(DFB)_Zulal_Wellness_Resort', 'Estádio_Internacional_Khalifa', distancia_padrao.distancias_inadmissivel11['Delegação_Alemã_(DFB)_Zulal_Wellness_Resort']['Estádio_Internacional_Khalifa'][1] )
    arvore.ligar('Estádio_Lusail', 'Estádio_Cidade_da_Educação', distancia_padrao.distancias_inadmissivel11['Estádio_Lusail']['Estádio_Cidade_da_Educação'][1] )
    arvore.ligar('Estádio_Lusail', 'Estádio_Internacional_Khalifa', distancia_padrao.distancias_inadmissivel11['Estádio_Lusail']['Estádio_Internacional_Khalifa'][1] )
    arvore.ligar('Estádio_Lusail', 'Estádio_Al_Bayt', distancia_padrao.distancias_inadmissivel11['Estádio_Lusail']['Estádio_Al_Bayt'][1] )
    arvore.ligar('Estádio_Lusail', 'Estádio_974', distancia_padrao.distancias_inadmissivel11['Estádio_Lusail']['Estádio_974'][1] )
    arvore.ligar('Estádio_974', 'Estádio_Cidade_da_Educação', distancia_padrao.distancias_inadmissivel11['Estádio_974']['Estádio_Cidade_da_Educação'][1] )
    arvore.ligar('Estádio_974', 'Estádio_Lusail', distancia_padrao.distancias_inadmissivel11['Estádio_974']['Estádio_Lusail'][1] )
    arvore.ligar('Estádio_974', 'Estádio_Al_Bayt', distancia_padrao.distancias_inadmissivel11['Estádio_974']['Estádio_Al_Bayt'][1] )
    arvore.ligar('Estádio_Al_Bayt', 'Estádio_974', distancia_padrao.distancias_inadmissivel11['Estádio_Al_Bayt']['Estádio_974'][1] )
    arvore.ligar('Estádio_Al_Bayt', 'Estádio_Internacional_Khalifa', distancia_padrao.distancias_inadmissivel11['Estádio_Al_Bayt']['Estádio_Internacional_Khalifa'][1] )
    arvore.ligar('Estádio_Al_Bayt', 'Estádio_Lusail', distancia_padrao.distancias_inadmissivel11['Estádio_Al_Bayt']['Estádio_Lusail'][1] )
    arvore.ligar('Estádio_Al_Bayt', 'Delegação_Argentina_(AFA)_Qatar_University_Sports_&_Events_Complex', distancia_padrao.distancias_inadmissivel11['Estádio_Al_Bayt']['Delegação_Argentina_(AFA)_Qatar_University_Sports_&_Events_Complex'][1] )
    arvore.ligar('Delegação_Argentina_(AFA)_Qatar_University_Sports_&_Events_Complex', 'Estádio_Al_Bayt', distancia_padrao.distancias_inadmissivel11['Delegação_Argentina_(AFA)_Qatar_University_Sports_&_Events_Complex']['Estádio_Al_Bayt'][1] )

    # tornan arvore nao dirigida, criar ligacoes simetricas
    arvore.nao_dirigida()
    caminho = a_estrela(arvore, lista_destino, origem, destino, distancia_padrao.distancias_inadmissivel11[origem][destino][0])
    print(caminho)

if __name__ == "__main__": main()
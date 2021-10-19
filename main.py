from pathlib import Path

class Transicao:
    def __init__(self, valores, estado_dest):
        self.valores        = valores
        self.estado_dest    = estado_dest

class Estado:
    def __init__(self, nome, flag_inicial, flag_final, transicoes):
        self.nome           = nome
        self.flag_inicial   = flag_inicial
        self.flag_final     = flag_final
        self.transicoes     = transicoes

class Alfabeto:
    def __init__(self, nome_estados, caracteres_aceitos, estado_inicial, estado_final): #construtor que recebe oos atributos que são vetores ou não
        self.Q = nome_estados #Nomes dos estados que estão separados por espaços
        self.S = caracteres_aceitos #Caracteres que são aceitos pela nossa máquina
        self.I = estado_inicial #Nome do estado inicial (mesmo maluco do nome_estados)
        self.F = estado_final #Nome do estado final (mesmo maluco do nome_estados)


input_file      = open(Path('init.txt'), "r")
estados_input   = input_file.readline().replace("Q: ", "").replace("\n", "").split(" ")
estado_inicial  = input_file.readline().replace("I: ", "").replace("\n", "")

if (estado_inicial not in estados_input):
    print("\nEstado inicial inválido!")
else:
    estados_finais  = input_file.readline().replace("F: ", "").replace("\n", "")
    estados         = []

    # Percorre os estados do input criando um objeto Estado para cada e adicionando na lista estados
    for estado in estados_input:

        flag_ini = False
        flag_fin = False

        if (estado_inicial == estado):
            flag_ini = True

        if (estado in estados_finais):
            flag_fin = True

        est = Estado(estado, flag_ini, flag_fin, [])

        estados.append(est)

    transicoes      = []
    transicao_input = ""

    # Percorre as transições do input criando um objeto Transicao para cada e adicionando na lista de transições do estado origem da transição
    for linha in input_file:
        transicao_input = linha.replace("\n", "").split(" -> ") # input().split(" -> ")

        if (transicao_input[0] == "---"):
            break

        estado_origem   = transicao_input[0]
        estado_destino  = transicao_input[1].split(" | ")[0]
        valores         = transicao_input[1].split(" | ")[1].split(" ")

        transicao       = Transicao(valores, estado_destino)

        # Percorre os estados para encontrar o estado de origem da transição e adicionar a transição à lista de transições deste estado
        for estado in estados:
            if (estado.nome == estado_origem):
                estado.transicoes.append(transicao)
                break

    casos_teste = []

    for linha in input_file:
        entry = linha.replace("\n", "")
        casos_teste.append(entry)

    for caso in casos_teste:
        # Reseta o estado atual para o inicial para cada novo caso de teste
        estado_atual    = estado_inicial
        flag_erro       = False

        # Percorre os valores do caso atual
        for valor in range(len(caso)):
            
            # Percorre a lista de estados
            for estado in estados:

                # Seleciona o estado do estado atual
                if (estado_atual == estado.nome):

                    # Percorre as transições do estado atual
                    for trans in range(len(estado.transicoes)):

                        # Se encontra uma transição com o mesmo valor atual troca de estado atual
                        if (caso[valor] in estado.transicoes[trans].valores):
                            estado_atual = estado.transicoes[trans].estado_dest
                            break

                        # Se no final das transições não encontrar nenhuma transição com o mesmo valor, o caso deu errado
                        if(trans == len(estado.transicoes) - 1):
                            flag_erro = True

                    break # break para sair do for de estados e ir para o próximo valor (estava causando problema pois o estado_atual é alterado dentro do for)

        # Se no final do caso o estado atual for um estado final, o caso deu certo, caso contrário deu errado
        for estado in estados:
            if (estado_atual == estado.nome):
                if (estado.flag_final):
                    flag_erro = False
                else:
                    flag_erro = True
                
                break

        if(flag_erro):
            print("X")
        else:
            print("OK")

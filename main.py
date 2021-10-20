from pathlib import Path
from automaton.automaton import AFD_ALPHABET, Transicao, Estado, AFD, bcolors, AFN

def testAFD(file_name):
    print(bcolors.UNDERLINE + bcolors.OKCYAN + "\nAFD\n" + bcolors.RESET)
    input_file      = open(Path(file_name), "r")
    estados_input   = input_file.readline().replace("Q: ", "").replace("\n", "").split(" ")
    estado_inicial  = input_file.readline().replace("I: ", "").replace("\n", "")

    # alfabeto = Alfabeto(input_file.readline().replace("S: ", "").replace("\n", ""))
    # alfabeto.checkIsInAlphabet('a7b88bba')

    if (estado_inicial not in estados_input):
        print(bcolors.FAIL + "\nEstado inicial inválido!" + bcolors.RESET)
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

    #inicia um afd 
    afd = AFD(estado_inicial=estado_inicial, estados=estados, casos_teste=casos_teste)
    afd.verificaCasosDeTeste()

def test_afd_multiple_alphabet(file_name):
    print(bcolors.UNDERLINE + bcolors.OKCYAN + "\nAFD alfabeto\n" + bcolors.RESET)
    input_file      = open(Path(file_name), "r")
    estados_input   = input_file.readline().replace("Q: ", "").replace("\n", "").split(" ")
    alfabeto = input_file.readline().replace("S: ", "").replace("\n", "")
    estado_inicial  = input_file.readline().replace("I: ", "").replace("\n", "")

    if (estado_inicial not in estados_input):
        print(bcolors.FAIL + "\nEstado inicial inválido!" + bcolors.RESET)
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

    #inicia um afd 
    afdf = AFD_ALPHABET(estado_inicial=estado_inicial, estados=estados, casos_teste=casos_teste, alfabeto=alfabeto)
    afdf.verificaCasosDeTeste()
#Definição de Teste de AFN
def test_afn(file_name):
    print(bcolors.UNDERLINE + bcolors.OKCYAN + "\nAFN\n" + bcolors.RESET)

    input_file      = open(Path(file_name), "r")
    estados_input   = input_file.readline().replace("Q: ", "").replace("\n", "").split(" ")
    alfabeto = input_file.readline().replace("S: ", "").replace("\n", "")
    estado_inicial  = input_file.readline().replace("I: ", "").replace("\n", "").split(" ")

    if (all(item in estados_input for item in estado_inicial) == False):
        print(bcolors.FAIL + "\nEstado inicial inválido!" + bcolors.RESET)
    else:
        estados_finais  = input_file.readline().replace("F: ", "").replace("\n", "")
        estados         = []
        
        # Percorre os estados do input criando um objeto Estado para cada e adicionando na lista estados
        for estado in estados_input:

            flag_ini = False
            flag_fin = False

            if (estado in estado_inicial):
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

    # Inicia AFN
    #Verificação de labda
    if('\\' in alfabeto):
        #Inválido caso haja lambda no alfabeto
        print(bcolors.FAIL + "Alfabeto invalido!\n" + bcolors.RESET)
    else:
        #Alfabeto Válido
        afn = AFN(estado_inicial=estado_inicial, estados=estados, casos_teste=casos_teste, alfabeto=alfabeto)
        afn.verificaCasosDeTeste()

def __main__():
    testAFD('init.txt')

    test_afd_multiple_alphabet('alfabeto.txt')

    test_afn('afn2.txt')

__main__()
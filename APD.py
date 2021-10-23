from pathlib import Path

class Transicao:
    def __init__(self, valores, estado_dest):
        self.valores     = valores # Array de Pilha
        self.estado_dest = estado_dest
        
class ValoresPilha:
    def __init__(self, le, desempilha, empilha):
        self.le             = le
        self.desempilha     = desempilha
        self.empilha        = empilha

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

class Alfabeto:
    def __init__(self, alphabet): #construtor que recebe oos atributos que são vetores ou não
        self.alphabet = alphabet

    def checkIsInAlphabet(self, entry) -> bool:
        isValid = True

        #para cada caractere na string de teste checamos se ele esta no alfabeto
        for char_entry in entry:
            isIn = False
            for char in self.alphabet:
                if(char_entry == char):
                    isIn = True

            #caractere nao foi encontrado no alfbeto 
            if(isIn == False):
                isValid = False
                break

        return isValid


input_file      = open(Path ("initP.txt"),"r")
estados_input   = input_file.readline().replace("Q: ", "").replace("\n", "").split(" ")
alfabeto        =  input_file.readline().replace("S: ", "").replace("\n", "") 
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
        transicao_input = linha.replace("\n", "").split(" -> ")

        if (transicao_input[0] == "---"):
            break

        estado_origem   = transicao_input[0]
        estado_destino  = transicao_input[1].split(" | ")[0]
        valores         = transicao_input[1].split(" | ")[1].split(" ")
        
        valoresPilha = []
        
        for valor in valores:
            transP = ValoresPilha(valor.split(",")[0], valor.split(",")[1].split("/")[0], valor.split(",")[1].split("/")[1])
            valoresPilha.append(transP)
    
        transicao = Transicao(valoresPilha, estado_destino)

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
        # Reseta o estado atual para o inicial e a flag de erro para cada novo caso de teste
        estado_atual = estado_inicial
        flag_erro    = False
        pilha        = [] # Esvazia a pilha para cada novo caso de teste

        # Percorre os valores do caso atual
        for valor in range(len(caso)):
            flag_sucess  = False # Reseta a flag sucess para cada novo valor no caso de teste
            
            # Percorre a lista de estados
            for estado in estados:

                # Seleciona o estado do estado atual
                if (estado_atual == estado.nome):

                    # Percorre as transições do estado atual
                    for trans in range(len(estado.transicoes)):
                        
                        # Percorre os valores das transições de pilha
                        for valorP in estado.transicoes[trans].valores:
                            # Se o valo atual do caso de teste for igual ao valor "lê" da transição de pilha e se nesta transição de pilha não
                            # o valor desempilha for igual à "\" (vazio) ou for igual ao último elemento da lista pilha (lista que simula uma pilha)
                            # então essa transição é "escolhida"
                            if (caso[valor] == valorP.le and (valorP.desempilha == '\\' or valorP.desempilha == pilha[len(pilha) - 1])):
                                estado_atual = estado.transicoes[trans].estado_dest
                                
                                # Se existe elemento na pilha e o desempilha da transição atual for diferente de "\" e for igual ao ultimo elemento da pilha,
                                # desempilha este valor da pilha
                                if (len(pilha) > 0 and valorP.desempilha != '\\' and valorP.desempilha == pilha[len(pilha) - 1]):
                                    pilha.pop() # remove o último elemento da lista pilha
                                
                                # Se o valor empilha da transição atual for diferente de "\" (vazio), os valores serão empilhados
                                if (valorP.empilha != '\\'):
                                    count = len(valorP.empilha) -1

                                    # Percorre os valores "empilha" da transição atual, de forma invertida para empilhá-los corretamente
                                    while count >= 0:
                                        pilha.append(valorP.empilha[count])
                                        count -= 1
                                
                                # Flag succes recebe true para sair do for anteriror
                                flag_sucess = True
                                break
                        
                        # Flag succes como true significa que foi encontrada uma transição correta e então é preciso sair do for de transições do estado
                        if (flag_sucess):
                            break
                        
                        # Se chegou ao fim das transições e não encontrou uma transição correta, significa que o caso deu errado
                        if(trans == len(estado.transicoes) - 1):
                            flag_erro = True

                    break # break para sair do for de estados e ir para o próximo valor (estava causando problema pois o estado_atual é alterado dentro do for)
            
            # Se deu erro em um dos valores do caso, continua para o proximo caso antes de passar para o proximo valor do caso atual
            if (flag_erro):
                break        
        
        if (not flag_erro):

            # Verifica se mesmo depois de acabar o caso de teste ficou faltando fazer a última transição do APD, ou seja, retirar o fundo da pilha (F)
            # Se sim, desempilha o "F" da pilha e realiza a transição
            for estado in estados:
                if (estado_atual == estado.nome):
                    if (pilha[0] == 'F'): # Verifica se sobrou apenas o fundo de pilha na pilha
                        for trans in range(len(estado.transicoes)):
                            for valorP in estado.transicoes[trans].valores:
                                # Verificação da transição de desempilhar o fundo da pilha
                                if (valorP.desempilha == 'F' and valorP.le == '\\' and valorP.empilha == '\\'):
                                    estado_atual = estado.transicoes[trans].estado_dest
                                    pilha.pop()

            # Verificação final para ver se o estado atual é um estado final e se a pilha se encontra vazia
            # Se sim, o caso deu certo
            # Se não, deu errado
            for estado in estados:
                if (estado_atual == estado.nome):
                    if (estado.flag_final and len(pilha) == 0):
                        flag_erro = False
                    else:
                        flag_erro = True

                    break
        apd = Alfabeto(alphabet=alfabeto)
        flag_chck = apd.checkIsInAlphabet(caso)

        if(flag_erro or flag_chck == False):
            print("X")
        else:
            print("OK")
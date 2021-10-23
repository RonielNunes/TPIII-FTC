class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\x1b[0m'

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

class AFD:
    def __init__(self, estado_inicial, estados, casos_teste):
        self.estado_inicial = estado_inicial
        self.estados = estados
        self.casos_teste = casos_teste
        pass
        
    def verificaCasosDeTeste(self):
        for caso in self.casos_teste:
            # Reseta o estado atual para o inicial para cada novo caso de teste
            estado_atual    = self.estado_inicial
            flag_erro       = False

            # Percorre os valores do caso atual
            for valor in range(len(caso)):
                
                # Percorre a lista de estados
                for estado in self.estados:

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
            for estado in self.estados:
                if (estado_atual == estado.nome):
                    if (estado.flag_final):
                        flag_erro = False
                    else:
                        flag_erro = True
                    
                    break

            if(flag_erro):
                print(bcolors.FAIL + "X" + bcolors.RESET)
            else:
                print(bcolors.OKGREEN + "OK" + bcolors.RESET)


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

class AFD_ALPHABET(AFD):
    def __init__(self, estado_inicial, estados, casos_teste, alfabeto):
        super().__init__(estado_inicial, estados, casos_teste)
        self.alfabeto = Alfabeto(alphabet=alfabeto)
    
    def verificaCasosDeTeste(self):
        for caso in self.casos_teste:
            # Reseta o estado atual para o inicial para cada novo caso de teste
            estado_atual    = self.estado_inicial
            flag_erro       = False

            #verifica se o caso bate com o alfabeto se for false encerra o casoe vai para o proximo
            isValid = self.alfabeto.checkIsInAlphabet(caso)

            if(isValid == False):
                print(bcolors.FAIL + "X" + bcolors.RESET)
                continue

            # Percorre os valores do caso atual
            for valor in range(len(caso)):
                
                # Percorre a lista de estados
                for estado in self.estados:

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
            for estado in self.estados:
                if (estado_atual == estado.nome):
                    if (estado.flag_final):
                        flag_erro = False
                    else:
                        flag_erro = True
                    
                    break

            if(flag_erro):
                print(bcolors.FAIL + "X" + bcolors.RESET)
            else:
                print(bcolors.OKGREEN + "OK" + bcolors.RESET)


class AFN(AFD_ALPHABET):
    def __init__(self, estado_inicial, estados, casos_teste, alfabeto):
        super().__init__(estado_inicial, estados, casos_teste, alfabeto)
    
    def verificaCasosDeTeste(self):
        
        for caso in self.casos_teste:
            #para cada estado inicial fazemos um teste, se todos falharem nao temos um teste valido
            cont_erro = 0
            
            for estado_in in self.estado_inicial:
                # Reseta o estado atual para o inicial para cada novo caso de teste
                estado_atual    = estado_in
                #flag_erro       = False

                #verifica se o caso bate com o alfabeto se for false encerra o casoe vai para o proximo
                isValid = self.alfabeto.checkIsInAlphabet(caso)

                if(isValid == False):
                    #print(bcolors.WARNING + "is not valid" + bcolors.RESET)
                    cont_erro += 1
                    continue

                # Percorre os valores do caso atual
                for valor in range(len(caso)):
                    
                    # Percorre a lista de estados
                    for estado in self.estados:

                        # Seleciona o estado do estado atual
                        if (estado_atual == estado.nome):
                            flag_estado_atual_para_ele_mesmo = False
                            # Percorre as transições do estado atual
                            for transicao_index in range(len(estado.transicoes)):
                                #tratamento de lambda
                                for valor_index in range(len(estado.transicoes[transicao_index].valores)): #vetor para percorrer os valores que estão no vetor de valores
                                    if(estado.transicoes[transicao_index].valores[valor_index] == '/'): #Verificação para ver se há lambdas na transicao
                                        estado_atual = estado.transicoes[transicao_index].estado_dest #vai para o estado de destino com transição lambda
                                        break
                                # Se encontra uma transição com o caracter do estado atual, troca de estado atual
                                if (caso[valor] in estado.transicoes[transicao_index].valores):
                                    if (estado_atual == estado.transicoes[transicao_index].estado_dest):
                                        flag_estado_atual_para_ele_mesmo = True
                                        continue
                                    
                                    else:
                                        estado_atual = estado.transicoes[transicao_index].estado_dest
                                        break                                
                                # Se no final das transições não encontrar nenhuma transição com o mesmo valor e nem lambda, o caso deu errado
                                if(transicao_index == len(estado.transicoes) - 1 and flag_estado_atual_para_ele_mesmo == False):
                                    #flag_erro = True
                                    cont_erro += 1

                            break # break para sair do for de estados e ir para o próximo valor (estava causando problema pois o estado_atual é alterado dentro do for)

                # Se no final do caso o estado atual for um estado final, o caso deu certo, caso contrário deu errado
                for estado in self.estados:
                    if (estado_atual == estado.nome):
                        if (estado.flag_final == False):
                            cont_erro += 1
                        #     flag_erro = False
                        # else:
                        #     #flag_erro = True
                        
                        break

            # se o cont_erro for do mesmo valor da quantidade de estados iniciais, nenhuma verificacao validou
            #print(cont_erro, len(self.estado_inicial))
            if(cont_erro > 0):
                print(bcolors.FAIL + "X" + bcolors.RESET)
            else:
                print(bcolors.OKGREEN + "OK" + bcolors.RESET)
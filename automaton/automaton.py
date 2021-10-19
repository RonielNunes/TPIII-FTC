

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
                print("X")
            else:
                print("OK")


class Alfabeto:
    def __init__(self, alphabet): #construtor que recebe oos atributos que são vetores ou não
        self.alphabet = alphabet

    def checkIsInAlphabet(self, entry) -> bool:
        isValid = True

        #verifica se eh palavra vazia
        if(len(entry) == 0):
            return False
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
                print("X")
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
                print("X")
            else:
                print("OK")

    

class Fita(object):
    simboloEmBranco = "_"

    def __init__(self, fita_string = ""):
        self.fita = dict((enumerate(fita_string)))
        
    def __str__(self):
        s = ""
        minIndexUsado = min(self.fita.keys()) 
        maxIndexUsado = max(self.fita.keys())
        for i in range(minIndexUsado, maxIndexUsado):
            s += self.fita[i]
        return s
   
    def __getitem__(self,index):
        if index in self.fita:
            return self.fita[index]
        else:
            return Fita.simboloEmBranco

    def __setitem__(self, pos, char):
        self.fita[pos] = char
        
class TuringMachine(object):
    
    def __init__(self, fita = "", simboloEmBranco = "_", estadoInicial = "", estadoFinal = None, funcaoDeTransicao = None):
        self.fita = Fita(fita)
        self.posicaoHead = 0
        self.simboloEmBranco = simboloEmBranco
        self.estadoAtual = estadoInicial
        if funcaoDeTransicao == None:
            self.funcaoDeTransicao = {}
        else:
            self.funcaoDeTransicao = funcaoDeTransicao
        if estadoFinal == None:
            self.estadoFinal = set()
        else:
            self.estadoFinal = set(estadoFinal)
        
    def getFita(self): 
        return str(self.fita)
    
    def passo(self):
        char_cabecote = self.fita[self.posicaoHead]
        # print("char:", char_cabecote)
        x = (self.estadoAtual, char_cabecote)
        # print("x:", x)
        if x in self.funcaoDeTransicao:
            y = self.funcaoDeTransicao[x]
            # print("y:", y)
            self.fita[self.posicaoHead] = y[1]
            if y[2] == "D":
                self.posicaoHead += 1
            elif y[2] == "E":
                self.posicaoHead -= 1
            
            self.estadoAtual = y[0]

    def final(self):
        if self.estadoAtual in self.estadoFinal:
            return True
        else:
            return False
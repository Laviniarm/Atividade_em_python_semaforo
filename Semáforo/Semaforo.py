class Semaforo: 

    def __init__(self, cor :str, tempo:int=0):
        # definindo as propriedades/atributos
        self.cor = cor
        self.tempo = tempo
       
    def getCor(self)->str:
        return self.cor
    
    def getTempo(self)->int:
        return self.tempo

    def setTempo(self, novoTempo: int):
        self.tempo = novoTempo


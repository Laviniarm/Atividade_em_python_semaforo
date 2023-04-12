import time
from Semaforo import Semaforo

verde = Semaforo("Verde") 
amarelo = Semaforo("Amarelo") 
vermelho = Semaforo("Vermelho")

verde.setTempo(2)
amarelo.setTempo(1)
vermelho.setTempo(3)

ciclos = 3

for i in range(ciclos):
    print("\n Semáforo aceso: ", verde.getCor())
    time.sleep(verde.getTempo())
    print("\n Semáforo aceso: ", amarelo.getCor())
    time.sleep(amarelo.getTempo())
    print("\n Semáforo aceso: ", vermelho.getCor())
    time.sleep(vermelho.getTempo())

print("\n Fim do programa")


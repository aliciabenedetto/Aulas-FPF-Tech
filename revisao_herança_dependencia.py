# Herança e Injeção de Dependência - Revisão
#Criar uma classe base "Veiculo" com um método mover(pass)
#Crie uma classe "Motor" que tem um método "ligar" que só faz print ("motor ligado").
#Crie uma Classe Carro que herda de “Veiculo”,
#Além disso, injete uma instância de motor na classe Carro
#Carro terá um método "ligar" que rodara Motor.ligar e depois fará um print "carro andando"

class Veiculo:
   def mover(self):
       pass

class Motor:
   def ligar(self):
       print('motor ligado')

class Carro(Veiculo):
   def __init__(self,motor):
       self.motor = motor
   def mover(self):
       self.motor.ligar()
       print('carro andando')

m = Motor()
c = Carro(m)
c.mover()


        
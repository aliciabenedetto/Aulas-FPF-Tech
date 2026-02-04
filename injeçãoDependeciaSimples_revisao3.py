# Revisão Aula 3: Injeção de Dependência Simples

class Mensagem:
   def enviar(self,texto):
       print(f'Mensagem enviada: {texto}')

class Usuario:
   def __init__(self,msg):
       self.msg = msg


   def notificar(self,txt):
       self.msg.enviar(txt)

m = Mensagem()
u = Usuario(m)
u.notificar('Olá')
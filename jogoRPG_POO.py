import random as rd

class Personagem:
    def __init__(self, nome: str, vida: int, defesa: int, ataque: int):
        self.nome = nome
        self.vida = vida
        self.defesa = defesa
        self.ataque = ataque

    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, alvo):
        dano = max(self.ataque - alvo.defesa, 0)
        alvo.vida -= dano
        return dano

    def fortalecer(self, valor=2):
        self.ataque += valor

    def curar(self, valor=10):
        self.vida = min(self.vida+valor, 100)


class jogoRPG:
    def __init__(self):
        nome_player = input('Qual o seu nome?')
        self.player = Personagem(nome_player, 100, 10, 10)
        self.inimigo = Personagem('boss', 100, 10, 10)

    def iniciar(self):
        print(f'batalha entre {self.player.nome} e {self.inimigo.nome}!')
        while self.player.esta_vivo() and self.inimigo.esta_vivo():
            self.turno_jogador()
            self.turno_inimigo()
        self.finalizar_jogo()

    def turno_jogador(self):
        print(f' {self.player.nome} : {self.player.vida} HP | {self.inimigo.nome} : {self.inimigo.vida} HP')
        escolha = input('Ação [1] Atacar | [2] Fortalecer | [3] Curar \n')
        if escolha == '1':
            dano = self.player.atacar(self.inimigo)
            print(f'{self.player.nome} Atacou em {self.inimigo.nome} e causou {dano} de dano')
        elif escolha == '2':
            valor_dado = rd.randint(1, 10)
            self.player.fortalecer(valor_dado)
            print(f'{self.player.nome} aumentou seu ataque em {valor_dado} !')
        elif escolha == '3':
            valor_curar = rd.randint(1, 10)
            self.player.curar(valor_curar)
            print(f'{self.player.nome} se curou em {valor_curar} de vida')
        else:
           print('escolha um valor valido')

    def turno_inimigo(self):
        escolha = rd.choice(['Atacar', 'Fortalecer', 'Curar'])
        match escolha:
            case 'Atacar':
                dano = self.inimigo.atacar(self.player)
                print(f'{self.inimigo.nome} Atacou em {self.player.nome} e causou {dano} de dano')
                # self.inimigo.atacar(self.player)
            case 'Fortalecer':
                valor_forca = rd.randint(1, 10)
                self.inimigo.fortalecer(valor_forca)
                print(f'Inimigo se fortaleceu em {valor_forca}')
            case 'Curar':
                valor_cura = rd.randint(1, 10)
                self.inimigo.curar(valor_cura)
                print(f'Inimigo se curou em {valor_cura}')

    def finalizar_jogo(self):
        print(f'{self.player.nome} perdeu') \
            if not self.player.esta_vivo() \
            else print(f'Parabéns {self.player.nome} você ganhou')


if __name__ == '__main__':
   jogo = jogoRPG()
   jogo.iniciar()
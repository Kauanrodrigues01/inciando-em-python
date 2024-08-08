import random

class NPC:
    def __init__(self, nome, time, forca, municao, defesa, agilidade):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.defesa = defesa
        self.agilidade = agilidade
        self.energia = 100
        self.vivo = True
        self.experiencia = 0
        self.nivel = 1
        self.inventario = []
        self.status = []

    def info(self):
        print(f'Nome......: {self.nome}')
        print(f'Time......: {self.time}')
        print(f'Força.....: {self.forca}')
        print(f'Munição...: {self.municao}')
        print(f'Defesa....: {self.defesa}')
        print(f'Agilidade.: {self.agilidade}')
        print(f'Energia...: {self.energia}')
        print(f'Experiência: {self.experiencia}')
        print(f'Nível.....: {self.nivel}')
        print(f'Inventário: {self.inventario}')
        print(f'Status....: {self.status}')
        print('Vivo......: Sim' if self.vivo else 'Vivo......: Não')
        print('-' * 30)

    def trocar_time(self, novo_time):
        self.time = novo_time

    def treinar(self):
        if self.energia >= 10:
            self.forca += 5
            self.energia -= 10
        else:
            print(f'{self.nome} está muito cansado para treinar!')

    def atirar(self, alvo):
        if self.municao > 0:
            self.municao -= 1
            self.energia -= 5
            if random.random() < (self.agilidade / 100):  # Chance de acertar baseada na agilidade
                dano = max(0, self.forca - alvo.defesa)
                alvo.receber_dano(dano)
                print(f'{self.nome} acertou {alvo.nome} causando {dano} de dano!')
            else:
                print(f'{self.nome} errou o tiro em {alvo.nome}!')
        else:
            print('Munição esgotada!')

    def carregar(self):
        self.municao = 100
        print(f'{self.nome} recarregou a munição.')

    def receber_dano(self, dano):
        self.energia -= dano
        if self.energia <= 0:
            self.vivo = False
            self.energia = 0
            print(f'{self.nome} morreu!')

    def curar(self, quantidade):
        if self.vivo:
            self.energia += quantidade
            if self.energia > 100:
                self.energia = 100
            print(f'{self.nome} foi curado e agora tem {self.energia} de energia.')
        else:
            print(f'{self.nome} está morto e não pode ser curado.')

    def ganhar_experiencia(self, pontos):
        self.experiencia += pontos
        if self.experiencia >= 100:
            self.nivel += 1
            self.experiencia -= 100
            self.forca += 10
            self.defesa += 5
            self.agilidade += 3
            print(f'{self.nome} subiu para o nível {self.nivel}!')

    def adicionar_item(self, item):
        self.inventario.append(item)
        print(f'{self.nome} recebeu {item}.')

    def usar_item(self, item):
        if item in self.inventario:
            self.inventario.remove(item)
            if item == 'kit de primeiros socorros':
                self.curar(50)
            elif item == 'munição extra':
                self.carregar()
            print(f'{self.nome} usou {item}.')
        else:
            print(f'{self.nome} não possui {item} no inventário.')

    def adicionar_status(self, status):
        self.status.append(status)
        print(f'{self.nome} está agora com status {status}.')

    def remover_status(self, status):
        if status in self.status:
            self.status.remove(status)
            print(f'{status} removido de {self.nome}.')

class Soldado(NPC):
    def __init__(self, nome, time):
        super().__init__(nome, time, forca=200, municao=200, defesa=50, agilidade=60)

    def habilidade_especial(self, alvo):
        if self.energia >= 20:
            self.energia -= 20
            dano = self.forca * 2
            alvo.receber_dano(dano)
            print(f'{self.nome} usou habilidade especial causando {dano} de dano em {alvo.nome}!')
        else:
            print(f'{self.nome} não tem energia suficiente para usar a habilidade especial!')

class Guarda(NPC):
    def __init__(self, nome, time):
        super().__init__(nome, time, forca=100, municao=20, defesa=30, agilidade=40)

    def habilidade_especial(self, alvo):
        if self.energia >= 20:
            self.energia -= 20
            dano = self.forca * 1.5
            alvo.receber_dano(dano)
            alvo.adicionar_status('atordoado')
            print(f'{self.nome} usou habilidade especial causando {dano} de dano e atordoando {alvo.nome}!')
        else:
            print(f'{self.nome} não tem energia suficiente para usar a habilidade especial!')

class Elite(NPC):
    def __init__(self, nome, time):
        super().__init__(nome, time, forca=400, municao=500, defesa=70, agilidade=80)

    def habilidade_especial(self, alvo):
        if self.energia >= 30:
            self.energia -= 30
            dano = self.forca * 2.5
            alvo.receber_dano(dano)
            print(f'{self.nome} usou habilidade especial causando {dano} de dano em {alvo.nome}!')
        else:
            print(f'{self.nome} não tem energia suficiente para usar a habilidade especial!')

class Missao:
    def __init__(self, descricao, recompensa):
        self.descricao = descricao
        self.recompensa = recompensa
        self.concluida = False

    def concluir(self, npc):
        if not self.concluida:
            npc.ganhar_experiencia(self.recompensa)
            self.concluida = True
            print(f'Missão concluída! {npc.nome} ganhou {self.recompensa} de experiência.')
        else:
            print('Missão já foi concluída.')

# Exemplo de uso
s1 = Soldado('Olho Vivo', 1)
s2 = Guarda('Bala na Agulha', 2)
s3 = Elite('Ninja', 1)
s4 = Soldado('Arqueiro', 2)
s5 = Guarda('Silent', 1)
s6 = Elite('Samurai', 2)

s1.info()
s2.info()

s1.atirar(s2)
s2.info()

s2.treinar()
s2.info()

s1.ganhar_experiencia(120)
s1.info()

s1.adicionar_item('kit de primeiros socorros')
s1.usar_item('kit de primeiros socorros')

s1.adicionar_item('munição extra')
s1.usar_item('munição extra')

s1.habilidade_especial(s2)
s2.info()

missao = Missao('Derrotar 3 inimigos', 50)
missao.concluir(s1)
s1.info()
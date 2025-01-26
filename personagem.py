import random
from colorama import Fore, Style

class Personagem:
    """Classe que representa um personagem genérico"""
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    @property
    def nome(self):
        return self.__nome

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, valor):
        self.__vida = valor

    @property
    def nivel(self):
        return self.__nivel

    def mostrar_detalhes(self):
        return f"""
        Nome: {Fore.CYAN + Style.BRIGHT}{self.nome}
        Vida: {Fore.GREEN + Style.BRIGHT}{self.vida}
        Nível: {Fore.YELLOW + Style.BRIGHT}{self.nivel}
        """

    def atacar(self, alvo):
        dano = random.randint(self.nivel * 2, self.nivel * 4)
        alvo.receber_ataque(dano)
        self.exibir_mensagem_ataque(alvo.nome, dano, alvo.vida)
        return dano

    def receber_ataque(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0

    def exibir_mensagem_ataque(self, nome_alvo, dano, vida_alvo):
        print(f"{Fore.RED + Style.BRIGHT}{self.nome} atacou {nome_alvo} e causou {dano} de dano! A Vida do {nome_alvo} é de {vida_alvo}")

    def ataque_especial(self, alvo):
        dano = random.randint(self.nivel * 4, self.nivel * 7)
        alvo.receber_ataque(dano)
        self.exibir_mensagem_ataque(alvo.nome, dano, alvo.vida)
        return dano

class Heroi(Personagem):
    """Classe que representa um herói"""
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    @property
    def habilidade(self):
        return self.__habilidade

    def mostrar_detalhes(self):
        return f'{super().mostrar_detalhes()} Habilidade: {Fore.MAGENTA + Style.BRIGHT}{self.habilidade}'

    def ataque_especial(self, alvo):
        dano = super().ataque_especial(alvo)
        print(f"{Fore.BLUE + Style.BRIGHT}{self.nome} usou sua habilidade especial {self.habilidade}!")
        return dano

class Vilao(Personagem):
    """Classe que representa um vilão"""
    def __init__(self, nome, vida, nivel, especie):
        super().__init__(nome, vida, nivel)
        self.__especie = especie

    @property
    def especie(self):
        return self.__especie

    def mostrar_detalhes(self):
        return f'{super().mostrar_detalhes()} Espécie: {self.__especie}'

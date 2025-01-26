from personagem import Heroi, Vilao
from colorama import Fore, Style

class GerenciadorDeViloes:
    """Classe para gerenciar a lista de vilões"""
    def __init__(self, viloes):
        self.viloes = viloes
        self.vilao_atual = 0

    def proximo_vilao(self):
        if self.vilao_atual < len(self.viloes):
            vilao = self.viloes[self.vilao_atual]
            self.vilao_atual += 1
            return vilao
        return None

class Combate:
    """Classe orquestradora do jogo"""
    def __init__(self, heroi, gerenciador_de_viloes, desenhar_caixa):
        self.heroi = heroi
        self.gerenciador_de_viloes = gerenciador_de_viloes
        self.desenhar_caixa = desenhar_caixa

    def iniciar_combate(self):
        """Inicia o combate entre herói e vilão entre turnos"""
        self.desenhar_caixa("Início da Batalha", f"{Fore.YELLOW}Pressione ENTER para começar essa partida épica!")
        input()
        vilao = self.gerenciador_de_viloes.proximo_vilao()
        while self.heroi.vida > 0 and vilao:
            self.desenhar_caixa("Batalha Iniciada", f"{Fore.RED}{self.heroi.nome} VS {vilao.nome}!")
            while self.heroi.vida > 0 and vilao.vida > 0:
                detalhes = f"{Fore.MAGENTA}{self.heroi.mostrar_detalhes()}\n{vilao.mostrar_detalhes()}"
                self.desenhar_caixa("Detalhes dos Personagens", detalhes)

                escolha = input(f"{Fore.CYAN}Escolha o que fazer:\n1 - Atacar\n2 - Ataque Especial\n")

                if escolha == '1':
                    self.heroi.atacar(vilao)
                elif escolha == '2':
                    self.heroi.ataque_especial(vilao)
                else:
                    self.desenhar_caixa("Aviso", f"{Fore.RED}Opção inválida. Cuidado com o que escolhe!")

                if vilao.vida <= 0:
                    self.desenhar_caixa("Vitória!", f"{Fore.GREEN}{vilao.nome} foi derrotado!")
                    vilao = self.gerenciador_de_viloes.proximo_vilao()
                    if vilao:
                        self.desenhar_caixa("Próximo Vilão", f"{Fore.BLUE}Prepare-se para o próximo vilão: {vilao.nome}!")
                    break

                vilao.atacar(self.heroi)

            if self.heroi.vida <= 0:
                self.desenhar_caixa("Derrota", f"{Fore.RED}{self.heroi.nome} foi derrotado!")

        if self.heroi.vida > 0:
            self.desenhar_caixa("Parabéns!", f"{Fore.GREEN}Você derrotou todos os vilões!")

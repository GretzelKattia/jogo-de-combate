from personagem import Heroi, Vilao
from combate import Combate, GerenciadorDeViloes
from colorama import init, Fore, Style

init(autoreset=True)

def desenhar_caixa(titulo, conteudo):
    linha = "*" * (len(titulo) + 4)
    print(f"\n{Fore.CYAN + Style.BRIGHT}{linha}\n* {titulo} *\n{linha}")
    print(conteudo)
    print(f"{linha}")

if __name__ == "__main__":
    print(f"{Fore.CYAN + Style.BRIGHT}BEM-VINDO AO JOGO DE COMBATE!")
    nomeHeroi = input("Digite o nome do herói: ")
    habilidadeHeroi = input("Digite o ataque do herói: ")
    heroi1 = Heroi(nomeHeroi, 100, 5, habilidadeHeroi)
    vilao1 = Vilao("Lex Luthor", 80, 4, "Humano")
    vilao2 = Vilao("Coringa", 70, 3, "Humano")
    vilao3 = Vilao("Darkseid", 150, 6, "Alienígena")
    viloes = [vilao1, vilao2, vilao3]
    gerenciador_de_viloes = GerenciadorDeViloes(viloes)
    batalha = Combate(heroi1, gerenciador_de_viloes, desenhar_caixa)
    batalha.iniciar_combate()

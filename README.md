# Jogo de Combate em Turno

## Descrição

Este projeto foi proposto pela Rocketseat no curso de Python. Ele é basicamente um jogo de combate em turnos, onde o jogador controla um herói e luta contra diversos vilões. 
O jogo aplica conceitos de Programação Orientada a Objetos (POO) como herança, encapsulamento, polimorfismo e abstração, 
proporcionando um exemplo prático de como esses pilares podem ser utilizados para criar softwares melhores e mais organizados.

## Programação Orientada a Objetos (POO)

### Definição

A Programação Orientada a Objetos (POO) é um paradigma de programação que utiliza "objetos" para representar dados e métodos. 
Este paradigma promove a organização, modularidade e reutilização do código, facilitando a criação de softwares mais eficientes e fáceis de manter.

### Pilares da POO

1. **Herança**: Permite que uma classe herde atributos e métodos de outra classe, promovendo a reutilização do código e a criação de hierarquias.
2. **Encapsulamento**: Restringe o acesso direto a alguns componentes de um objeto, protegendo a integridade dos dados e prevenindo modificações acidentais.
3. **Polimorfismo**: Permite que objetos de diferentes classes sejam tratados de maneira similar, promovendo a flexibilidade e a extensibilidade do código.
4. **Abstração**: Esconde os detalhes complexos de um sistema, permitindo que os desenvolvedores se concentrem nos aspectos importantes do código.

### Aplicações no Projeto

- **Atributos e Métodos**: Variáveis que armazenam o estado dos objetos e funções que definem seu comportamento.
- **Herança**: `Heroi` e `Vilao` herdam da classe base `Personagem`.
- **Encapsulamento**: Atributos como `nome`, `vida` e `nivel` são encapsulados dentro das classes.
- **Polimorfismo**: Métodos como `atacar` e `mostrar_detalhes` permitem que objetos de diferentes classes sejam tratados de maneira uniforme.
- **Abstração**: A classe base `Personagem` fornece uma interface abstrata para classes derivadas.

## Estrutura do Projeto

```plaintext
jogo_combate_turno/
│
├── personagem.py  # Define as classes Personagem, Heroi e Vilao
│
├── combate.py     # Define as classes GerenciadorDeViloes e Combate
│
└── main.py        # Ponto de entrada do programa
```

### Conteúdo das Classes

1. **personagem.py**
   - `Personagem`: Classe base para os personagens do jogo.
   - `Heroi`: Classe derivada representando o herói controlado pelo jogador.
   - `Vilao`: Classe derivada representando os vilões adversários.

2. **combate.py**
   - `GerenciadorDeViloes`: Classe para gerenciar a lista de vilões.
   - `Combate`: Classe que gerencia o fluxo do jogo e a lógica de combate em turnos.

3. **main.py**
   - Ponto de entrada do programa. Instancia as classes e inicia a batalha.

## Instruções de Uso

1. Clone este repositório.
2. Navegue até o diretório do projeto.
3. Execute o arquivo `main.py` para iniciar o jogo.

## Exemplo de Uso

```plaintext
***************************
* Início da Batalha *
***************************
Pressione ENTER para começar essa partida épica!
***************************

***************************
* Detalhes dos Personagens *
***************************
Nome: Superman
Vida: 100
Nível: 5
Habilidade: Super Força

Nome: Lex Luthor
Vida: 80
Nível: 4
Espécie: Humano
***************************

Escolha o que fazer:
1 - Atacar
2 - Ataque Especial

Superman atacou Lex Luthor e causou 15 de dano! A Vida do Lex Luthor é de 65
...

***************************
* Parabéns! *
***************************
Você derrotou todos os vilões!
***************************
```

## Referências

- [Documentação do Python](https://docs.python.org/3/)
- [Guia de POO](https://realpython.com/python3-object-oriented-programming/)
- [Colorama Documentation](https://pypi.org/project/colorama/)

  ---

<p align="center">
  Feito com 💜 pela Gretzel Kattia
</p>

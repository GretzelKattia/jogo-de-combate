## Aprendizados Adicionais

### Utilização de Cores no Console

Para deixar as mensagens no console mais atraentes, utilizamos a biblioteca `colorama` para adicionar cores. Aqui está um exemplo de como usar essa biblioteca:

1. Instale a biblioteca `colorama`:

```bash
pip install colorama
```

2. Importe e inicialize a `colorama` no seu código:

```python
from colorama import init, Fore, Style

init(autoreset=True)
```

3. Utilize as constantes `Fore` e `Style` para adicionar cores e estilos às suas mensagens:

```python
print(f"{Fore.CYAN + Style.BRIGHT}Esta é uma mensagem colorida!")
```

### Decorador `@property` em Python

O decorador `@property` em Python permite que um método de uma classe seja acessado como um atributo. Isso significa que, ao invés de chamar o método com parênteses como uma função, você pode acessá-lo diretamente como uma variável. 

#### Exemplo:

```python
class Personagem:
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida

    @property
    def nome(self):
        return self.__nome

    @property
    def vida(self):
        return self.__vida
```

Com isso, você pode acessar `nome` e `vida` como atributos, sem usar parênteses:

```python
personagem = Personagem("Superman", 100)
print(personagem.nome)  # Acessa o método como um atributo
print(personagem.vida)  # Acessa o método como um atributo
```

### Declarando a Função `main`

A função `main` em Python é usada para definir o ponto de entrada do programa. Aqui está uma explicação detalhada de como declarar e utilizar a função `main`.

1. **Defina a Função `main`**:

```python
def main():
    # Código principal do programa
    print("Hello, World!")
```

2. **Verifique se o Script está sendo Executado Diretamente**:

Adicione a verificação `if __name__ == "__main__":` para garantir que o código dentro dela seja executado apenas quando o script for executado diretamente, e não quando for importado como um módulo.

```python
if __name__ == "__main__":
    main()
```

### Exemplo Completo:

```python
def main():
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}! Bem-vindo ao jogo.")

if __name__ == "__main__":
    main()
```
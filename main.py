
## Comando print serve para inscrever algo no console. Essa função é boa para ser usada para debugar
print("Olá mundo!!")

## Quando colocado o sep na função print ele é servira para separar as frases pelo significado eu determinamos, no nosso caso por barra.
## Para o Python quando colocado uma virgula em uma função Print é considerado  como concatenação.
print('O Brasil', 'ganhou', 5, 'títulos mundiais', sep="/")

## Função help no console é uma função que nos auxilia a descobrir para que serve alguma função. Para declarar essa função deve colocar help parênteses e em frente se coloca
## a função que quer descobri.
## Por exemplo help(print).

## VARIAVEIS
## No Python, não é preciso retornar um tipo de variável, é sempre determinado pelo tipo que a variável ira retorna.

## para determinar uma variável String colocamos o valor da variável com aspas, e essa variável só recebe tipo CHAR.
pais = "Itália"

## Para descobrir o tipo de variável que está nos retornando utilizamos a função TYPE
type(pais)

## Para tipos inteiros basta retornar um valor sem ser decimal, não retornar número com números após a virgulas
quantidade = 4

## Para retornar uma variável decimal retornamos um número com números após a virgula
GolsPorPartidas = 3.5

## Para declarar uma variável booleana declaramos colocando como verdadeiro ou falso as variáveis
## Para declarar como verdadeiro ou falso declaramos com letras maiúsculas.
enforcou = True

## A função INPUT recebe oq vai ser impresso no console. Para receber esses parâmetros ou trabalhar com o mesmo é indicado que faça receber esse parâmetro em uma variável.
num = input('Digite um número')

## Utilizamos o método main quando queremos declarar que será a função principal.
if(__name__ == "__main__"):
    print('Teste')

## No python tem uma função que procura uma palavra ou uma letra dentro de uma string
pais.find("a")

## Remove os espaços no início e no final da string, esse comando é como o trim().
pais = pais.strip()

# OPEN é um comando para abrir um documento e puxar tudo que tem dentro dele.
arquivo = open("palavras.txt", "r")

## Para criar uma variável array pasta criar com dois colchetes
palavras = []

# Comando append server para adicionar um novo campo ao array
palavras.append(palavras)

## Comando para fechar o documento.
arquivo.close()

## Random é um comando para mesclar as palavras, fazer uma bagunça.
numero = random.randrange(0, len(palavras))

## Aqui pegamos as palavras e colocamos em maiusculas
palavra_secreta = palavras[numero].upper()


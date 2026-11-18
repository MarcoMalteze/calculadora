
# Função que transforma uma letra ou número no seu valor correspondente
def valor_digito(caractere):

    # Todos os símbolos que podem ser usados nas bases
    simbolos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Deixa a letra maiúscula para facilitar a comparação
    caractere = caractere.upper()

    # Percorre os símbolos para encontrar o caractere digitado
    for i in range(len(simbolos)):

        if simbolos[i] == caractere:
            return i

    # Se não encontrar, significa que o caractere é inválido
    return -1


# Função que transforma um valor no símbolo correspondente
def simbolo_digito(valor):

    simbolos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Retorna o símbolo de acordo com a posição do valor
    return simbolos[valor]


# Função que transforma um número de qualquer base para decimal
def base_para_decimal(numero, base):

    decimal = 0
    sinal = 1
    inicio = 0

    # Verifica se o número é negativo
    if numero[0] == "-":
        sinal = -1
        inicio = 1

    # Percorre cada caractere do número digitado
    for i in range(inicio, len(numero)):

        # Descobre o valor de cada caractere
        valor = valor_digito(numero[i])

        # Verifica se o valor existe na base escolhida
        if valor < 0 or valor >= base:
            return None

        # Faz o cálculo para transformar o número em decimal
        decimal = decimal * base + valor

    # Retorna o resultado, mantendo o sinal original
    return decimal * sinal


# Função que transforma um número decimal para outra base
def decimal_para_base(numero, base):

    resultado = ""
    sinal = ""

    # Verifica se o número é negativo
    if numero < 0:
        sinal = "-"
        numero = numero * -1

    # Se o número for zero, já retorna o resultado
    if numero == 0:
        return "0"

    # Continua dividindo até o número chegar a zero
    while numero > 0:

        # Pega o resto da divisão pela base escolhida
        resto = numero % base

        # Adiciona o símbolo encontrado no começo do resultado
        resultado = simbolo_digito(resto) + resultado

        # Divide o número e pega apenas a parte inteira
        numero = numero // base

    # Retorna o resultado junto com o sinal, se tiver
    return sinal + resultado


# Função principal que faz a conversão entre as bases
def converter(numero, base_origem, base_destino):

    # Primeiro transforma o número original em decimal
    decimal = base_para_decimal(numero, base_origem)

    # Se retornar None, significa que o número é inválido
    if decimal is None:
        return None

    # Depois transforma o decimal para a base desejada
    resultado = decimal_para_base(decimal, base_destino)

    return resultado


# Função para o usuário escolher a base que deseja utilizar
def escolher_base():

    print("\nEscolha a base:")
    print("1 - Binário (base 2)")
    print("2 - Octal (base 8)")
    print("3 - Decimal (base 10)")
    print("4 - Hexadecimal (base 16)")
    print("5 - Outra base")

    try:
        # Converte a opção digitada para número inteiro
        opcao = int(input("Opção: "))

    except ValueError:
        # Caso digite letras ou algo que não seja um número
        print("Digite uma opção válida!")
        return -1

    # Cada opção retorna sua respectiva base
    if opcao == 1:
        return 2

    elif opcao == 2:
        return 8

    elif opcao == 3:
        return 10

    elif opcao == 4:
        return 16

    elif opcao == 5:

        try:
            # Permite que o usuário escolha uma base diferente
            base = int(input("Digite a base (2 a 36): "))

        except ValueError:
            # Evita erro caso seja digitado algo que não seja número
            print("Digite uma base numérica!")
            return -1

        # Verifica se a base está dentro do limite permitido
        if base >= 2 and base <= 36:
            return base

        else:
            print("Base inválida!")
            return -1

    else:
        # Caso escolha uma opção que não existe
        print("Opção inválida!")
        return -1


# Função principal, onde o programa começa a funcionar
def main():

    # Mantém o programa rodando até o usuário decidir sair
    while True:

        print("\n==============================")
        print("       CONVERSOR DE BASES")
        print("==============================")

        # Primeiro escolhe de qual base o número vai sair
        print("\nBase de origem:")
        base_origem = escolher_base()

        # Se a escolha for inválida, volta para o começo
        if base_origem == -1:
            continue

        # Depois escolhe para qual base o número será convertido
        print("\nBase de destino:")
        base_destino = escolher_base()

        if base_destino == -1:
            continue

        # Recebe o número que o usuário deseja converter
        numero = input("\nDigite o número que deseja converter: ")

        try:
            # Chama a função que realiza toda a conversão
            resultado = converter(numero, base_origem, base_destino)

        except (ValueError, IndexError):
            # Caso aconteça algum desses erros, considera o número inválido
            resultado = None

        # Se a conversão deu certo, mostra o resultado
        if resultado is not None:

            print("\nResultado:", resultado)

        else:

            print("\nNúmero inválido para a base escolhida!")

        print("\n------------------------------")
        print("Deseja fazer outra conversão?")
        print("1 - Sim")
        print("0 - Sair")

        # Pergunta se o usuário deseja continuar
        continuar = input("Opção: ")

        # Se digitar zero, encerra o programa
        if continuar == "0":
            break

    print("\nPrograma encerrado.")


# Chama a função principal para iniciar o programa
main()
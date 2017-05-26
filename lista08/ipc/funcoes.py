import random

    # lista 1 questão 1
    def imprimir_questao1(n):
        res = ""
        c = 1
        for i in range(n):
            res += c * (str(i + 1) + " ") + "\n"
            c += 1
        return res


# lista 1 questão 2
def imprimir_questao2(n):
    res = ""
    c = 1
    for i in range(n + 1):
        # res += str(i + 1) + "\n"
        for j in range(i):
            res += str(j + 1) + " "
        res += "\n"
    return res


# lista 1 questão 3
def soma_tres(valor1, valor2, valor3):
    res = valor1 + valor2 + valor3
    return res


# lista 1 questao 4
def positivo_negativo(arg):
    if arg > 0:
        res = "P"
    else:
        res = "N"
    return res


# lista 1 questao 5
def soma_imposto(taxaImposto, custo):
    res = (taxaImposto * custo) / 100 + custo
    return res


# lista 1 questão 6 a
def converte_horas(horas, minutos):
    if horas < 12 and horas >= 0:
        tipo = "A"
    else:
        tipo = "P"
        horas -= 12

    horario = [horas, minutos, tipo]

    return horario


# lista 1 questão 6 b
def saida(horario):
    print(horario)
    if horario[2] == "A":
        horario[2] = "AM"
    else:
        horario[2] = "PM"
    res = str(horario[0]) + ":" + str(horario[1]) + " " + horario[2]

    return res


# lista 1  questao 7
def contaDigito(n):
    cont = 1
    while n // 10 > 0:
        n //= 10
        cont += 1

    return cont


# lista 1 questao 8
def reverte(n):
    invertido = 0
    var = contaDigito(n) - 1
    while var >= 0:
        invertido += (n % 10) * 10 ** var
        var -= 1
        n //= 10
    return invertido


# lista 1 questao 9
def jogar_dados():
    dados = [random.randint(1, 6), random.randint(1, 6)]
    dados = dados[0] + dados[1]
    return dados


# lista 1 questao 9
def jogar_jogo(dados, cont, pontos):
    while True:

        if cont == 0:

            if (4 <= dados <= 6 or 8 <= dados <= 10):
                pontos = dados
                return pontos
            elif ((dados == 7 or dados == 11) or (dados == pontos and cont > 0)):
                print("natural. ganhou")
                exit()
            else:
                print("perdeu")
                exit()
        else:
            if dados == 7:
                print("perdeu")
                exit()

            else:
                if dados == pontos:
                    print("ganhou")
                    exit()
                else:
                    return pontos
        cont += 1

# lista 1 questao 10
def data_mes_extenso(data):

    data = data.split("/")

    if len(data) != 3:
        mes_extenso = None
    elif int(data[0]) < 0 or int(data[0]) > 31:
        mes_extenso = None
    elif int(data[1]) < 0 or int(data[1]) > 12:
        mes_extenso = None

    else:

        meses = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ]

        mes_extenso = str(data[0]) + " de " + meses[int(data[1])-1] + " de " + data[2]

    return mes_extenso

# lista 1 questao11
def embaralha(nome):
    palavra=""
    nome.lower()
    a=list(range(0,len(nome)))
    while a[0]==0:
        random.shuffle(a)
    for i in a:
        palavra+=nome[i]
    return palavra


# Calculo IMC
def imc():

    p = float(input('Informe seu Peso(Kg):'))
    h = float(input('Informe sua Altura(m):'))

imc()

#calculo fatorial
def fatorial(num):
    i = num
    while i > 1:

        i -= 1
        num *= i

    return num

x = int(input("Insira um número para caluclar o fatorial: "))

print ('fatorial: ', fatorial(x))


# Calculadora de Média utilizando pesos diferentes para cada nota

nota_1 = int(input('Insira a primeira nota: '));
pesoNota_1 = int(input('Insira o peso da nota 1: '))
nota_2 = int(input('Insira a segunda nota: '));
pesoNota_2 = int(input('Insira o peso da nota 1: '))

media = float;
nota_1 *= pesoNota_1;
nota_2 *= pesoNota_2;

media = (nota_1 + nota_2) / (pesoNota_1 + pesoNota_2);

print("Media Final: ", media)


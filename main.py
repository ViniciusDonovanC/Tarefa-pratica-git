# Calculo IMC
def imc():
    p = float(input('Informe seu Peso(Kg):'))
    h = float(input('Informe sua Altura(m):'))

    x = p / (h*h)

    return print(f'Seu IMC é {x}')


imc()

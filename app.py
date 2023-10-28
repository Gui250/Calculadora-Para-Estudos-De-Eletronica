
def menu(): 
    print("""

    ****************************************
    Calculadora para os estudos de eletrônica
    ****************************************
          
    [1] Para calcular resistores em série
    [2] Para calcular resistores em paralelo
""")
    opcao = int(input("Digite uma opção: "))
    if(opcao == 1): 
        resistores_em_serie()
    else: 
        resistores_em_paralelo()



def resistores_em_paralelo(): 
    resistor1 = float(input("Digite o valor do primeiro resistor: "))
    resistor2 = float(input("Digite o valor do segundo resistor: "))

    calculo = (resistor1 * resistor2) / (resistor1 + resistor2)
    print(f'O calculo dos resistores paralelos é: {calculo:.2f}')






def resistores_em_serie(*numeros):
    quantidade_resistores = int(input("Digite a quantidade de resistores em série: "))
    auxiliar = []

    for i in range(quantidade_resistores):
        numeros = float(input("Digite o valor de cada resistor: ")) 
        auxiliar.append(numeros)
        soma = sum(auxiliar)
        










    print(f'A soma dos resistores em série é: {soma:.2f}')

def main(): 
    menu()





main()
 
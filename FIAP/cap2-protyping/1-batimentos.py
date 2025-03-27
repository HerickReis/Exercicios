"""
1 - Verificar se os batimentos cardíacos por minuto se encontram na faixa adequada. Para isso, você deve solicitar ao usuário que informe o seu número de BATIMENTOS POR MINUTO (BPM) e a IDADE. 
A partir disso, o script deve verificar e exibir uma mensagem informando se os batimentos do usuário encontram-se DENTRO da faixa adequada, ACIMA da faixa adequada ou ABAIXO
da faixa adequada.
"""

batimentos = int(input("Insira seu BPM atual: "))
idade = int(input("Insira sua idade: "))

if idade <= 2 :
    if batimentos >= 120 and batimentos <= 140:
        print("Normal")
    elif batimentos < 120:
        print("Baixo")
    else:
        print("Alto")


elif idade >= 8 and idade <= 17:
    if batimentos >= 80 and batimentos <= 100:
        print("Normal")
    elif batimentos < 80:
        print("Baixo")
    else:
        print("Alto")

elif idade >= 18 and idade <= 65:
    if batimentos >= 70 and batimentos <= 80:
        print("Normal")
    elif batimentos < 70:
        print("Baixo")
    else:
        print("Alto")
        

elif idade >= 65:
    if batimentos >= 50 and batimentos <= 60:
        print("Normal")
    elif batimentos < 50:
        print("Baixo")
    else:
        print("Alto")


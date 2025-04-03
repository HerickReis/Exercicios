"""
2 - Viajar é bom demais! Uma agência de viagens está propondo uma estratégia para alavancar as vendas após os impactos da pandemia do coronavírus.
A empresa ofertará descontos progressivos na compra de pacotes, dependendo do número de viajantes que estão no mesmo grupo e moram na mesma residência.
Para ajudar a tornar esse projeto real, você deve criar um algoritmo que receba o VALOR BRUTO do pacote, a CATEGORIA DOS ASSENTOS no voo e a QUANTIDADE DE VIAJANTES que moram
em uma mesma casa e calcule os descontos de acordo com a tabela abaixo:

Econômica
2 viajantes -> 3%
3 viajantes -> 4%
4 viajantes ou mais -> 5%
----------------------------------------------------------------------------------------------------------------
Executiva
2 viajantes -> 5%
3 viajantes -> 7%
4 viajantes ou mais -> 8%
----------------------------------------------------------------------------------------------------------------
Primeira classe
2 viajantes -> 10%
3 viajantes -> 15%
4 viajantes ou mais -> 20%

"""

valor_bruto = float(input("Insira o valor bruto do pacote: "))
categoria = input("Insira a categoria dos assentos: ")
viajantes = int(input("Insira a quantidade de viajantes: "))


if categoria == "Econômica":
    if viajantes == 2:
        desconto = valor_bruto * 0.03
    elif viajantes == 3:
        desconto = valor_bruto * 0.04
    elif viajantes >= 4:
        desconto = valor_bruto * 0.05

elif categoria == "Executiva":
    if viajantes == 2:
        desconto = valor_bruto * 0.05
    elif viajantes == 3:
        desconto = valor_bruto * 0.07
    elif viajantes >= 4:
        desconto = valor_bruto * 0.08

elif categoria == "Primeira classe":
    if viajantes == 2:
        desconto = valor_bruto * 0.10
    elif viajantes == 3:
        desconto = valor_bruto * 0.15
    elif viajantes >= 4:
        desconto = valor_bruto * 0.20

valor_final = valor_bruto - desconto
print(f"O valor da viajem é de R${valor_bruto:.2f}")
print(f"O desconto aplicado foi de R${desconto:.2f}")
print(f"O valor final do pacote é de R${valor_final:.2f}")
print(f"O valor médio por viajante é de R${valor_final/viajantes:.2f}")

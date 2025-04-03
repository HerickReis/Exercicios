"""
1 - Você deve elaborar um algoritmo implementado em Python em que o usuário informe quantos alimentos consumiu naquele dia e 
depois possa informar o número de calorias de cada um dos alimentos. 
Como nao estudamos listas neste capitulo, você nao deve se preocupar em armazenar todas as calorias digitadas, mas deve exibir o total de calorias no final.
"""

calorias_consumidas = []

quantidade_alimentos = int(input("Por favor, informe quantos alimentos você consumiu hoje: "))


for c in range(quantidade_alimentos):
    
    calorias = float(input("Calorias: "))
    calorias_consumidas.append(calorias)

total = sum(calorias_consumidas)
    
print(f"Foi consumido um total de {total} calorias")

"""
3 - Hora de decidir! Os colaboradores da sua equipe foram sorteados para ganhar um console de última geração, cada um, em razão do bom desempenho que tiveram nos últimos projetos. Por
uma questão de logística, porém, a empresa pede que todos os cinco membros da equipe recebam o mesmo aparelho.
Crie um algoritmo em que o usuário possa digitar o voto de cada um dos 5 membros da equipe e, ao final, exiba qual foi o console escolhido e com quantos votos.
As opções são: PLAYSTATION, XBOX e NINTENDO.
"""

votos = 0
playstation = 0
xbox = 0
nintendo = 0

while votos < 5:
    voto = int(input("""Vote no console:
        1 - Playstation
        2 - Xbox
        3 - Nintendo
        Digite o voto: """))
    
    if voto == 1:
        playstation += 1
    elif voto == 2:
        xbox += 1
    elif voto == 3:
        nintendo += 1
    else:
        print("Opção inválida.")
    
    votos += 1


maximo = max([playstation, xbox, nintendo])

if playstation == maximo:
    print(f"Playstation ganhou com {playstation} votos.")
elif xbox == maximo:
    print(f"Xbox ganhou com {xbox} votos.")
elif nintendo == maximo:
    print(f"Nintendo ganhou com {nintendo} votos.")

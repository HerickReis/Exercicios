"""

# 1️⃣ Desafio Classificador de nível de Herói

**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões

## Objetivo

Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

Se XP for menor do que 1.000 = Ferro
Se XP for entre 1.001 e 2.000 = Bronze
Se XP for entre 2.001 e 5.000 = Prata
Se XP for entre 5.001 e 7.000 = Ouro
Se XP for entre 7.001 e 8.000 = Platina
Se XP for entre 8.001 e 9.000 = Ascendente
Se XP for entre 9.001 e 10.000= Imortal
Se XP for maior ou igual a 10.001 = Radiante

## Saída

Ao final deve se exibir uma mensagem:
"O Herói de nome **{nome}** está no nível de **{nivel}**"
"""

nome_heroi = input("Digite o nome do herói: ")
xp_heroi = 0
nivel = ""

while True:
    input("Enter:")
    
    if xp_heroi < 1000:
        xp_heroi += 1001
        nivel = "Ferro"
        
    elif 1000 <= xp_heroi <= 2000:
        xp_heroi += 1001
        nivel = "Bronze"
        
    elif 2001 <= xp_heroi <= 5000:
        xp_heroi += 3001
        nivel = "Prata"
        
    elif 5001 <= xp_heroi <= 7000:
        xp_heroi += 2001
        nivel = "Ouro"
        
    elif 7001 <= xp_heroi <= 8000:
        xp_heroi += 1001
        nivel = "Platina"
        
    elif 8001 <= xp_heroi <= 9000:
        xp_heroi += 1001
        nivel = "Ascendente"
        
    elif 9001 <= xp_heroi <= 10000:
        xp_heroi += 1001
        nivel = "Imortal"
        
    else:
        nivel = "Radiante"
            
    print(f"\nO Herói de nome **{nome_heroi}** está no nivel de **{nivel}**") 

    if nivel == "Radiante":
        break     

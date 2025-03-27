""" 2️⃣ Calculadora de partidas Rankeadas

**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões
- Funções

## Objetivo:

Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

Se vitórias for menor do que 10 = Ferro
Se vitórias for entre 11 e 20 = Bronze
Se vitórias for entre 21 e 50 = Prata
Se vitórias for entre 51 e 80 = Ouro
Se vitórias for entre 81 e 90 = Diamante
Se vitórias for entre 91 e 100= Lendário
Se vitórias for maior ou igual a 101 = Imortal

## Saída

Ao final deve se exibir uma mensagem:
"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**" """

def points_calulator(vitorias=0, derrotas=0):
    return vitorias - derrotas
    

def ranks(points):
    rank = ""
    
    if points <= 10:
        rank = "Ferro"
    elif points >= 11 and points <= 20:
        rank = "Bronze"
    elif points >= 21 and points <= 50:
        rank = "Prata"
    elif points >= 51 and points <= 80:
        rank = "Ouro"
    elif points >= 81 and points <= 90:
        rank = "Diamante"
    elif points >= 91 and points <= 100:
        rank = "Lendário"
    elif points >= 101:
        rank = "Imortal"
       
    return rank

pontos_de_vitoria = points_calulator(900, 30)

ranking = ranks(pontos_de_vitoria)

print(f"O Herói tem de saldo de **{pontos_de_vitoria}** está no nível de **{ranking}**")

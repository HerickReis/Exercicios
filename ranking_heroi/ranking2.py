nome_heroi = input("Digite o nome do herói: ")
xp_heroi = int(0)
nivel = str("")

rankings = {"Ferro": {"min":0, "max":1000},
    "Bronze": {"min": 1001, "max": 2000},
    "Prata": {"min":2001, "max":5000},
    "Ouro": {"min": 5001, "max":7000},
    "Platina": {"min": 7001, "max": 8000},
    "Ascendente": {"min": 8001, "max": 9000},
    "Imortal": {"min": 9001, "max": 10000},
    "Radiante": {"min": 10001, "max": float("inf")}
}

def ganhar_1000(xp):
    return int(xp + 1000)
        
while True:
    for ranking, valores in rankings.items():
        if valores["min"] <= xp_heroi <= valores["max"]:
            nivel = ranking
            break
        
    xp_heroi = ganhar_1000(xp_heroi)
        
    print(f"\nO Herói de nome **{nome_heroi}** está no nivel de **{nivel}**")    
    input("Enter:")

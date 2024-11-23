pokedex = {}


nome_pokemon = input("Digite o nome do pokemon: ")
nivel_pokemon = input("Digite o nivel do pokemon: ")
sexo_pokemon = input("Digite o sexo do pokemon: ")
vida_pokemon = input("Digite a vida do pokemon: ")
elemento_pokemon = input("Digite o elemento do pokemon: ")

pokedex[nome_pokemon] = {
    "nivel": nivel_pokemon,
    "sexo": sexo_pokemon,
    "vida": vida_pokemon,
    "elemento": elemento_pokemon
}

print(f"{nome_pokemon.upper()} cadastrado com sucesso!")

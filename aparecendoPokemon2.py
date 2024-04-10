import random
import time

pokemons = ['Pikachu', 'Charmander', 'Squirtle', 'Bulbasaur', 'Eevee']

def explorar_ambiente(ambiente):
    print("Explorando", ambiente , "...")
    if random.random() < 0.3:  
        pokemon = random.choice(pokemons)
        print(f"Um {pokemon} selvagem apareceu!")
        capturar = input("Deseja tentar capturar o Pokémon? (sim/não): ")
        if capturar.lower() == 'sim':
            if random.random() < 0.7: 
                print("Você capturou", pokemon)
                return pokemon
            else:
                print("O Pokémon escapou!")
        else:
            print("Você decidiu não capturar o Pokémon.")
    else:
        print("Nenhum Pokémon apareceu desta vez.")
    return None

capturados = []
pokebolas = 10
while True:
    sairDoMatoCaverna = False
    andando = True
    if sairDoMatoCaverna:
        break
    elif andando:
        print("andando...")
        ambiente = random.choice(['matos altos', 'caverna'])
        pokemon_capturado = explorar_ambiente(ambiente)
        if pokemon_capturado:
            capturados.append(pokemon_capturado)
    time.sleep(1)



print("Pokémon capturados durante sua aventura:")
for pokemon in capturados:
    print(pokemon)

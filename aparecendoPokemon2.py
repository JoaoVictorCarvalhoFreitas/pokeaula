import random
import time

# Lista de Pokémon que podem aparecer
pokemons = ['Pikachu', 'Charmander', 'Squirtle', 'Bulbasaur', 'Eevee']

# Função para simular a exploração
def explorar_ambiente(ambiente):
    print("Explorando", ambiente , "...")
    if random.random() < 0.3:  # 30% de chance de encontrar um Pokémon
        pokemon = random.choice(pokemons)
        print(f"Um {pokemon} selvagem apareceu!")
        capturar = input("Deseja tentar capturar o Pokémon? (sim/não): ")
        if capturar.lower() == 'sim':
            # Simula a captura do Pokémon
            if random.random() < 0.7:  # 70% de chance de sucesso na captura
                print("Você capturou", pokemon)
                return pokemon
            else:
                print("O Pokémon escapou!")
        else:
            print("Você decidiu não capturar o Pokémon.")
    else:
        print("Nenhum Pokémon apareceu desta vez.")
    return None

# Loop principal do jogo
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
    time.sleep(1.5)



# Exibe os Pokémon capturados ao acabar as pokebolas
print("Pokémon capturados durante sua aventura:")
for pokemon in capturados:
    print(pokemon)

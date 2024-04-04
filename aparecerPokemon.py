"""sistema que possibilite o jogador a explorar matos altos e cavernas
 para encontrar pokemons"""



import random
import time

# Lista de Pokémon que podem aparecer
pokemons = ['Pikachu', 'Charmander', 'Squirtle', 'Bulbasaur', 'Eevee']

# Função para simular a exploração
def explorar_ambiente(ambiente):
    print(f"Explorando {ambiente}...")
    if random.random() < 0.55:  # 55% de chance de encontrar um Pokémon
        pokemon = random.choice(pokemons)
        print(f"Um {pokemon} selvagem apareceu!")
        capturar = input("Deseja tentar capturar o Pokémon? (sim/não): ")
        if capturar.lower() == 'sim':
            # Simula a captura do Pokémon
            if random.random() < 0.7:  # 80% de chance de sucesso na captura
                print(f"Você capturou {pokemon}!")
                return pokemon
            else:
                print("O Pokémon escapou!")
        elif capturar.lower() == "nao":
            print("Você decidiu não capturar o Pokémon.")
        else: 
            print("você digitou uma opção invalida e o pokemon fugiu.")
            print("Mais sorte na proxima")
        
    else:
        print("Nenhum Pokémon apareceu desta vez.")
    return None

# Loop principal do jogo
capturados = []
menu = True
while menu:
    print("---- andar = 1 ----")
    print("---- sair  = 2 ----")
    acao = input("digite sua ação: ")
    if acao == "1":
        print("andando...")
        ambiente = random.choice(['matos altos', 'caverna'])
        pokemon_capturado = explorar_ambiente(ambiente)
        if pokemon_capturado:
            capturados.append(pokemon_capturado)    
    else:
        print("Comando inválido. Por favor, digite 'explorar' ou 'sair'.")


# Exibe os Pokémon capturados ao final do jogo
print("Pokémon capturados durante sua aventura:")
for pokemon in capturados:
    print(pokemon)

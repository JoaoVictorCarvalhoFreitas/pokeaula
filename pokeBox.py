#adicionar podemons na box ate o usuario digitar exit.
import random
import time

pokedex_safari = ["Magikarp","Psyduck", "Goldeen", "Dragonair", "Dratini","Seaking","Poliwag","Exeggcute","Rhyhorn","Nidoran F.","Nidoran M","Nidorino","Nidorina","Doduo","Chansey","Kangaskhan","Scyther","Pinsir","Tauros"]



box_pokemon = []
menu = True
posicao_na_box = 0
def aparecendo_pokemon():
   pokemon = random.choice(pokedex_safari)
   box_pokemon.append(pokemon)

while menu:
   print("---- andar = 1 ----")
   print("---- sair  = 2 ----")
   acao = input("digite sua ação: ")
   if acao == "1":
      aparecendo_pokemon()
      print(box_pokemon)
      time.sleep(1)
   elif acao == "2":
      print( )
      break
   else:
      print("opção invalida por favor digite apenas as opções definidas")
      print("tente novamente")
      continue



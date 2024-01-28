print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem-vindo a ilha do tesouro.")
print("Sua missão é encontrar o tesouro.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input("Você está em uma encruzilhada. Qual caminho deseja seguir? 'direita' ou 'esquerda'? ")
direction = direction.lower()
if direction == "esquerda":
  lake = input("Você está diante de um enorme lago. O que deseja fazer? 'nadar' ou 'esperar'? ")
  lake = lake.lower()
  if lake == "esperar":
    boat = input("Um barco aparece sendo guiado por um homem e pergunta:.\n 'Você deseja seguir adiante? 'sim' ou 'não'? ") 
    boat = boat.lower()
    if boat == "sim":
      altar = input("O barco te leva ao centro do lago onde tem três altares com objetos em cima. Uma 'joia', uma 'faca' e uma 'maça'. Qual deles você deseja pegar? ")
      altar = altar.lower()
      if altar == "joia":
        print("Sua ganância foi sua perdição! Você se tornou um Gollon.")
      elif altar == "faca":
        print("Ao pegar a faca, você percebe que era uma faca amaldiçoada. Ela se transforma em uma cobra venenosa e te morde.")
        print("Infelizmente, não há cura para o veneno da faca amaldiçoada. Seu corpo é encontrado dias depois por exploradores. GAME OVER")

      elif altar == "maça":
        print("Seu desejo de sobrevivência sem lutar foi ouvido e saciado. Você encontrou o maior tesouro da ilha!")
      else:
        print("Devido ao frio e a fome por ficar esperando que algo acontecesse, seus ossos foram encontrados por colonizadores dezenas de anos depois. GAME OVER")
    else: 
      print("Devido ao frio e a fome por ficar esperando que algo acontecesse, seus ossos foram encontrados por colonizadores dezenas de anos depois. GAME OVER")
  else:
    print("As criaturas do lago lhe levaram para o fundo para nunca mais ser achado! GAME OVER.")
else:
  print("Você deu de cara com os canibais da ilha e foi fritado. GAME OVER!")
 
  

import pygame
from Player import Sanity
from Player import Insanity
from Player import Health
from Random_encounter import RandomEncounter
from Shop import Shop
from getkey import getkey
from getkey import keys
from images import draw_image1
from images import draw_image2
from images import testImage
from images import image2
from images import screen
from UseableItems import Bandages
from UseableItems import SanityPill
from images import image3
from images import draw_image3
import sys, time

player = Sanity(100)
player_health = Health(100)
random_encounter = RandomEncounter()

draw_image2(image2, 2, 2)
print("Journey to Innsmouth.")
input("Press enter to start")
if getkey() == keys.ENTER:
  screen.fill(0)
  time.sleep(2)
  draw_image1(testImage, 2, 2, 0)

  print("")
  file = open('Notebook.txt')
  content = file.readlines()
  office = content[0:6]

  for line in office:
    words = line.split()
    for word in words:
      for char in word:
        if char == ' ':
          print(' ', end='')
        else:
          print(char, end='')
        sys.stdout.flush()
        time.sleep(0.03)
      print(" ", end='')

  choice = input("")  # Ensure proper indentation for the rest of the code

  if choice not in ['1', '2', '3']:
    NotValid = "Not a valid choice. Please enter a valid choice."

    for char in NotValid:
      print(char, end='')
      sys.stdout.flush()
      time.sleep(0.05)

  elif choice == "1":
    print("")
    SuppliesMessage = content[8]

    for char in SuppliesMessage:
      print(char, end='')
      sys.stdout.flush()
      time.sleep(0.05)

      shop = Shop()
      shop.visitShop()
      print("")

  elif choice == "2":
    print("")
    choice2 = input('content[10]')
    if choice2 == "1":
      print("")
      print(content[12])
    elif choice2 == "2":
      print("")
      choice3 = input(content[14])
      if choice3 == "1":
        print("")
        print(content[16])
        player.Sanity -= 1
        player.Insanity += 1
        print(player.Sanity_bar)
        random_encounter_result = random_encounter.get_random_encounter(
          player.Insanity)
        print("Random Encounter Result:", random_encounter_result)
      elif choice3 == "2":
       print("")
      print(content[18])
  elif choice == "3":
    pygame.quit()
    print("")
    print(content[20])

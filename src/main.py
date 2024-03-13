import pygame
from Player import Sanity
from Player import Insanity
from Player import Health
from Random_encounter import RandomEncounter
from Shop import Shop
from UseableItems import Inventory
# from getkey import getkey
# from getkey import keys
from images import draw_image1
from images import draw_image2
from images import testImage
from images import image2
from images import draw_image4
from images import screen
from UseableItems import Bandages
from UseableItems import SanityPill
from images import image3
from images import image4
from images import draw_image3
import sys, time

choice = 0
player = Sanity(10)
player_health = Health(10)
#following line of code gets rid of error with insanity
player_insanity = Insanity(0)
random_encounter = RandomEncounter()

draw_image2(image2, 2, 2)
#for some reason it works/runs better when no keys at all are pressed (including enter) prior to the "Press enter to start" line appears, or else it just stops running 
print("Journey to Innsmouth.")
enterInput = input("Press enter to start")
#if getkey() == keys.ENTER:
if enterInput == "":
  screen.fill(0)
  time.sleep(2)
  draw_image1(testImage, 2, 2, 0)

  print("")
  file = open('Notebook.txt')
  content = file.readlines()
  office = content[0:6]
  content9 = content[9]
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

  choice = input("What is your choice?" + "")
  time.sleep(3)
  # !!!Moved the following code to the bottom of the loop!!!
  
  # if choice not in [0, "0", '0', 1, '1', 2, '2', 3, '3', '', "", '\n']:
  #   NotValid = "Not a valid choice. Please enter a valid choice."

  #   for char in NotValid:
  #     print(char, end='')
  #     sys.stdout.flush()
  #     time.sleep(0.05)

  if choice == 1 or choice == "1" or choice == '1':
    print("")
    SuppliesMessage = content[8]

    for char in SuppliesMessage:
      print(char, end='')
      sys.stdout.flush()
      time.sleep(0.05)
      shop = Shop()
      shop.visitShop()
      print("")

  elif choice == 2 or choice == "2" or choice == '2':
    print("")
    #it starts at 0 so content 10 is line 11, which is blank, so content 9 is the correct line
    content9 = content[9]
    
    for char in content9:
      print(char, end='')
      sys.stdout.flush()
      time.sleep(0.06)
      
    choice2 = input("What's your choice?")
    if choice2 == 1 or choice2 == "1" or choice2 == '1':
      print("")
      #same thing with the following line and all the other content ones
      print(content[11])
    elif choice2 == 2 or choice2 == "2" or choice2 == '2':
      print("")
      content13 = content[13]
      choice3 = input(content13)
      if choice3 == 1 or choice3 == "1" or choice3 == '1':
        print("")
        print(content[15])
        player.Sanity -= 1
        player_insanity.Insanity += 1
        print(player.Sanity_bar)
        screen.fill(0)
        #the image appears now
        draw_image4(image4, 100, 2)

      elif choice3 == 2 or choice3 == "1" or choice3 == '1':
        print("")
        print(content[18])
  elif choice == 3 or choice == "3" or choice == '3':
    #pygame.quit()
    print("")
    print(content[20])

  elif choice != 1 and choice != 2 and choice != 3 and choice != "" and choice != '\n' and choice!= '': 
    NotValid = "Not a valid choice. Please enter a valid choice."

    for char in NotValid:
      print(char, end='')
      sys.stdout.flush()
      time.sleep(0.05)

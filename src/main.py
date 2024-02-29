import pygame
from Player import Sanity
from Player import Insanity
from Player import Health
from Random_encounter import RandomEncounter
from Shop import Shop
#from getkey import getkey
#from getkey import keys
import keyboard
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

player = Sanity(10)
player_health = Health(10)
random_encounter = RandomEncounter()
key1 = keyboard.read_key()

#draw_image2(image2, 2, 2)
print("Journey to Innsmouth.")
input("Press enter to start")
# if getkey() == keys.ENTER:
if key1 == 'enter':
  screen.fill(0)
  time.sleep(2)
  #draw_image1(testImage, 2, 2, 0)

  print("")
  office = """The scene opens in a dimly lit office, rain cracks against 
  glass casting a scattering of dots across the room. A haze gathering 
  from an ash tray chocks the room. A grey weathered man lies feet up on 
  the desk. The night went on like so many others, slummped in my office 
  chiar, cigar sputtering in the ash tray. The radio was playing some the
  usual rabble, nothing interesting. My eyes glazed from a half empty 
  bottle to the print on my door, Eliase Blackwood, private investigator. 
  Thats when she walked in, her eyes where lit with fear, the kind that 
  eats at you like a hungry rat.He names was Deliala Delorain. She says 
  that her husband disapeared into thin air on a trip to Alaska. But she 
  knows better than to believe in the impossible. She knows that something 
  dark and cruel, something otherworldy had ocured and the thought burned 
  her alive. I'll follow the case of course, that is my job. But first I 
  must get ready. You grab from your desk a pack of smokes, your notebook,
  1000 in cash , and the pills your doctor perscribed for you headaches
  
  What do do first?
  1: Shop for supplies 
  2: talk to Delorian 
  3: Leave to start the case"""

  for char in office:
    print(char, end='')
    sys.stdout.flush()
    time.sleep(0.05)

choice = input("")

if choice not in ['1', '2', '3']:
  NotValid = "Not a valid choice. Please enter a valid choice."

  for char in NotValid:
    print(char, end='')
    sys.stdout.flush()
    time.sleep(0.05)

elif choice == "1":
  print("")
  SuppliesMessage = """You stop near your local shop 
        to pick up supplies for the upcoming trip"""

  for char in SuppliesMessage:
    print(char, end='')
    sys.stdout.flush()
    time.sleep(0.05)

    shop = Shop()
    shop.visitShop()
    print("")

elif choice == "2":
  print("")
  choice2 = input(
      "You walk over to Delorian, she looks at you with a smile, her eyes where glazed with fear. what do you ask her? 1) Where was your huband when he disapeared? 2) Did you see anything when it happened 3) Sorry I bothered you, I get right to the case.     "
  )
  if choice2 == "1":
    print("")
    print(
        "We were on a fishing trip, he always hated buisy towns so we choose some place remote. Innsmouth I belive the town was called."
    )
  elif choice2 == "2":
    print("")
    choice3 = input(
        "Her eyes grow wide and her hands start to tremble, she will show you if that is what you really want. 1) I want to see (this may cause harm) 2) Keep it to yourself    "
    )
    if choice3 == "1":
      print("")
      print(
          "Ok, I'll share what I saw. She grabs a pen and paper and begins to draw. As the lines unfold from the pen your eyes start to ache and mind gets filled with images you dont understand. She puts the pen down and the pain subsides. Sanity-1"
      )
      player.Sanity -= 1
      player.Insanity += 1
      print(player.Sanity_bar)
      random_encounter_result = random_encounter.get_random_encounter(
          player.Insanity)
      print("Random Encounter Result:", random_encounter_result)
    elif choice3 == "2":
      print("")
      print("youd be better off not knowing anyway")
elif choice == "3":
  pygame.quit()
  print("")
  print(
      "You rush out the door eager to get the case started. You head strait to the port a grab the first ride to Massachewsits. When you arive you look around at the bustling city and relise you are completely lost. You wander around, going town by town unable to find anything. after a few weeks you return defeated. Shame you didnt get any more information before starting, maybe you would have been more succesful. THE END"
  )

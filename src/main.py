from Sanity import Sanity
from Health import Health
#hp lovecraft story. 1920s elchrich invastigator- mystery story, shop to buy things to help on the way, random incounters of elch beasts, they heard of mysterious disapearance that brought them to a sleepy town in the north, before they+ leave the stock up on items. End of story sees you stop a cult from waking C'thulu.
from Shop import Shop
from getkey import getkey, keys
from Sanity import Sanity
from Health import Health
player = Sanity(10)
player_health = Health(10)
key = getkey()
#from images import draw_test_image
#the following line of code (when uncommented) can be put into the code in some place such as after a key press, and it could get an image to be displayed
#draw_test_image(2,2)
print("                                     title of game.")
input("Press enter to start")
if key == keys.ENTER:
  #opening monologue
  print("")
  print("The scene opens in a dimly lit office, rain cracks against glass casting a scattering of dots across the room. A haze gathering from an ash tray chocks the room. A grey weathered man lies feet up on the desk" + "The night went on like so many others, slummped in my office chiar, cigar sputtering in the ash tray. The radio was playing some the usual rabble, nothing interesting. My eyes glazed from a half empty bottle to the print on my door, Eliase Blackwood, private investigator. Thats when she walked in, her eyes where lit with fear, the kind that eats at you like a hungry rat.He names was Deliala Delorain. She says that her husband disapeared into thin air on a trip to Alaska. But she knows better than to believe in the impossible. She knows that something dark and cruel, something otherworldy had ocured and the thought burned her alive. I'll follow the case of course, that is my job. But first I must get ready. You grab from your desk a pack of smokes, your notebook, 1000 in cash , and the pills your doctor perscribed for you headaches")
  print("")
  #first inventory addition
  #first choices
  choice = input("What do do first?  1) Shop for supplies 2) talk to Delorian 3) Leave to start the case ")
  if choice == "1":
    print("")
    print("You stop near your local shop to pick up supplies for the upcoming trip")
    #image
    #draw_test_image(2,2)
    #show shop inventory
    print("")
    
  elif choice == "2":
    print("")
    choice2 =input("You walk over to Delorian, she looks at you with a smile, her eyes where glazed with fear. what do you ask her? 1) Where was your huband when he disapeared? 2) Did you see anything when it happened 3) Sorry I bothered you, I get right to the case.     ")
    if choice2 == "1":
      print("")
      print("We were on a fishing trip, he always hated buisy towns so we choose some place remote. Innsmouth I belive the town was called.")
    elif choice == "2":
      print("")
      choice3 = input("Her eyes grow wide and her hands start to tremble, she will show you if that is what you really want. 1) I want to see (this may cause harm) 2) Keep it to yourself    ")
      if choice3 == "1":
        print("")
        print("Ok, I'll share what I saw. She grabs a pen and paper and begins to draw. As the lines unfold from the pen your eyes start to ache and mind gets filled with images you dont understand. She puts the pen down and the pain subsides. Sanity-1")
        player.Sanity -= 1
        print(player.Sanity_bar)
      elif choice3 == "2":
        print("")
        print("youd be better off not knowing anyway")
  elif choice == "3":
    print("")
    print("You rush out the door eager to get the case started. You head strait to the port a grab the first ride to Massachewsits. When you arive you look around at the bustling city and relise you are completely lost. You wander around, going town by town unable to find anything. after a few weeks you return defeated. Shame you didnt get any more information before starting, maybe you would have been more succesful. THE END")
print("")
#shop- create a variable for money, create options and cost



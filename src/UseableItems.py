import random

class Bandages:
    def __init__(self, bandage_count):
        self.bandages = bandage_count

    def use_bandage(self, health, sanity):
        if self.bandages >0 and health < 100:
            if sanity >= 10:
                min_healing = 40
                max_healing = 45
                failure_chance = 0
            elif sanity == 9:
                min_healing = 39
                max_healing = 43
                failure_chance = 0
            elif sanity == 8:
                min_healing = 38
                max_healing = 40
                failure_chance = 2
            elif sanity == 7:
                min_healing = 36
                max_healing = 39
                failure_chance = 6
            elif sanity == 6:
                min_healing = 30
                max_healing = 35
                failure_chance = 10
            elif sanity == 5:
                min_healing = 25
                max_healing = 30
                failure_chance = 20
            elif sanity == 4:
                min_healing = 20
                max_healing = 25
                failure_chance = 30
            elif sanity == 3:
                min_healing = 15
                max_healing = 20
                failure_chance = 40
            elif sanity == 2:
                min_healing = 10
                max_healing = 15
                failure_chance = 50
            elif sanity == 1:
                min_healing = 5
                max_healing = 10
                failure_chance = 70
            else:
                print("Your madness has gotten the best of you. YOU MUST RAISE YOUR SANITY")
                return

            if random.randint(1, 100) <= failure_chance:
              self.bandages -= 1
              print("Bandage failed to heal try you can keep trying but you may want to raise your sanity.")
              return

            healing_amount = random.randint(min_healing, max_healing)
            health = min(100, health + healing_amount)
            self.bandages -= 1
            print(f"You know have {health}")
        else:
            print("Cannot use bandage. No bandages available.")




class SanityPill:

  def __init__(self, SP_count):
    self.sanitypills = SP_count

  def use_SP(self, Sanity):
    if Sanity < 10 and self.sanitypills > 0:
      Sanity += 2
      self.sanitypills -= 1
      print("Sanity Pill used. Player sanity increased to", Sanity)
    else:
      print(
          "Cannot use Sanity Pill. Sanity is full or no sanity pills available."
      )
'  '

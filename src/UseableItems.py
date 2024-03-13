import random
from Player import Health, Sanity, Insanity


class Bandages:

  def __init__(self, bandage_count):
    self.bandages = bandage_count

  def use_bandage(self, health, sanity):
    if self.bandages > 0 and health < 100:
      healing_data = {
          10: (4, 4.5, 0),
          9: (3.9, 4.3, 0),
          8: (3.8, 4, 2),
          7: (3.6, 3.9, 0.6),
          6: (3.0, 3.5, 1),
          5: (2.5, 3.0, 2.0),
          4: (2.0, 2.5, 3.0),
          3: (1.5, 2.0, 4.0),
          2: (1.0, 1.5, 5.0),
          1: (0.5, 1.0, 7.0)
      }
      if sanity not in healing_data:
        print(
            "Your madness has gotten the best of you. YOU MUST RAISE YOUR SANITY"
        )
        return
      min_healing, max_healing, failure_chance = healing_data[sanity]
      if random.randint(1, 100) <= failure_chance:
        print(
            "Bandage failed to heal. You can keep trying but you may want to raise your sanity."
        )
        return
      healing_amount = random.randint(min_healing, max_healing)
      health = min(100, health + healing_amount)
      print(f"You now have {health}")
    else:
      print("Cannot use bandage. No bandages available.")


class SanityPill:

  def __init__(self, SP_count):
    self.sanitypills = SP_count

  def use_SP(self, Sanity):
    if Sanity < 10 and self.sanitypills > 0:
      Sanity += 2
      print("Sanity Pill used. Player sanity increased to", Sanity)
    else:
      print(
          "Cannot use Sanity Pill. Sanity is full or no sanity pills available."
      )


class Inventory:
  from Player import Health, Sanity, Insanity

  def __init__(self, sanitypills, bandages):
   self.sanitypills = sanitypills
   self.bandages = bandages
   self.sanitypill_instance = SanityPill(
       sanitypills) 

  def displayInventory(self):
   print("Inventory")
   print(f"Sanity Pills: {self.sanitypills}")
   print(f"Bandages: {self.bandages}")

  def main():
    print("What would you like to do?")
    print("1. Use Sanity Pill")
    InventoryM = Inventory(sanitypills=3, bandages=5)
    Choice = input()
    if Choice == "1":
      InventoryM.displayInventory()
      InventoryM.sanitypill_instance.use_SP(
     Sanity) 
    elif Choice == "2":
      InventoryM.displayInventory()
      bandages_instance = Bandages(InventoryM.bandages)
      bandages_instance.use_bandage(Health.Health, Sanity.Sanity)
      bandages_instance = Bandages(InventoryM.bandages)
  
      bandages_instance.use_bandage(Health.Health, Sanity.Sanity)
    elif Choice == "3":
      pass
    else:
      print("Invalid choice. Please select a valid option.")
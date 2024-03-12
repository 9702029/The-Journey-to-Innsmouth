import random
from Player import Health, Sanity, Insanity


class Bandages:

  def __init__(self, bandage_count):
    self.bandages = bandage_count

  def use_bandage(self, health, sanity):
    if self.bandages > 0 and health < 100:
      healing_data = {
          10: (40, 45, 0),
          9: (39, 43, 0),
          8: (38, 40, 2),
          7: (36, 39, 6),
          6: (30, 35, 10),
          5: (25, 30, 20),
          4: (20, 25, 30),
          3: (15, 20, 40),
          2: (10, 15, 50),
          1: (5, 10, 70)
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
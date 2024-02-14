class Shop:
  def __init__(self):
      self.money = 100
      self.sanitypills = 0
      self.bandages = 0

  def visitShop(self):
      sp = """Welcome to (shop name). What can I do for you?

   ITEM         COST
1. sanity pill  10
2. bandages     5

"""

      print(sp)
      choice = input("What would you like to buy?: ") 

      if choice == "1":
          if self.money >= 10:
              self.sanitypills += 1
              self.money -= 10
              print("You now have", self.sanitypills, "sanity pills.")
          else:
              print("You don't have enough money to buy a sanity pill.")

      elif choice == "2":
          if self.money >= 5:
              self.bandages += 1
              self.money -= 5
              print("You now have", self.bandages, "bandages.")
          else:
              print("You do not have enough money to buy bandages.")

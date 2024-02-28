import sys
import time

class Shop:
    def __init__(self):
        self.money = 100
        self.sanitypills = 0
        self.bandages = 0

    def visitShop(self):
        sp = "Welcome to The Emporium. What can I do for you?\nYou have {} money.\n".format(self.money)

        for char in sp:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(0.06)

        items = """ITEM         COST
1. sanity pill  10
2. bandages     5
3. exit shop"""

        for char in items:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(0.06)

        while True:
            choice = input("\nWhat would you like to buy?: ")

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

            elif choice == "3":
                print("Exiting the shop.")
                break  


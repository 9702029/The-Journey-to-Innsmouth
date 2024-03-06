class Inventory:

  def __init__(self, sanitypills, bandages):
    self.sanitypills = sanitypills
    self.bandages = bandages

  def displayInventory(self):
    print("Inventory")
    print(f"Sanity Pills: {self.sanitypills}")
    print(f"Bandages: {self.bandages}")

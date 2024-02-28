class Bandages:

  def __init__(self, bandage_count):
    self.bandages = bandage_count

  def use_bandage(self, Health):
    if Health < 10 and self.bandages > 0:
      Health += 2
      self.bandages -= 1
      print("Bandage used. Player health increased to", Health)
    else:
      print("Cannot use bandage. Health is full or no bandages available.")


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


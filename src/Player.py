class Health:
    def __init__(self, Health):
        self.Health = Health
        self.Health_bar = "Health""[" + "=" * self.Health + " " * (10 - self.Health) + "]"
    Health = 10

class Sanity:
    def __init__(self, Sanity):
        self.Sanity = Sanity
        self.Sanity_bar = "Sanity""[" + "=" * self.Sanity + " " * (10 - self.Sanity) + "]"
    Sanity = 10

class Insanity:
  def __init__(self, Insanity):
        self.Insanity = Insanity
        self.Insanity_bar = "Insanity""[" + "=" * self.Insanity + " " * (0 + self.Insanity) + "]"
  Insanity = 0
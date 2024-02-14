class Health:
    def __init__(self, Health):
        self.Health = Health
        self.Health_bar = "Health""[" + "=" * self.Health + " " * (10 - self.Health) + "]"
    Health = 10
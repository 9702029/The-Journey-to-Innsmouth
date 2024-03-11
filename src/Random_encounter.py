from Player import Insanity
from random import choices

class RandomEncounter:
#list of encounters
    encounters = [
        {"A stuborn mule lies in the middle of the road. YOu loose an hour waiting for it to pass":"Easy Encounter", "difficulty": 1},
        {"name": "Moderate Encounter", "difficulty": 2},
        {"name": "Hard Encounter", "difficulty": 3},
        {"While travelling the streats you are ambushed by a group of figures with hoods covering their faces, they pull knives out of their pockets. Its clear what their intention is": "Very Hard Encounter", "difficulty": 4},
        {"": "Extreme Encounter", "difficulty": 5}
    ]

    def get_random_encounter(self, Insanity):
        # Calculate the maximum difficulty based on insanity
        max_difficulty = max(1, min(Insanity // 20, 5))
        # Filter encounters based on maximum difficulty
        valid_encounters = [encounter for encounter in self.encounters if encounter["difficulty"] <= max_difficulty]
        # Choose a random encounter from valid encounters
        return random.choice(valid_encounters)
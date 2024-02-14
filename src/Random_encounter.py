from Sanity import Sanity
from random import choices

class RandomEncounter:
    {"name": "Easy Encounter", "difficulty": 1},
    {"name": "Moderate Encounter", "difficulty": 2},
    {"name": "Hard Encounter", "difficulty": 3},
    {"name": "Very Hard Encounter", "difficulty": 4},
    {"name": "Extreme Encounter", "difficulty": 5}

def get_random_encounter(sanity):
    # Calculate the maximum difficulty based on sanity
    max_difficulty = max(1, min(sanity // 20, 5))
    # Filter encounters based on maximum difficulty
    valid_encounters = [encounter for encounter in encounters if encounter["difficulty"] <= max_difficulty]
    # Choose a random encounter from valid encounters
    return random.choice(valid_encounters)
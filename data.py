"""Game data for the text-based quest.

Pure data module: no input() or print() calls.

GAME_STATE is the single dictionary holding every state of the game.
Each state key maps to:
    location : title shown for the place
    question : the scene text / prompt
    status   : "active", "victory" or "game_over"
    choices  : list of (answer text, next state key) tuples
               a next key of None means "exit the game"
"""

# Shared by every end screen (victory / game over).
_END_CHOICES = [
    ("Start Over", "start"),
    ("Exit", None),
]

GAME_STATE = {
    # ---------- Active rooms ----------
    "start": {
        "location": "Dark Room",
        "question": "You wake up at night in a dark room after hearing a strange sound...",
        "status": "active",
        "choices": [
            ("Look under the bed", "under_bed"),
            ("Go lock the window", "window"),
            ("Turn on the light", "light_on"),
            ("Open the wardrobe", "wardrobe"),
            ("Exit to the next room", "hallway"),
        ],
    },
    "under_bed": {
        "location": "Under the Bed",
        "question": "You kneel down. Two eyes glow in the dark under the bed...",
        "status": "active",
        "choices": [
            ("Reach in to grab it", "game_over_bed"),
            ("Step back slowly", "start"),
        ],
    },
    "window": {
        "location": "By the Window",
        "question": "The window is wide open and the curtain is moving in the wind.",
        "status": "active",
        "choices": [
            ("Lock the window", "start"),
            ("Lean out and look outside", "game_over_window"),
        ],
    },
    "light_on": {
        "location": "Lit Room",
        "question": "The light flickers on. The room is empty, but a note on the desk says: 'Check the hallway.'",
        "status": "active",
        "choices": [
            ("Follow the note to the hallway", "hallway"),
            ("Turn the light off and stay", "start"),
        ],
    },
    "hallway": {
        "location": "Hallway",
        "question": "The hallway is quiet. The sound seems to come from the kitchen.",
        "status": "active",
        "choices": [
            ("Go to the kitchen", "kitchen"),
            ("Check the bathroom", "bathroom"),
            ("Climb the attic stairs", "attic"),
            ("Go back to the bedroom", "start"),
            ("Open the front door", "victory"),
        ],
    },
    "kitchen": {
        "location": "Kitchen",
        "question": "A pot lies on the floor and a basement door creaks open.",
        "status": "active",
        "choices": [
            ("Pet the cat hiding behind the pot", "victory"),
            ("Open the basement door", "game_over_basement"),
            ("Open the fridge", "fridge"),
            ("Go back to the hallway", "hallway"),
        ],
    },
    "wardrobe": {
        "location": "Wardrobe",
        "question": "The wardrobe door creaks open. Coats hang inside and something shifts behind them.",
        "status": "active",
        "choices": [
            ("Hide inside and close the door", "game_over_wardrobe"),
            ("Push the coats aside", "light_on"),
            ("Close it and step back", "start"),
        ],
    },
    "bathroom": {
        "location": "Bathroom",
        "question": "The tap is dripping and the mirror is fogged up. Someone has drawn a face in the steam.",
        "status": "active",
        "choices": [
            ("Wipe the mirror clean", "game_over_mirror"),
            ("Turn off the tap and leave", "hallway"),
        ],
    },
    "attic": {
        "location": "Attic",
        "question": "Dusty boxes everywhere. A small window shows the neighbour's porch light across the street.",
        "status": "active",
        "choices": [
            ("Wave a flashlight at the neighbour's window", "victory"),
            ("Open a dusty box", "game_over_box"),
            ("Climb back down", "hallway"),
        ],
    },
    "fridge": {
        "location": "Fridge",
        "question": "The fridge light flickers. There is a carton of milk that is warm, and a plate of cold pizza.",
        "status": "active",
        "choices": [
            ("Drink the warm milk", "game_over_milk"),
            ("Grab the pizza and step back", "kitchen"),
        ],
    },

    # ---------- End screens ----------
    "victory": {
        "location": "Victory!",
        "question": "You found the cat and the night is calm again. You win!",
        "status": "victory",
        "choices": _END_CHOICES,
    },
    "game_over_bed": {
        "location": "Game Over",
        "question": "Something grabs your arm and pulls you under the bed...",
        "status": "game_over",
        "choices": _END_CHOICES,
    },
    "game_over_window": {
        "location": "Game Over",
        "question": "A gust of wind slams the window on you and you lose your balance...",
        "status": "game_over",
        "choices": _END_CHOICES,
    },
    "game_over_basement": {
        "location": "Game Over",
        "question": "The stairs are dark and the door locks behind you...",
        "status": "game_over",
        "choices": _END_CHOICES,
    },
    "game_over_wardrobe": {
        "location": "Game Over",
        "question": "The wardrobe door locks from the outside and the coats start to move...",
        "status": "game_over",
        "choices": _END_CHOICES,
    },
    "game_over_mirror": {
        "location": "Game Over",
        "question": "The face in the mirror smiles back at you, and it isn't your reflection...",
        "status": "game_over",
        "choices": _END_CHOICES,
    },
    "game_over_box": {
        "location": "Game Over",
        "question": "The box is full of old dolls. Their eyes all turn toward you at once...",
        "status": "game_over",
        "choices": _END_CHOICES,
    },
    "game_over_milk": {
        "location": "Game Over",
        "question": "The milk tastes strange and the room starts to spin...",
        "status": "game_over",
        "choices": _END_CHOICES,
    },
}

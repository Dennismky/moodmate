import random

MOOD_SUGGESTIONS = {
    "happy": [
        "Celebrate your day with your favorite song!",
        "Share your joy with a friend.",
        "Go out for a walk and smile at strangers."
    ],
    "sad": [
        "Watch a comforting movie.",
        "Call someone you trust.",
        "Write your feelings in a journal."
    ],
    "angry": [
        "Try deep breathing exercises.",
        "Go for a run or do intense exercise.",
        "Listen to calming music."
    ],
    "jovial": [
        "Dance like nobody's watching!",
        "Make someone else laugh.",
        "Do something spontaneous and fun."
    ],
    "anxious": [
        "Try a short meditation session.",
        "Write down your worries and rip them up.",
        "Drink some water and rest your eyes."
    ]
}

def get_random_suggestion(mood):
    suggestions = MOOD_SUGGESTIONS.get(mood.lower(), [])
    if suggestions:
        return random.choice(suggestions)
    return "No suggestion available for this mood."

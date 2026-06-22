import random

subjects = [
    "Samandar Khan",
    "Qalandar Khan",
    "Tofan Khan",
    "cat of Karachi",
    "a group of Monkeys",
    "Prime Minister of Pakistan",
    "Auto Driver from Karachi"
]

actions = [
    "launches missiles",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Karachi local market",
    "a plate of pakora",
    "inside the Parliament",
    "at Ada Kharo",
    "during a PSL match",
    "at Chaman border"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("Do you want to generate another headline? (y/n): ").strip().lower()

    if user_input == "n":
        break

print("\nThank you for using the Fun Headline Generator!")
import random 
easy_words = ("apple","train","tiger","rupees","iran",)
medium_words = ("python","bottle","monkey","planet","laptop",)
hard_words = ("elephant","computer","dimand","mountain","elephant",)


print ( "Welcome to the  pasword Guessing Game!")
print ("choose a difficulty level : easy, medium, hard")


level = input("Enter difficulty level: ").lower()
if level == "easy":
    secrat = random .choice(easy_words)
elif level == "medium":
    secrat = random .choice(medium_words)
elif level == "hard":
    secrat = random .choice(hard_words)
else:
    secrat = random .choice(easy_words)


    attempts = 0
    print ("\nGuess secret password:")
while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1
    if guess == secrat:
        print (f"Congratulations! You guessed the password in {attempts} attempts.")
        break
    hint=""
    for i in range(len(secrat)):
        if i < len(guess) and guess[i] == secrat[i]:
            hint += guess[i]
        else:
            hint += "_"

    print(f"Hint: {hint}")
    print("Game Over!")
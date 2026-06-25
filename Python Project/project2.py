# 1- import the random module 
import random
# 2- crate subjects
subjects ={
    "Falana Khan ",
    "Qalandar Khan",
    "Samandar Khan",
    "A Karachi Cat",
    "Group of Monkeys",
    "Prime Minister of Pakistan",
    "Ricksha Driver from Karachi"

}

actions ={
    "launches",
    "contects",
    "dance with",
    "eats",
    "declears war on ",
    " orders",
    "celebrates",


}

places_or_things ={
    "at Red Fort",
    "Karachi local market",
    "a palat of shalgham",
    "inside a parliamant",
    "at qabristan",
    "during a cricket match",
    "at taftan border",
}
#start the headline generator loop
while True:
    subject = random . choice(subjects)
    action = random . choice(actions)
    place_or_thing = random . choice(places_or_things)
    headline = f" BREAKING NEWS : {subject} {action} {place_or_thing}"
    print ("\n =headline ")
    user_input = input ("\n do ypu want to anpther headline  ? (yes/no) ").strip()
    if user_input=="no":
        break
    # PRINT goodbye_message 
    print ("\n thanks for using the  fun headline generator.have a fun day Goodbye")
           
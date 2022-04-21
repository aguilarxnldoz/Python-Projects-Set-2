"""
this program gives us three stories of which the user can input any
verbs, nouns, adjectives, number, etc to have the each story playout in different ways.
"""
print("DISCLAIMER: ANYTHING SAID IN THESE STORIES ARE ALL FICTION AND JUST FOR FUN \
       DO NOT TAKE THE FOLLOWING SERIOUSLY")

# This code asks the user what they want to select.
story = int(input("Choose a story [1-3 or q]: "))

# This code asks for adjectives, verbs, nouns, etc
# to tell the story in different ways.
adj = input("Choose an adjective: ")
adj2 = input("Choose another adjective: ")
adj3 = input("Choose a last adjective: ")
verb = input("Choose a verb: ")
verb2 = input("Choose another verb: ")
verbing = input("Choose a verb that ends with 'ing': ")
noun = input("Choose a noun: ")
pnoun = input("Choose a plural noun: ")
bpart = input("Select a body part: ")
location = input("Choose a place: ")
digit = input("Select a number")
name = input("Enter a Name: ")

# These madlibs are the three stories.
madlib1 = f"Once upon a time in a place called {location} there was a {adj} kid named 'Avant'. \
He is {digit}-years-old, but is a total {noun}. One day Avant decided to {adj2} {verb} a random freshman \
in the D wing. The freshman totally felt it in the {bpart}. The freshman then started {verbing}, he then called his \
other {pnoun} for backup. Unfortunately they were scared of Avant the menace. Their expressions were {adj3} and \
they {verb2} themselves. \
The end."

madlib2 = f"Once upon a time, a {adj} grandpa who was in his {digit}'s, and his grandaughter, '{name}' lived in a very \
 {adj2} {location}. One day, the grandpa went to go {verb} and catch some {pnoun}. He {verb2} '{name}' in the {location} because \
her {bpart} was missing making her unable to do {verbing} outside of {location}. \
after a few hours the grandpa came home with a {adj3} {noun}. {name} was very happy to see her grandpa \
succeed in a big catch!"

madlib3 = f"Once upon a time there was a {digit}-year-old {adj} rapper called '{name}'. He was very talented but hated among his \
{pnoun}. He lived in a very poor neighborhood called '{location}' where the crime rate was {digit}%. It \
was not a good environment for him and his career. One day he clenched his {bpart} and told himself,'I'm going to {verb} and become \
the best {adj2} rapper alive and make it out {location}!' He started putting in the work and {verbing}. \
He made sure his efforts never went to waste and always made sure they {verb2}. After a few years of pure commitment, \
he was able to make it out of {location} with his {adj3} tracks and was able to hit number 1 on the billboards \
and was able to achieve his long dream of obtaining a {noun}! The End!"


if story == 1:
    print(madlib1)

elif story == 2:
    print(madlib2)

elif story == 3:
    print(madlib3)

elif story == "q":
    print("Have a good day!")

else:
    while story != 1 or 2 or 3 or "q":
        print("Invalid Option.")
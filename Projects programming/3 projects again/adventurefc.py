from PIL import Image
harvard = Image.open("harvard.png")
kimchi = Image.open("kimchi.jpg")
monkey = Image.open("monke.jpg")
sick = Image.open("sick.jpg")


name = input("What is your name?: ")
print("This is " + name + "'s" + "adventure!")
print("Your options for each situation will be printed above the question.")
print("please print with just the corresponding letters within the answers. ex: a, b, c.")

def physics():
    print("You study physics for the rest of lunch and take your test the following class. You receive full marks and get into Harvard University. The end!")
    harvard.show()

def math():
    print("Your math is an online class in SAIL and you can reschedule your test anytime... You die to your own obliviousness... Game Over.")

def study():
    print("a.) Math / b.) Physics")
    story = input("You are in a state of panic and head to the nurse's office to recover. You decide to study for two tests today but only have time for one... What do you study?: ")
    
    if story == "a":
        math()
    
    elif story == "b":
        physics()

    else:
        print("Invalid Option... Game Over")

def choice1b():
    print("a.) Shake his hand / b.) Give him a fist bump")
    story = input("He approaches you with an extended arm and hand waiting to be greeted, what action do you take...: ")

    if story == "a":
        print("You have died to an unnatural disease... Game Over.")
        sick.show()
    
    elif story == "b":
        study()
        
    else:
        print("Invalid Option... Game Over.")

def gorilla():
    print("She obtains the strength of a gorilla and suplexes your head into the table... Game Over...")
    monkey.show()

def give_lunch():
    print("You open your bag and you pull out a container filled with your favourite, kimchi friedrice. Both of you share together and stuff yourselves. Happy Ending!")
    kimchi.show()

def dont_m_her():
    print("School ends and you start walking home, you feel as if a menacing presence is following you. You Died... Game Over.")

def dash():
    print("a.) Give her the lunch you were saving / b.) let her starve...")
    story = input("You run out of the classroom and meet her in the library. She is waiting and starving. Whats your move?: ")
    
    if story == "a":
        give_lunch()
    
    elif story == "b":
        gorilla()

    else:
        print("Invalid Option... Game Over.")


def m_her():
    print("She immediatly finds your location and drags you out with the strength of a gorilla. She stuffs you in a locker... Game Over.")
    monkey.show()

def choice1a():
    print("a.) dont message her, spend time with the homies. / b.) dash out the class and find her. / c.) message her saying you have other plans. ")
    story = input("You arrive at Mr. Rai's room and take a seat with your group. Suddenly you remembered you were suppose to spend time with your girl. What do you do?: ")

    if story == "a":
        dont_m_her()

    elif story == "b":
        dash()

    elif story == "c":
        m_her()
    
    else:
        print("Invalid Option... Game Over.")


def beginning():
    print("a.) Head to Mr. Rai's room. / b.) You cannot escape.")
    story = input("The lunch bell rings and you head straight to the den to meet up with your friends, in the corner of your eye you see james coming down the stairs, what do you do?: ")

    if story == "a":
        choice1a()

    elif story == "b":
        choice1b()

    else:
        print("Invalid Input... Game Over.")

beginning()
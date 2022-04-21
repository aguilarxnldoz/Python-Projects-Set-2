from PIL import Image
print("This is the quiz game!")
image1 = Image.open("images.png.png")
image2 = Image.open("IMG_2185.JPG.JPG")
playing = input("Do you wanna play? ")


def game():
    if playing.lower() == "yes":

        print("okie dokie!")
        score = 0

        answer = input("what do you call people from the Philippines? ")
        if answer.lower()  == "filipinos":
            print('Correct Answer!')
            score = score + 1
            print(str(score) + "/" + "10")
            image1.show()
        else: 
            print('Incorrect Answer! ANS: Filipinos / filipinos')
            print(str(score) + "/" + "10") 



        answer = input("Whats KP's rival school? ")
        if answer.lower() == "guildford park" or answer.lower() == 'gp':
            print('Correct Answer!')
            score = score + 1
            print(str(score) + "/" + "10")
        else: 
            print('Incorrect Answer! ANS: Guildford Park / GP')
            print(str(score) + "/" + "10") 



        answer = input("how many letters are in the alphabet? ")
        if answer.lower() == "26" or answer.lower() == "twenty-six":
            print('Correct Answer!')
            score = score + 1
            print(str(score) + "/" + "10")
        else: 
            print('Incorrect Answer! ANS: 26 / twenty-six')
            print(str(score) + "/" + "10") 



        answer = input("a yellow fruit? ")
        if answer.lower() == "mango" or answer.lower() == "lemon" or answer.lower() == "banana":
            print('Correct Answer!')
            score = score + 1
            print(str(score) + "/" + "10")
        else: 
            print('Incorrect Answer! ANS: mango / lemon / banana')
            print(str(score) + "/" + "10") 



        answer = input("what is the speed limit in a city/town? ")
        if answer.lower() == "60" or answer.lower() == "60km/h":
            print('Correct Answer!')
            score = score + 1
            print(str(score) + "/" + "10")
        else: 
            print('Incorrect Answer! ANS: 60 or 60km/h') 
            print(str(score) + "/" + "10")



        answer = input("Nooks and...? ")
        if answer.lower() == "crannys":
            print('Correct Answer!')
            score = score + 1
            print(str(score) + "/" + "10")
        else: 
            print('Incorrect Answer! ANS: crannys')
            print(str(score) + "/" + "10")


        answer = input("Whats the color of Arsh's gutti? ")
        if answer.lower() == "black":
            print('Correct Answer!')
            score = score + 1
            print(str(score) + "/" + "10")
            image2.show()
        else: 
            print('Incorrect Answer! ANS: look at Arsh')
            print(str(score) + "/" + "10")


        answer = input("At what age can get your Class-7 (Learners)? ")
        if answer.lower() == "16" or answer.lower() == "sixteen":
            print('Correct Answer!')
            score = score + 1
            print(str(score) + "/" + "10")
        else: 
            print('Incorrect Answer! ANS: 16 / sixteen') 
            print(str(score) + "/" + "10")



        answer = input("What is the button on the keyboard that fullscreens \
        the selected window? ")
        if answer.lower() == "f11":
            print('Correct Answer!')
            score = score + 1
            print(str(score) + "/" + "10")
        else: 
            print('Incorrect Answer! ANS: f11')
            print(str(score) + "/" + "10") 



        answer = input("what color is the middle circle on a traffic light? ")
        if answer.lower() == "yellow":
            print('Correct Answer!')
            score = score + 1
            print(str(score) + "/" + "10")
            score == score * 10
            print("Final Mark:" + str(score * 10) + "%")

        else: 
            print('Incorrect Answer! ANS: yellow')  
            print("You got: " + str(score) + "/" + "10" + "On this quiz!")

            score == score * 10
            print("Final Mark:" + str(score * 10) + "%")


    elif playing.lower() == "no":
        print("goodbye")

game()
replay = input("Retry?")
 
while replay == "yes":
    game()
    replay = input("Retry?")
    if replay == "no":
        print("goodbye") 



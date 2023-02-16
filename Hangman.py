# initialise the program
import turtle
import random
import time

turtle.speed(0)
done = False

print("************Welcome to hangman, you have 6 chances to guess the word************")

with open("/Users/raphaelbialystok-joly/Documents/Code/Python/Hangman/words.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))


def makeword():
    while True:
        x = random.choice(words)
        if len(x) > 3 and len(x) <= 6:
            print(x)
            return (x)
        


def setup():
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(5)
    turtle.pencolor("blue")
    #draws hanging station
    turtle.penup()
    turtle.backward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(400)
    turtle.backward(200)
    turtle.left(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(30)

def drawbody(bpart):
    if bpart == 5: # head
        turtle.right(90)
        turtle.circle(20)
        turtle.left(90)
        turtle.penup()
        turtle.forward(40)
        turtle.pendown()
    if bpart == 4: # body
        turtle.forward(100)
    if bpart == 3: # left leg
        turtle.left(45)
        turtle.forward(60)
        turtle.backward(60)
        turtle.right(45)
    if bpart == 2: # right leg
        turtle.right(45)
        turtle.forward(60)
        turtle.backward(60)
        turtle.left(45)
    if bpart == 1:# left arm
        turtle.backward(75)
        turtle.left(75)
        turtle.forward(60)
        turtle.backward(60)
        turtle.right(75)
    if bpart == 0: # right arm
        turtle.right(75)
        turtle.forward(60)
        turtle.backward(60)
        time.sleep(1.5)
        turtle.penup()
        turtle.home()
        turtle.backward(55)
        turtle.pendown()
        turtle.pencolor("red")
        turtle.write("You lose", font=("Arial", 30, "normal"))
        time.sleep(1.5)
        

def game():
    score = turtle.Turtle()
    turtle.reset()
    turtle.clearscreen()
    setup()
    lives = 6

    


    # makes list with word
    finalword = []
    guessword = ("")
    guessl = []
    for i in makeword():
        finalword.append(i)
        guessword = guessword + (i)

    for i in range(0, len(guessword)):
        guessl.append("-")
    #Figgure out how to join this into a string
        
    
    # Asks for input for first letter
    while finalword != []:
        pinput = turtle.textinput("Hangman", "Enter a letter: ")

        if pinput in finalword:  # if letter is in word
            finalword = finalword.remove(pinput)
            score.clear()
            score.write("Current found: " + guess, font=("Arial", 30, "normal"))
            

        elif pinput not in finalword:  # if the letter is not in the word
            print("wrong")
            lives = lives - 1
            if lives == 0:
                drawbody(0)
                game()
            else:
                drawbody(lives)
                # draw hangman


game()

# draw the hangman

# initialise the program
import turtle
import random
import time
import customtkinter as Ctk


screen = turtle.Screen()
screen.setup(1000, 500, startx=0, starty=0)
screen.bgcolor("white")
turtle.speed(0)
score = turtle.Turtle()
score.penup()
score.hideturtle()
score.forward(250)
guessl = []
usedlets = ("")
hiddenusedlets = ("")

usedletters = turtle.Turtle()
usedletters.penup()
usedletters.hideturtle()
usedletters.forward(-300)

print("************Welcome to hangman, you have 6 chances to guess the word************")

with open("words.txt", "r") as file:
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
    # draws hanging station
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
    if bpart == 5:  # head
        turtle.right(90)
        turtle.circle(20)
        turtle.left(90)
        turtle.penup()
        turtle.forward(40)
        turtle.pendown()
    if bpart == 4:  # body
        turtle.forward(100)
    if bpart == 3:  # left leg
        turtle.left(45)
        turtle.forward(60)
        turtle.backward(60)
        turtle.right(45)
    if bpart == 2:  # right leg
        turtle.right(45)
        turtle.forward(60)
        turtle.backward(60)
        turtle.left(45)
    if bpart == 1:  # left arm
        turtle.backward(75)
        turtle.left(75)
        turtle.forward(60)
        turtle.backward(60)
        turtle.right(75)
    if bpart == 0:  # right arm
        turtle.right(75)
        turtle.forward(60)
        turtle.backward(60)
        time.sleep(1.5)
        turtle.penup()
        turtle.home()
        turtle.backward(55)
        turtle.right(90)
        turtle.forward(150)
        turtle.left(90)
        turtle.pendown()
        turtle.pencolor("red")
        turtle.write("You Lose", font=("Arial", 30, "normal"))
        time.sleep(1.5)


# realword needs to be a string, setup is a boolean and guess is a string. This function will make the word with the filled in '-'
def makeguess(realword, setup, guess):
    # makes a list of the guess
    global guessl
    newguessl = []
    realwordlist = [i for i in realword]  # makes a list of 'realword'
    score.clear()
    if setup == True:
        for i in range(0, len(realword)):
            guessl.append("-")
            return stringconvert(guessl)
    if setup == False:
        
        if guess in realwordlist and len(guess) > 1:
            thing = realwordlist.find(guess)
            for i in range(0, thing - 1):
                newguessl.append("-")
            newguessl.append(guess)
            for i in range(len(guess)+thing-1, len(realword)):
                newguessl.append("-")
                
        elif len(guess) == 1:
            for i in realwordlist:
                if guess == i or i in guessl != "-":
                    newguessl.append(i)
                
                else:
                    newguessl.append("-")
        guessl = newguessl
        score.write(stringconvert(guessl), font=("Verdana", 20, "normal"))


def stringconvert(word):
    fword = ""
    for i in word:
        fword += i
    return fword


def input_box(prompt, default=None):
    # create a tkinter window
    root = Ctk.CTk()

    root.geometry("200x200")
    root.anchor("center")

    frame = Ctk.CTkFrame(root)

    input = Ctk.CTkInputDialog(
        text=prompt, title=prompt)

    return input.get_input()

    root.mainloop()


def game():
    global hiddenusedlets
    # sets up the game
    usedletters.clear()
    turtle.reset()
    turtle.clearscreen()
    setup()
    lives = 6
    global usedlets

    # makes list with word
    finalword = []
    guessword = ("")
    guessl = []
    for i in makeword():
        finalword.append(i)
        guessword = guessword + (i)

    # makes the blank word
    blank = makeguess(guessword, True, None)

    # Asks for input for first letter
    while finalword:

        pinput = input_box("Enter a letter", "")

        print(pinput)
        print(finalword)
        if pinput in stringconvert(finalword):

            for i in range(len(finalword)):
                if pinput in stringconvert(finalword):
                    finalword.remove(pinput)

            hiddenusedlets = hiddenusedlets + (pinput + ", ")
            makeguess(guessword, False, pinput)

            if not finalword:
                turtle.penup()
                turtle.home()
                turtle.backward(55)
                turtle.right(90)
                turtle.forward(150)
                turtle.left(90)
                turtle.pendown()
                turtle.pencolor("green")
                turtle.write("You win", font=("Arial", 30, "normal"))
                time.sleep(1.5)
                game()
        
        elif pinput in hiddenusedlets:
            usedletters.clear()
            usedletters.write("You have already\n used that letter", font=(
                "Verdana", 20, "normal"))
            time.sleep(1.5)
            usedletters.clear()
            usedletters.write(usedlets, font=("Verdana", 20, "normal"))

        
        
        else:
            lives -= 1
            if lives == 0:
                drawbody(0)
                game()
            else:
                drawbody(lives)
                usedlets = usedlets + (pinput + ", ")
                hiddenusedlets = hiddenusedlets + (pinput + ", ")
                usedletters.write(usedlets, font=("Verdana", 20, "normal"))
                # draw hangman


game()

# draw the hangman

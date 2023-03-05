
# initialise the program
import turtle
import random
import time
import tkinter as tk
import socket
import threading

yyy = 0

HOST = ''  # empty string means this socket can accept connections from any available network interface
PORT = 1432
PORT1 = 1435


message = "notworking"

finalword = []
input_text = ""

root = tk.Tk()


def submit():
    global input_text
    input_text = input_box.get()
    print("User entered:", input_text)
    input_box.delete(0, 'end')
    evoy(input_text)
    game()  # Clear the input box
    


def setup():
    global lives
    global guessword
    global finalword
    global guessl
    global usedlets
    global hiddenusedlets
    global thread
    global thread2
    thread = threading.Thread(target=receive)
    thread2 = threading.Thread(target=send)

    usedletters.clear()
    hang.reset()
    hang.clear()
    hang.hideturtle()
    hang.speed(0)
    hang.pensize(5)
    hang.pencolor("blue")
    # draws hanging station
    hang.penup()
    hang.backward(200)
    hang.right(90)
    hang.forward(100)
    hang.left(90)
    hang.pendown()
    hang.forward(400)
    hang.backward(200)
    hang.left(90)
    hang.forward(300)
    hang.right(90)
    hang.forward(150)
    hang.right(90)
    hang.forward(30)

    lives = 6
    # makes list with word
    finalword = []
    guessword = ("")
    guessl = []
    for i in makeword():
        finalword.append(i)
        guessword = guessword + (i)

    # makes the blank word
    makeguess(guessword, True, None)


def receive():

    global message

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                message = data.decode()
                print(f"Received message: {message}")
                response = "Data received successfully"
                conn.sendall(response.encode())
                s.close()
                setup()
                


def send():
    def multisubmit():

        global multitext

        multitext = multinput_box.get()
        multinput_box.delete(0, 'end')

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(multitext.encode())
            data = s.recv(1024)
            print('Received', repr(data))
            s.close()
            recv_thread = threading.Thread(target=recoi)
            recv_thread.start()


    multinput_box = tk.Entry(root)
    multinput_box.pack()

    multisubmit_button = tk.Button(
        root, text="Enter Multi", command=multisubmit)
    multisubmit_button.pack()

    multinput_box.delete(0, 'end')


def evoy(data):
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the server
        s.connect((HOST, PORT1))
        # Send the data
        s.sendall(data.encode())


def recoi():
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind the socket to the port
        s.bind((HOST, PORT1))
        # Listen for incoming connections
        s.listen()
        while True:
            # Wait for a client to connect
            conn, addr = s.accept()
            with conn:
                while True:
                    # Receive the data
                    data = conn.recv(1024)
                    if not data:
                        # If no more data is received, break out of the loop
                        break
                    # Print the received data
                    print(data.decode())


def multi():
    send_button = tk.Button(root, text="Send word?", command=thread2.start)
    send_button.pack()

    recive_button = tk.Button(root, text="Recive word?", command=thread.start)
    recive_button.pack()


# Create an input box
input_box = tk.Entry(root)
input_box.pack()

# Create an enter button
enter_button = tk.Button(root, text="Enter", command=submit)
enter_button.pack()

start_button = tk.Button(root, text="Start/Restart", command=setup)
start_button.pack()

multi_button = tk.Button(root, text="Multiplayer", command=multi)
multi_button.pack()


# Create a Turtle window
canvas = turtle.Canvas(root, width=1000, height=500)

canvas.pack()

usedletters = turtle.RawTurtle(canvas)
score = turtle.RawTurtle(canvas)
hang = turtle.RawTurtle(canvas)

hang.speed(0)

score.penup()
score.hideturtle()
score.forward(250)
guessl = []
usedlets = ("")
hiddenusedlets = ("")


usedletters.penup()
usedletters.hideturtle()
usedletters.forward(-300)

root.bind('<Return>', lambda event: submit())


with open("words.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))


def makeword():
    global x
    global message
    '''
    if message == "":
        while True:
            global x
            x = random.choice(words)
            if len(x) > 3 and len(x) <= 8:
                print(x)
                return (x)
    else:
        
    '''
    x = message
    return message


def drawbody(bpart):
    global usedlets
    global hiddenusedlets
    if bpart == 5:  # head
        hang.right(90)
        hang.circle(20)
        hang.left(90)
        hang.penup()
        hang.forward(40)
        hang.pendown()
    if bpart == 4:  # body
        hang.forward(100)
    if bpart == 3:  # left leg
        hang.left(45)
        hang.forward(60)
        hang.backward(60)
        hang.right(45)
    if bpart == 2:  # right leg
        hang.right(45)
        hang.forward(60)
        hang.backward(60)
        hang.left(45)
    if bpart == 1:  # left arm
        hang.backward(75)
        hang.left(75)
        hang.forward(60)
        hang.backward(60)
        hang.right(75)
    if bpart == 0:  # right arm
        hang.right(75)
        hang.forward(60)
        hang.backward(60)
        hang.penup()

        hang.home()
        hang.backward(65)
        hang.right(90)
        hang.forward(200)
        hang.left(90)
        hang.pendown()
        hang.pencolor("red")
        hang.write("You Lose \nThe word was: " +
                   x, font=("Arial", 30, "normal"))
        usedlets = ""
        hiddenusedlets = ""

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


def game():
    global hiddenusedlets
    global usedlets
    global lives
    # sets up the game

    # Asks for input for first letter

    pinput = input_text

    print(pinput)
    print(finalword)

    if str(pinput) in str(finalword):

        for i in range(len(finalword)):
            if pinput in finalword:
                finalword.remove(pinput)

        hiddenusedlets = hiddenusedlets + (pinput + ", ")
        makeguess(guessword, False, pinput)

        if not finalword:
            hang.penup()
            hang.home()
            hang.backward(55)
            hang.right(90)
            hang.forward(150)
            hang.left(90)
            hang.pendown()
            hang.pencolor("green")
            hang.write("You win", font=("Arial", 30, "normal"))
            usedlets = ""
            hiddenusedlets = ""
            time.sleep(1.5)

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


if yyy == 0:
    setup()
    yyy = yyy + 1

root.mainloop()


# draw the hangman

# This small project is a reworked version of the one made by Bro Code (https://www.youtube.com/watch?v=V9MbQ2Xl4CE).
# I just wanted to have a tinker around these kinds of applications on python.
from tkinter import *
import random

def next_turn(row, column):
    # To divide the to modes without having a bunch of spaghetti code
    global  Mode
    if Mode == "PvP":
        PvP(row,column)
    elif Mode =="PvE":
        PvE(row,column)

def PvP (row,column):
    #  A basic turn base Function. As one player finishes they're turn it passes to the next player and while
    #  that's happening its checking if either player has won by check_winner conditions
    #
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=("Mode: "+ Mode +" "*10+players[1] + " turn"))

            elif check_winner() is True:
                label.config(text=("Mode: "+ Mode +" "*10+players[0] + " wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=("Mode: "+ Mode +" "*10+players[0] + " turn"))

            elif check_winner() is True:
                label.config(text=("Mode: "+ Mode +" "*10+players[1] + " wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

def PvE (row,column):
    # Works just like PVP the only differences is that
    # since I couldn't make the "bot" go first because of
    # how bare bones it is, so the player will always start to make the ball roll.
    # The "CPU"/"Bot" is just a very simple loop that checks the grids array to see if [x,x] is empty
    # if so place marker if not reset to find one.
    # Very very simple but there wasn't a need for a Tic Tac Toe master AI
    global player
    global Cpu
    global Turn
    Turn = player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        buttons[row][column]['text'] = player

        if check_winner() is False:
            Turn = Cpu

            label.config(text=("Mode: "+ Mode +" "*10+Cpu + " turn"))

        elif check_winner() is True:
            label.config(text=("Mode: "+ Mode +" "*10 +" Player wins"))

        elif check_winner() == "Tie":
            label.config(text="Tie!")

        while True and check_winner() is False :
           R1 = random.randint(0, 2)
           R2 = random.randint(0, 2)
           if buttons[R1][R2]['text'] == "":
            buttons[R1][R2]['text'] = Cpu
            if check_winner() is True:
              label.config(text=("Mode: "+ Mode +" "*10+"Cpu wins"))
            elif check_winner() == "Tie":
              label.config(text="Tie!")
            break

        if check_winner() is False:
           Turn = player
           label.config(text = "Mode: "+ Mode +" "*10+ player + " turn")

def check_winner():
    # Checks if a row/column connects by the text in the array (x or o)
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    # Tie checker
    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False

def empty_spaces():
    # As the name implies it checks every space in the array to see if there's any place without a mark
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():
    # Resets everything from the players mark to the board
    global player
    global Cpu

    Cpu = random.choice(players)
    player = ""

    if Cpu == players[0]:
        player = players[1]
    else:
        player = players[0]

    label.config(text = "Mode: "+ Mode +" "*10+ player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

def modes():
    # A small way and dumb way to change the modes
    # if its in PvE the change it to PvP and vice versa then reset the board
    global Mode

    if Mode == "PvE":
        Mode = "PvP"
    else:
        Mode = "PvE"
    new_game()

# All the essential Variables needed
window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","o"]
Cpu = ""
player = ""
Mode = "PvE"

# Hoe the mode is first set
if Mode == "PvP" :

    player = random.choice(players)

elif Mode == "PvE" :

    Cpu = random.choice(players)

    if Cpu == players[0] :

       player = players[1]
    else :

       player = players[0]


#The grid
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
#Buttons & Labels/Text
label = Label( text = "Mode: "+ Mode +" "*10+ player + " turn", font=('consolas',19))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")
switch_button = Button(text="Switch modes", font=('consolas',15), command=modes)
switch_button.pack(side= "top")
frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)



window.mainloop()
# - *- coding: utf- 8 - *-
#lipan
#C:\Users\Lee\Documents\Notepad\hardwaypython
from sys import exit

def gold_room():
    print "This room is full of gold.How much do you take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("man,type a number")

    if how_much < 50:
        print "U A Not greedy,you win"
        exit(0)
# exit(0)表示正常退出，其他的1，2,3表示各种与自己对应的错误退出
# use different values other than 1 to differentiate between different kind of errors.
    else:
        dead("you greedy bastard!")

def bear_room():
    print "There is a bear here"
    bear_move = False
    while True:
        next = raw_input("> ")
        if next == "take money":
            dead("The bear looks at you the slaps your face off")
        elif next == "taunt bear" and notbear_move:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_move:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door"and bear_move:
            gold_room()
        else:
            print "I'm got no idea what that means."

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()

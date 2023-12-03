#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:21:30 2023
@author: Krista Brehm
Python Guessing Game with Leaderboard

This assignment creates a guessing name where you are given a square
root value of a number between 10-100 and must guess the integer. When the game
ends, the current leaderboard is printed.
"""

#import statements
import random
import math

#boolean variable used to control when the program runs vs when
#the game ends
gameover = False

#this function is responsible for getting the input from the user
#and performing exception handling if it is not an int or inside the range 10-100
def GetInput(s):
    while True:
        try:
            num = int(input(s))
            if 10 <= num <= 100:
                return num
            else:
                print("Must be a number from 10 to 100.")
        except ValueError:
            print("Must be a number from 10 to 100.")

#this is the main function. it is responsible for the loop that the user plays
#to guess a number. this function uses conditionals to address the users guess
#compared to the correct guess. it additionally keeps count of the number of guesses
#they make, as well as there name to later store in the leaderboard
def PlaySquareRootGame():
    global gameover
    leaderboard = {}
    num_guesses = 0

    while not gameover:
        guessingnumber = random.randint(10, 100)
        squareroot = math.sqrt(guessingnumber)

        print(squareroot, "is the square root of what number? ")

        while not gameover:
            userguess = GetInput("")
            num_guesses += 1

            if userguess < guessingnumber:
                print("Too low, guess again: ")
            elif userguess > guessingnumber:
                print("Too high, guess again: ")
            else:
                print("You got it, baby!")
                break

        username = input("Good game! What is your name? : ")
        if username not in leaderboard:
            leaderboard[username] = num_guesses
        else:
            leaderboard[username] += num_guesses
        
        #in the case the user decides to quit, the leaderboard
        #is then printed with all the player's names and scores
        k = input("Press 'q' to quit or any key to continue: ")
        if k.lower() == 'q':
            gameover = True
            print("Scoreboard\n", "__________________")
            for player, score in leaderboard.items():
                print(f"{player} {score}")
                print("__________________")

            #then, the current leader is determined and that player's name is printed
            winner = min(leaderboard, key=leaderboard.get)  
            print("Congratulations,", winner, ", you have the best score!")
            break
        

#====================================================================
while not gameover:
    print("Welcome! Press 'q' to quit or any key to continue: ")
    c = input()
    #as long as the user does not enter 'q' the game continues on and on
    if c.lower() == 'q':
        break
    else:
        gameover = False
        PlaySquareRootGame()

print("Bye Bye!")


import dictionary
import json
import random

#dictionary and alphabet
dictionary = json.loads(dictionary.dictionary)
possibleConsonants = "bcdfghjklmnpqrstvwxyz"
possibleVowels = "aeiou"

#game variables
score = 0
lives = 3
round = 0
started = 0
used = []
required = []
gameover = 0

def requiredLetters():
    # TODO: set up random letter selection and return... flush out required[] after use
    return required

def isValid(word):
    isInDictionary = 0
    # TODO: implement required letters
    if (word in dictionary):
        isInDictionary = 1
    return isInDictionary

def updateScore(word):
    if ((isValid(word) == 1) & (len(word) > round)):
        score += (len(word) + (len(word) - round))
    elif ((isValid(word) == 0) & (len(word) < round)):
        score -= len(word)
        lives -= 1
    elif ((isValid(word) == 0) & (len(word) > round)):
        score -= int(len(word)/2)
        lives -= 1
    return score

def checkLives():
    if lives == 0:
        gameover = 1
        return gameover

import dictionary
import json

#dictionary and alphabet
dictionary = json.loads(dictionary.dictionary)
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]

#game variables
score = 0
lives = 3
round = 0
started = 0
used = []

def isValid(word):
    isInDictionary = 0
    if (word in dictionary):
        isInDictionary = 1
    return isInDictionary

def updateScore(score):
    #check word size
    return 0
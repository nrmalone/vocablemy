import dictionary
from tkinter import *
import json
import random

root = Tk();
root.title("Vocablemy test")

dictionary = json.loads(dictionary.dictionary)

possibleConsonants = "bcdfghjklmnpqrstvwxyz"
possibleVowels = "aeiou"

def randomConsonant():
    consonant = random.choice(possibleConsonants)
    return str(consonant)

def randomVowel():
    vowel = random.choice(possibleVowels)
    return str(vowel)

word = "supercalifragilisticexpialidocious"

consonant = randomConsonant()
vowel = randomVowel()

def testForRandom(consonant, vowel):
    if (consonant in word) & (vowel in word):
        return 1

randomLabel = Label(root, text=(consonant + " " + vowel))
randomLabel.grid(row=0,column=0)

testLabel = Label(root, text=testForRandom(consonant, vowel))
testLabel.grid(row=1,column=0)

root.mainloop()
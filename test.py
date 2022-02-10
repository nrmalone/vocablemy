import dictionary;
from tkinter import *;
import json;

root = Tk();
root.title("Vocablemy test")

dictionary = json.loads(dictionary.dictionary)

word = "testing"

def isValid(word):
    isInDictionary = "no"
    if (word in dictionary):
         isInDictionary = "yes"
    return isInDictionary

testLabel = Label(root, text=isValid(word))
testLabel.grid(row=0,column=0)

root.mainloop()
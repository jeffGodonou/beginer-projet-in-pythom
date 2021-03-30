#-*- coding: utf8 -*-
import random

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]

def getRandomItem(list):
    random_number = random.randint(0, len(list) - 1)
    item = list[random_number]
    return item

user_answer = 'A'

while user_answer != "B":
    user_answer = input('Tapez entrer pour connaître une autre citation ou B pour quitter le programme.')
    print(getRandomItem(quotes))    

for item in characters:
    item.capitalize()

"{} a dit : {}".format("Babar", "Tout n'est pas cirrhose dans la vie, comme dit l'alcoolique.")
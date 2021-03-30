# code inspiré de openclassroom 
# https://openclassrooms.com/fr/courses/4262331-demarrez-votre-projet-avec-python/4264121-bonus-collectez-des-citations-automatiquement-avec-scrapy

#-*- coding: utf8 -*-
import json
import random

# Return a List from a JSON file
def read_value_from_json(file, key):
    values = []
    with open(file) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
    return values

# Return a sentence from a JSON file
def clean_strings(sentences):
    cleaned = []
    for sentence in sentences:
        cleaned.append(sentence.strip())
    return cleaned


#Get a random item from a list
def getRandomItem(list):
    random_number = random.randint(0, len(list) - 1)
    item = list[random_number]
    return item

# Get a random value from a JSON
def random_value(source_path, key):
    all_values = read_value_from_json(source_path, key)
    clean_values = clean_strings(all_values)
    return getRandomItem(clean_values)

# Get a random quote
def random_quote():
    return random_value("quotes.json", "quote")

# Get a random character
def random_character():
    return random_value("characters.json", "character")


# Print a random sentence.

def print_random_sentence():
    rand_quote = random_quote()
    rand_character = random_character()
    print(">>>> {} a dit : {}".format(rand_character, rand_quote))

def main_loop():
    while True:
        print_random_sentence()
        message = ('Voulez-vous voir une autre citation ?'
                   'Pour sortir du programme, tapez [B].')
        choice = input(message).upper()
        if choice == 'B':
            break

if __name__ == '__main__':
    main_loop()
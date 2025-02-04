"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Veronika Semeradova
email: semeradova.veronika@gmail.com
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


user = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
user_1 = input("user: ")
password_1 = input("password: ")
print("-" * 40)
if user.get(user_1) == password_1:
    print(f"Welcome to the app, {user_1}\nWe have {len(TEXTS)} texts to be analyzed.")
    print("-" * 40)
else:
    print("Unregistered user, terminating the program...")
    exit()

if len(TEXTS) == 0:
    print("0 texts to be analyzed.")
    exit()

text_1 = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
print("-" * 40)
if not(text_1.isnumeric()):
    print("Wrong character.")
    exit()
elif int(text_1)>3 or int(text_1)<1:
    print("Wrong number.")
    exit()

clean_text = ''.join(c for c in TEXTS[int(text_1)-1] if c.isalnum() or c.isspace())

split_text = clean_text.split()
number = 0
words = 0
upper = 0
allupper = 0
alllower = 0
suma_all = 0

for idx in range(len(split_text)):
    if split_text[idx].isnumeric():
        number = number + 1
        suma_all = suma_all + int(split_text[idx])
    elif split_text[idx][0].isupper():
        upper = upper + 1
    if split_text[idx].isupper():
        allupper = allupper + 1
    if split_text[idx].islower():
        alllower = alllower + 1

words = len(split_text)
print("There are", words, "words in the selected text.")
print("There are", upper, "titlecase words.")
print("There are", allupper, "uppercase words.")
print("There are", alllower, "lowercase words")
print("There are", number, "numeric strings.")
print("The sum of all the numbers", suma_all,".")
print("-" * 40)
print("LEN|", "   ", "OCCURENCES", "   ", "|NR.")
print("-" * 40)

dictionary_words = split_text
length_words = {word: len(word) for word in dictionary_words}
unique_lenghts = set(length_words.values())
dict = {}
for value in unique_lenghts: 
    dict[value] = 0
for word in split_text:
    dict[len(word)] +=1


for word_lenghts in dict:
    print(f"{word_lenghts:2} |", end="")
    for i in range(dict[word_lenghts]):
      print("*", end="")
    print(f"{"|":>{21-dict[word_lenghts]}s}",dict[word_lenghts])
    


"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lukas Korenek
email: koreneklukas@seznam.cz
"""
import string
# Základní text
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
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
# print("ahoj" * 50)

# Funkce na provádění analýzy nad daným textem
def machine_analyze(text_index):
	words = len(TEXTS[text_index].split())
	print(f"There are {words} words in the selected text.")

	count_title = 0
	count_upper = 0
	count_lower = 0

	for word in TEXTS[text_index].split():
		if word.istitle():
			count_title += 1
	print(f"There are {count_title} titlecase words.")


	for word in TEXTS[text_index].split():
		if word.isupper():
			count_upper += 1
	print(f"There are {count_upper} uppercase words.")

	for word in TEXTS[text_index].split():
		if word.islower():
			count_lower += 1
	print(f"There are {count_lower} lowercase words.")

	count_numeric = 0
	sum_all_numbers = 0

	for number in TEXTS[text_index].split():
		if number.isdigit():
			count_numeric += 1
			sum_all_numbers += int(number)

	print(f"There are {count_numeric} numeric strings.")
	print(f"The sum of all the numbers {sum_all_numbers}")
	print("-" * 40)
	print(
		"LEN|    OCCURENCES      |NR."
	)
	print("-" * 40)

	slovnik = {}
	for slovo in TEXTS[text_index].split():
		slovo = slovo.strip(string.punctuation)
		delka = (len(slovo))

		slovnik[delka]=slovnik.get(delka, 0) + 1

	for delka in sorted(slovnik):
		pocet = slovnik[delka]
		print(f"{delka:>2} | {"*" * pocet:<18} | {pocet}")





# Dictionary uživatelů
registered_users = {
	"bob":"123",
	"ann":"pass123",
	"mike":"password123",
	"liz":"pass123"
}

# User input
username = input("username: ").lower()
pwd = input("Password: ").lower()

print("-" * 40)

if username in registered_users and registered_users[username] == pwd:
	print(f"Welcome to the app, {username} \n"
		  "We have 3 texts to be analyzed.")
	print("-" * 40)



	choice_text = input(
		"Enter a number btw. 1 and 3 to select: "
						)
	print("-" * 40)



	if not choice_text.isdigit():
		print("Musíš zadat číslo. Program ukončen.")
		exit()

	choice = int(choice_text)


	if choice == 1:
		machine_analyze(0)
	elif choice == 2:
		machine_analyze(1)
	elif choice == 3:
		machine_analyze(2)
	else:
		print("Zadané číslo není v zadání.")

else:
	print("Unregistered user, terminating the program...")


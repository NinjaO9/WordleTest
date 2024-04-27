import requests, random

wlist = (str(requests.get("https://www.mit.edu/~ecprice/wordlist.10000").content)).split(r"\n")
word = wlist[random.randint(0, len(wlist))]
while len(word) != 5:
    word = wlist[random.randint(0, len(wlist))]
word = word.lower()
attempt_num = 6

print(f"Welcome to WORDLE! \n Type a 5 letter word to get started! \n  CAPITAL letters mean the letter is perfectly in place. \n  lowercase letters mean the letter is in the word, but in the wrong place")

def checkvalidity(guess: str) -> bool:
    global message
    message = ""
    if len(guess) != 5:
        message += ("ERROR: The word must be 5 letters! \n")
    if not guess.isalpha():
        message += ("ERROR: The word must only be letters! \n")
    return (message == "")

for i in range(attempt_num):
    index = 0
    obtained = ["_","_","_","_","_"]
    while True:
        guess = str(input(f"\n {i + 1}/{attempt_num}: ")).strip().lower()
        if not checkvalidity(guess):
            print(f"Invalid Word! \n{message}")
        else:
            break

    
    for letter in list(guess.lower()):
        if letter in list(word):
            obtained[index] = letter.lower()
        if letter == word[index]:
            obtained[index] = letter.upper()
        index += 1
    
    for item in obtained:
        print(item, end="")

    if guess.lower() == word.lower():
        print(f"\n Word guessed! \n'{word}'")
        break


else:
    print(f"\n Too bad! \n The word was: '{word}'")

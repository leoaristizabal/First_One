print("Guessing Game")
print("************* \n")

print("You have three attempts to guess the secret word (animal) \n")

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess word: ")
        guess_count += 1 #cuenta los intentos
    else: 
        out_of_guesses = True

if out_of_guesses: 
    print("Out of Guesses, YOU LOSE!")
else:
    print("YOU WIN!")


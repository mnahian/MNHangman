import random


def hangman():
    word = random.choice(["Tiger", "Ironman", "Jervis",
                          "KFC", "BFC", "PizzaHut",
                          "Julia", "Angelina", "Yumi",
                          "UncleP"])
    validLetters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    userguess = ""

    while len(word) > 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in userguess:
                main = main + letter
            else:
                main = main + "_" + " "
        if main == word:
            print(main)
            print("You win!!")
            break
        print("Guess a word: ", main)
        guess = input()

        if guess in validLetters:
            userguess = userguess + guess
        else:
            print("Enter a valid charecter")
            guess = input()
        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print(" ---------- ")
            if turns == 8:
                print("8 turns left")
                print(" ---------- ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print(" ---------- ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print(" ---------- ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print(" ---------- ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print(" ---------- ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print(" ---------- ")
                print("    \O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print(" ---------- ")
                print("    \O/     ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print(" ---------- ")
                print("    \O/|     ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last chance to live")
                print(" ---------- ")
                print("    \O/_|    ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("you just let a man die")
                print("     O_|    ")
                print("    /|\     ")
                print("    / \     ")
                break


name = input("Enter your name: ")
print("Welcome " + name)
print("------------------")
print("Try to guess the word in less than 10 attempts")
hangman()
print()

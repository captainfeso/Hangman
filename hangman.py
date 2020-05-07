import random


def hangman():
    word_list = ["Takudzwa", "Simbarashe", "chibhanguza"]
    random_num = random.randint(0,2)
    word = word_list[random_num]

    wrong = 0

    stages = [" ",
              "----------     ",
              "|         |    ",
              "|         0    ",
              "|        /|\   ",
              "|         /\   ",
              "|              "
              ]
    remaining_letters = list(word)
    board = ["___"]*len(word)
    win = False
    print("Welcome to Hangman")

    while wrong<len(stages)-1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg)

        if char in remaining_letters:
            cind = remaining_letters.index(char)
            board[cind] = char
            remaining_letters[cind] = "$"

        else:
            wrong = wrong +1
        print((" ".join(board)))

        e = wrong +1
        print("\n".join(stages[0:e]))
        if "___" not in board:
            print("You won!!!!!!")
            print(" ".join(board))
            win = True
            break
    if not win:
            print("\n".join(stages[0:wrong]))
            print("You suck!! The word was {}.".format(word))
hangman()
        
    


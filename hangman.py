
import random
from visuals import lives_visual_dict
l = ["mumbai", "pune", "pradesh", "vashi"]


def play():
    word = random.choice(l)
    lives = 0
    li = []
    done = False

    while not done:
        for i in word:
            if i in li:
                print(i, end="")
            else:
                print("-", end=" ")

        print("")

        en = input("enter the letter :: ").lower()
        li.append(en)

        if en not in word:
            lives = lives + 1.
            if lives < 6:
                print(lives_visual_dict[lives])
                print("guess the correct word")
            if lives == 6:
                print("you lost the game\n")
                print("word was : " + word)
                n = input("do u want to play again :: ").upper()
                if n == "YES":
                    play()
                else:
                    exit()

        for m in word:
            if m not in li:
                done = False
            else:
                done = True

    if done:
        print("hey you won")
        print("word is :: " + word)
        n = input("do u want to play again :: ").upper()
        if n == "YES":
            play()
        else:
            exit()
    else:
        print("fuck u")


play()


import random
from visuals import lives_visual_dict
list_of_word = ["mumbai", "pune", "pradesh", "vashi"]

print("Lets play hangman !!!")
print("Fill up the hyphens ! \n")


def play():
    word = random.choice(list_of_word)
    lives = 0
    guesses = []
    done = False

    while not done:
        for letter in word:
            if letter in guesses:
                print(letter, end=" ")
            else:
                print("-", end=" ")

        print("\n")

        guess_letter = input("guess the letter :: ").lower()

        if guess_letter in guesses:
            print(f"letter '{guess_letter.upper()}' is already guessed")

        guesses.append(guess_letter)

        if guess_letter not in word:
            lives = lives + 1.
            if lives < 6:
                print(lives_visual_dict[lives])
                print(
                    f"guess the correct letter {int(6-lives)} chances left. ")

            if lives == 6:
                print("you lost the game\n")
                print("word was : " + word)
                n = input("do u want to play again :: ").upper()
                if n == "YES":
                    play()
                else:
                    exit()

        for letter in word:
            if letter not in guesses:
                done = False
            else:
                done = True

    if done:
        print("hey you won :) ")
        print("word is :: " + word)
        n = input("do u want to play again ? :: ").upper()
        if n == "YES":
            play()
        else:
            exit()


play()

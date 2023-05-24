import random
import hangmanWordList
import hangmanArt

print(hangmanArt.logo)

chosen_word = random.choice(hangmanWordList.word_list)
word_length = len(chosen_word)
lives = 6

display = []
for letter in chosen_word:
    display += "_"

end_of_game = False

while not end_of_game:
    print(f"Your word is {len(chosen_word)} letters long.")
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You've already guessed this letter")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"Your word was {chosen_word}")
            print("You Lose. Game Over")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter


    print(display)

    #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangmanArt.stages[lives])
import random
import hangman_words
import hangman_art

count = 7
word_list = hangman_words.word_list
end_of_game = False
# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
keys_list = list(word_list.keys()) #creating lists of keys from word_list dectionary
random_word = random.choice(list(word_list.keys())) #chosing random word from the list
description_list = list(word_list.values()) #creating value list from the dectionary
key_index = keys_list.index(random_word) #getting the index of random word in key_list
description = description_list[key_index] #choosing description from description list doe to index of random word
blanked = [  "-"  for  _  in random_word]  # Using list comprehension to create a list of dashes

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
print(hangman_art.logo)
print(f"\n\n{description}")
print(f'\n\n{"".join(blanked)}')



while not end_of_game:
    
    player_guess = input("\n\nPlease enter a letter:  ").lower()
    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    if player_guess in random_word:
        for i in range(len(random_word)):
            if random_word[i] == player_guess:
                blanked[i] = player_guess
    
    else:
        print("\nWrong!!!")
        count -= 1
        print(hangman_art.stages[count - 1])
        if count == 1:
            print("\n\nYou are hanged🪢")
            print(f"\n\nyour word was {random_word}")
            break

    print(" ".join(blanked))
    if "-" not in blanked:
        end_of_game = True
        print("\n\nYou won")

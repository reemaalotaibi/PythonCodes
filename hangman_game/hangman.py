from words_list import the_words
import random

"""
Hang man game
A brief explanation for how this works:
    1- the computer will choose a word at random from the word list. 
    2- the program will exclude words combined with dashes, -.
    3- define it's length and display it to the player 'user'.
    4- replace the word's letters with dashes and displays it to the user
    5- the play will have 6 lives, meaning that after 6 wrong guesses the program will
        terminate, display the word and the player loses.
    6- the player's guesses are either letters or words
    7- if the player entered an invalid guess he/she will be notified and no lives 
        will be deducted
    8- the correct guesses of the word will be shown in their places instead of the dashes
        to make it easier for the player to know what letters he/she guessed and their 
        positions in the word.
    9- both correct guesses and wrong ones will be stored in lists, so the player can keep 
        track of which letters he/she has chosen
    10- all player's letters will be changed to lower case letters to make it readible by the program
    11- if the player guessed all the letters right he/she will win.
"""
#this for loop will execlude words that have dashes, - , in them.
#then choose a word at random
for word in the_words: 
    if '-' not in word:
        word_at_random = random.choice(the_words)
print(word_at_random)


word_len = len(word_at_random)
# print('The word has ', word_len, ' characters.')

word_hashing = '-' * word_len
print('The word has ', word_len, ' characters. \n', word_hashing)



mistakes_allowed = 6
guess_is = False
guessed_inputs = []

while guess_is or mistakes_allowed != 0 :
    player_letter = input('What\'s your guess? ')

    if len(player_letter) == 1:
        if player_letter in word_at_random:
            if player_letter not in guessed_inputs:
                guessed_inputs.append(player_letter)
                print('Correct Guess!')
                word_formation = list(word_hashing)
                #places the character in its position in the word
                indices = [i for i, letter in enumerate(word_at_random) if letter == player_letter]
                for index in indices:
                    word_formation[index] = player_letter
                word_hashing=''.join(word_formation)
                print(word_hashing + '\n')
                #if all dashes were replaced with characters
                #return True, which will stop the while loop
                if '-' not in word_hashing:
                    guess_is = True
                    print('You guessed the word!')
                    print('Congrats! YOU WON!')

                # print(guessed_inputs)
            elif player_letter in guessed_inputs:
                print('You already tried this letter')
                print(word_hashing + '\n')

        elif player_letter not in word_at_random:
            if player_letter not in guessed_inputs:
                guessed_inputs.append(player_letter)
                mistakes_allowed -= 1
                print('Wrong Guess, you have {} lives left'.format(mistakes_allowed))
                print(word_hashing + '\n')
            elif player_letter in guessed_inputs:
                print('You already tried this letter')
                print(word_hashing + '\n')


    # elif len(player_letter) > 1 and player_letter!= word_at_random:
    #     if player_letter in guessed_inputs:
    #         print('You already tried this word')
    #         print(word_hashing + '\n')
    #     else:
    #         guessed_inputs.append(player_letter)
    #         print('Wrong Guess')
    #         print(word_hashing + '\n')
        

    elif len(player_letter) > 1 and (len(player_letter) < len(word_at_random) or len(player_letter) != len(word_at_random)):
        if player_letter in word_at_random:
            guessed_inputs.append(player_letter)
            print('Correct Guess')
            word_formation = list(word_hashing)
                #places the character in its position in the word
            indices = [i for i, letter in enumerate(word_at_random) if letter == player_letter]
            for index in indices:
                word_formation[index] = player_letter
            word_hashing=''.join(word_formation)
            print(word_hashing + '\n')
            #if all dashes were replaced with characters
            #return True, which will stop the while loop
            if '-' not in word_hashing:
                guess_is = True
                print('You guessed the word!')
                print('Congrats! YOU WON!')

        else: 
            mistakes_allowed -=1
            guessed_inputs.append(player_letter)
            print('Wrong guess, you have {} lives left'.format(mistakes_allowed))
            print(word_hashing + '\n')

    if len(player_letter) == len(word_at_random) and player_letter != word_at_random:
        mistakes_allowed -=1
        guessed_inputs.append(player_letter)
        print('Wrong Guess, you have {} lives left'.format(mistakes_allowed))
        print(word_hashing + '\n')

    elif len(player_letter) == len(word_at_random) and player_letter == word_at_random :
        guess_is = True
        word_hashing = word_at_random
        print('You guessed the word!')
        print('Congrats! YOU WON!')
        
        break
            
else:
    print('You ran out of lives!')
    print('the word is ', word_at_random)


from words_list import the_words
import random


#this for loop will execlude words that have dashes, - , in them.
#then choose a word at random
for word in the_words: 
    if '-' not in word:
        word_at_random = random.choice(the_words)


#stores the length of the word chosen at random
word_len = len(word_at_random)

#stores dashes equalling the length of the random
word_hashing = '-' * word_len
#then print the dashes representing the word
print('The word has ', word_len, ' characters. \n', word_hashing)


#the player has 6 allowed mistakes, 1 for the head, 2 for the hands, 2 for the legs, and one for the abdomen.
mistakes_allowed = 6

#initially the player's guess is False
guess_is = False
#this list will store all the letters and the words the player guessed, regardless of if they were correct of wrong.
guessed_inputs = []

#As long as the player's guesses don't match the WHOLE word
    #or as long as his/her mistakes are greater than 0, the program will run
    # if the player guessed the WHOLE word or if he/she ran out of lives -consumed all the mistakes allowed-
    #the program will terminate
while guess_is or mistakes_allowed > 0 :
    #prompt the player to enter inputs(letters or a word)
    player_letter = input('What\'s your guess? ')
    #the letter's will be changed to lower cases
    player_letter = player_letter.lower()
    #if the player entered a single letter (char)
    if len(player_letter) == 1:
        #if the letter is in the random word
        if player_letter in word_at_random:
            #if the letter is not stored in the guessed inputs letter
            if player_letter not in guessed_inputs:
                #the letter will added to the list
                guessed_inputs.append(player_letter)
               
                print('Correct Guess!')
                
                #create a list of the dashes, -. The length of the list equals to the
                #length of the random word. Each dash is treated as a separate string.
                word_formation = list(word_hashing)
                #places the character in its position in the word
                indices = [i for i, letter in enumerate(word_at_random) if letter == player_letter]
                for index in indices:
                    word_formation[index] = player_letter
                word_hashing=''.join(word_formation)
                print(word_hashing + '\n')
                
                #if all dashes were replaced with characters
                #return True, which will stop the while loop
                #and the player wins
                if '-' not in word_hashing:
                    guess_is = True
                    print('You guessed the word!')
                    print('Congrats! YOU WON!')
            
            #otherwise, if the player already trried this letter
            #meaning that the letter is in the guessed inputs list
            elif player_letter in guessed_inputs:
                #no pealties on choosing a letter that's already chosen
                print('You already tried this letter')
                print(word_hashing + '\n')
           
        #if the player guessed a wrong letter
        elif player_letter not in word_at_random:
            #if the letter wasn't in the guessed inputs list
            if player_letter not in guessed_inputs:
                #the letter will be added to the list
                guessed_inputs.append(player_letter)
                #and one mistake will be counted
                mistakes_allowed -= 1
                
                print('Wrong Guess, you have {} lives left'.format(mistakes_allowed))
                print(word_hashing + '\n')
             
            #the player already tried this letter
            elif player_letter in guessed_inputs:
                #no mistakes will be counted
                print('You already tried this letter')
                print(word_hashing + '\n')

    
    """This part of the code is supposed to accept multiple letters
        if any of the letters was in the random word, the player should be notifed, and mistakes
        should be counted for incorrect letters inputted.
        I guess this works by splitting the letters the user inputted then working on each letter separately
        
        I haven't found out yet how to do it."""
    elif len(player_letter) > 1 and len(player_letter) != len(word_at_random):
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
    
    #if the player inputted a word with same length as the random 
    #but it was wrong or some letters were wrong.
    #a mistake will be counted
    elif len(player_letter) == len(word_at_random) and player_letter != word_at_random:
        mistakes_allowed -=1
        guessed_inputs.append(player_letter)
        print('Wrong Guess, you have {} lives left'.format(mistakes_allowed))
        print(word_hashing + '\n')
    
    #if the player inputted the word
    elif len(player_letter) == len(word_at_random) and player_letter == word_at_random :
        #the player's guess will change to True, which will terminate the program
        guess_is = True
        #the dashes will be replaced with the word's letters
        word_hashing = word_at_random
        print('You guessed the word!')
        print('Congrats, YOU WON!')
        
        break
 #if the player ran out of lives
#the program will terminate
#and the word will be displayed.
else:
    print('You ran out of lives!')
    print('the word is ', word_at_random)


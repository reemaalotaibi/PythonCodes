import random
from words_list import the_words

#the computer has to return a word at random from the words list -done
#tell the user how long this the word -done
#prompt the user to enter a letter/char -done
# if the character was in the word -done
#return true and it's place in the word -done
#if the character wasn't in the word -done
#return false -done
#count a mistake -done

#return a word at random from the list
computer_word = random.choice(the_words)
#stores the length of the word
letters = len(computer_word)

#returns the the length of the word and dashes 'hashing'
word_hashing = '-'*letters
print('the word has {} letters'.format(letters),word_hashing)


#create a list to store the guessed letters
inputed_letters = []
#create a list to store the guessed words
inputted_words =[] 

#6 mistakes before showing the word and ending the game. 6 or head, both hands, both legs and abdomen
mistakes = 6

#by default the user guess will initially false
user_guess = False


#while the user guess is not correct and the mistakes are more than 0
while not user_guess and mistakes > 0:
    #take input from the user
    user_char=input('What\'s your character?')
    #we have 3 assumptions

    #the user entered a single character and it's an alphabet
    #and this for loop has 3 assumptions 

    if len(user_char) == 1 and user_char.isalpha(): #think about getting rid ofthis code line
            #the user entered a character he/she already entered
        if user_char in inputed_letters:
            print('You already guessed this letter!')
            #the character is not the word
        elif user_char not in computer_word:
            print('{} is wrong. Try again. Be careful you only have {} chances left'.format(user_char,mistakes))
            mistakes -= 1
            inputed_letters.append(user_char)
            #the character is in the word
        else:
            print('{} is in the word!'.format(user_char))
            #replace a dash with the guessed character
            word_formation = list(word_hashing)
            #places the character in its position in the word
            indices = [i for i, letter in enumerate(computer_word) if letter == user_char]
            for index in indices:
                word_formation[index] = user_char
            word_hashing=''.join(word_formation)
            #if all dashes were replaced with characters
            #return True, which will stop the while loop
            if '-' not in word_hashing:
                user_guess = True
        

    #or if the user input's length equals the computer's word length
    # and the user input's is alphabets
    elif len(user_char) == len(computer_word) and user_char.isalpha():
        if user_char in inputed_letters:
            print('You already guessed the word', user_char)
            #the user guessed a wrong letter
        elif user_char != computer_word:
            print(user_char, 'is not the word.')
            #decrement a life
            mistakes-=1
            #add the character to the list of guessed letters
            inputted_words.append(user_char)
            
         #the user guessed word   
        else:
            user_guess = True
            #replace the dashes with the word
            word_hashing = computer_word
    #the user entered an invalid character
    else:
        print('not a valid guess')
        print(word_hashing + '\n')
#
if user_guess:
    print("Congrats, YOU GUESSED THE WORD!")
else:
    print('Ran out of lives!. the word was {}.'.format(computer_word))
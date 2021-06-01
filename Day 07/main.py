import random
from replit import clear
from hangman_art import stages, logo
from hangman_words import word_list
from hearts import hearts


#-----Generate the chosen word for the game
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#set the flag for while loop and define variables for the game
end_of_game = False
lives = 6
display = []
guessed_letters = []
wrong_letters = []


#Create blanks for the length of the chosen word
for _ in range(word_length):
    display += "_"

#Print the logo and the stage
print(logo)
print(stages[lives])


#Testing code
# print(f'Pssst, the solution is {chosen_word}.')




#Run The Game
while not end_of_game:
    #Testing code
    # print(f'Pssst, the solution is {chosen_word}.')
    guess = input("Guess a letter: ").lower()
    clear() #Clear the screen so that game doesnt scroll
    print(logo) #Reprint logo to keep it on top of screen after clear

      

    #Add the guessed letter to the list for display
    guessed_letters.append(guess)
    print(f"You have guessed the following letters: \n{' '.join(guessed_letters)}\n\n")





    #Check to see if user has guessed the letter already
    if guess in display:
      print(f'You have guessed {guess} already, try again.')

    #--------If user guesses correctly-------
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

      


    #--------If user guesses incorrectly-------

    #If user previously guessed the letter but its wrong
    if guess not in chosen_word and guess in wrong_letters:
      print(f'You chose {guess}, you have already chosen that letter, try again.\n')

    #If user has not guessed the letter and its wrong
    elif guess not in chosen_word:
        wrong_letters.append(guess)
        lives -= 1
        print(f'You chose {guess}, that is not in the word. You lose a life.\n\n')

        if lives == 1:
          print(f'{hearts[lives]} life remains!\n\n')

        if lives > 1 :
          print(f'{hearts[lives]} lives remaining!\n\n')
        
        
        if lives == 0:
            end_of_game = True
            print("You are out of lives, you lose.\n ")
            print(f'Thanks for playing, the word was: {chosen_word}\n\n')



    #Join all the elements in the list and turn it into a String instead of showing a list
    print(f"{' '.join(display)}")



     
            
    #Reprint the stage after screen clear
    print(stages[lives])

     #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        if lives == 6:
          print(f'{hearts[lives]} lives remain!')
          print("\nFlawless Victory!\n\n")
        if lives == 5:
          print(f'{hearts[lives]} lives remain!')
          print("\nYou won, but your neck will hurt tomorrow\n\n")
        if lives == 4:
          print(f'{hearts[lives]} lives remain!')
          print("\nYou won, TIS BUT A SCRATCH\n\n")
        if lives == 3:
          print(f'{hearts[lives]} lives remain!')
          print('\nYou won, A scratch?! YOUR ARMS OFF!\n\n')
        if lives == 2:
          print(f'{hearts[lives]} lives remain!')
          print("\nYou won, tis just a flesh wound!\n\n")
        if lives == 1:
          print(f'❤️ life remains!')
          print("\nYou won by the skin of your teeth!\n\n")
          

      
      

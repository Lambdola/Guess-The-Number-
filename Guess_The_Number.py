import random as rd

"""
 A interactive logic game where you must guess a number based on clues.
 """
 
#Controls the number of digits to be guessed
NUM_DIGITS = 3  
#Controls the number of attempts(trials)
MAX_GUESSES = 10
#Controls the string to be printed when correct
VALIDATION = "Correct! You got it"
#Controls the main game While-loop,line 83. Try changing the value to False and see what happens.
KEY = True
#Controls the number of "*" that accompanies the 'Do you want to play again' line.
SEPARATION = 40 

print(f"I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.\n".upper())

print("""
Try to guess the number in 10 attempts.
When I Say;          That means:
# Pico:              One digit is correct but in the wrong position. 
# Fermi:             One digit is correct and in the right position. 
# Bagels:            No digit is correct.

For example, if the secret number was 248 and your guess was 843, the 
clues would be Fermi Pico
""")

  
def getSecretNum():
    #Create a list of numbers from 0 to 9.
    numbers = [str(i) for i in range(10)]
    
    #Shuffles the created list of numbers.
    rd.shuffle(numbers)
    
    #print(numbers)  #remove the '#' before the print(numbers) to reveal the shuffled numbers when code is run..
    
    #Gets the first NUM_DIGITS digits of the shuffled list and uses it as the SecretNum.
    SecretNum = ""
    for i in range(NUM_DIGITS):
        SecretNum += numbers[i]
    return SecretNum 
        

check = getSecretNum()
#print(check)  #remove the "#" before the print(check) to reveal the SecretNum. <CHEATING>


# Returns strings of  'Pico', 'Fermi', 'Bagels' as Clues for a given guess."""
def getClues(guess, check=check):
   
    #if given guess is equal to the SecretNum
    if guess == check:
        return 'FermiFermiFermi'
    #if given guess is not equal to the SecretNum
    else:
        Clues = [] 
 
        #iterating through the given guess to find conditions for Clues 
        for i in range(len(guess)):
            if guess[i] == check[i]: 
                # A correct digit is in the correct place. 
                Clues.append('Fermi') 
            elif guess[i] in check: 
                # A correct digit is in the incorrect place. 
                Clues.append('Pico')
                
        #if there are no conditions for any Clues in the given guess 
        if len(Clues) == 0:
           #There are no correct digits at all.
            return 'Bagels' 
        else:
         
            #Sorts the Clues in order not to give away the positions of numbers in the SecretNum
            Clues.sort() 
    #Joins the separate string Clues to make one single string Clue. 
    return "".join(Clues)                 

 
while KEY:                   # Main game loop. 
    print('I have thought up a number.') 
    print(f'You have {MAX_GUESSES} guesses left')

    numGuesses = 1   #counter for number of attempts
    while numGuesses <= MAX_GUESSES:   
        guess = ""
        # Keep looping until they enter a valid guess or run out of trials 
        while len(guess) != NUM_DIGITS:
            print(f'Guess #{numGuesses} ')
            guess = input('> ')
            #To validate the given guess 
            try: 
                int(guess)
                assert len(guess) == NUM_DIGITS
            except AssertionError:
                print(f"《》》》Guesses must be a {NUM_DIGITS} digit 《《《》")
                continue
            except (TypeError,ValueError):
                print("》No Alphabets,Spaces,Decimals or Special Characters: Numbers only !")
                continue
               
            store_Clues= getClues(guess)   #Gets Clues
            numGuesses += 1
            print(store_Clues)
            
            #if total number of trials has been reached
            if numGuesses > MAX_GUESSES: 
                print('\nYou ran out of guesses.') 
                print(f'The answer was {check}.'+'\n'*5)
                
            #If given guess equals to the SecretNum 
            if store_Clues == 'FermiFermiFermi':
                print(VALIDATION)
                print(f"The answer is {check}")
                print(f"\nNumber of trials: {numGuesses-1}"+"\n"*5)
                KEY = False  #Breaks line 83 While-Loop
                numGuesses = MAX_GUESSES + 1  #Breaks line 88 While-Loop
                break  #Breaks line 91 While-Loop
            
            print('*'*SEPARATION + '\nDo you want to play again?(yes/no)')
            #If yes, Continue Playing
            if input('>').lower().startswith('y'):
                print('*'*SEPARATION)
                print("Go again!")
                continue  # Skips the remaining lines of code and restarts from line 91 While- loop
           #Anything other than yes, End the game.
            else:
                print("Thanks for playing" + "\n"*10)
                KEY = False  #Breaks line 83 While-Loop
                numGuesses = MAX_GUESSES + 1  #Breaks line 88 While-loop
                break #Breaks line 91 While-Loop
                         
            
        
        
  
    


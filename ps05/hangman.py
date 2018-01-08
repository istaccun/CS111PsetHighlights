# Teresa and Isabel
# Pset 5
# 2/28/16

"""
The Taylor-Swift-song-titles Hangman game. Randomly display a song title and 
guess the title with no more than 6 wrong letter guesses. Play for as long as 
you want.
"""

import random

# A list of Taylor Swift song titles
songs = [
"All You Had to Do Was Stay",
"Better than Revenge",
"Everything Has Changed",
"I Knew You Were Trouble",
"Two is Better Than One",
"Welcome to New York",
"You Belong with Me",
"We Are Never Ever Getting Back Together",
"The Way I Loved You",
"Two is Better Than One",
"Teardrops on My Guitar"
]

# uncomment this if you want to test with a simple word over and over again
#songs = ["wellesley"]


# A list of graphics to represent a state of the game. One can use indices from
# 0 to 6 to print them out, for example: print hangmanGraphics[2] 
    
hangmanGraphics = [
"""
_______      
|      |      
|             
|             
|             
|             """,

"""
________      
|      |      
|      0      
|             
|             
|             """,
""" 
________      
|      |      
|      0      
|     /       
|             
|             """,
"""
________      
|      |      
|      0      
|     /|      
|             
|             """,
"""
________      
|      |      
|      0      
|     /|\     
|             
|             """,
"""
________      
|      |      
|      0      
|     /|\     
|     /       
|             """,
"""
________      
|      |      
|      0      
|     /|\     
|     / \     
|             
   GAME OVER!"""
]

def getUniqueLetters(phrase):
    """Accumulator function: turns a string into a list of unique characters."""
    list1 = []
    for char in phrase.lower():
        
        if char != " " and char not in list1:
            list1.append(char)
    return list1


def displayDisguise(phrase, foundLetters):
    """Accumulator function: disguises a phrase, showing letters as underscores.
       Returns a string value.
    """
    string1 = ""
    
    for char in phrase.lower():
    
        if char in foundLetters:
            string1 += char
        elif char == " ":
            string1 += " "
        
        elif char not in foundLetters:
            string1 += "_"
         
    return string1
                    
                                                                                                                   
def playHangman():
    """The core function where the game happens. It does the following:
        1) Randomly chooses a word/phrase from the list of songs.
        2) Initializes the state variables.
        3) Displays the initial game state.
        4) Uses a loop to get user guesses and update the game state.
        5) Displays appropriate messages according the game state.
        6) Completes execution with a win or a loss.
    """
    song = (random.choice(songs))
    number_guesses = 0
    hangmanGraphic = 0
    guessed_letters = []
    #foundLetters = ""
         
    print hangmanGraphics[0]
    
    print displayDisguise(song, "")
    
    while number_guesses < 6:
        
        guess = raw_input('Enter your guess: ')
        number_guesses += 1     
        
        if guess in guessed_letters:
            print ('You already tried this letter!')
           
        if guess in song:
            #for guess in song:
            guessed_letters += guess
            print displayDisguise(song, guessed_letters)
            print ("Guesses so far: " + str(guessed_letters))
            
        elif guess not in song:
            hangmanGraphic += 1
            
            if hangmanGraphic > 0:
                if hangmanGraphic == 1:
                    print hangmanGraphics[1]
                    print ("Guesses so far: " + str(guessed_letters))
                elif hangmanGraphic == 2:
                    print hangmanGraphics[2]
                    print ("Guesses so far: " + str(guessed_letters))
                elif hangmanGraphic == 3:
                    print hangmanGraphics[3]
                    print ("Guesses so far: " + str(guessed_letters))
                elif hangmanGraphic == 4:
                    print hangmanGraphics[4]
                    print ("Guesses so far: " + str(guessed_letters))
                elif hangmanGraphic == 5:
                    print hangmanGraphics[5]
                    print ("Guesses so far: " + str(guessed_letters))
                elif hangmanGraphic == 6:
                    print hangmanGraphics[6]
                    print ("Guesses so far: " + str(guessed_letters))
            #while number_guesses <= len(hangmanGraphics):
            #    hangmans = hangmans + number_guesses
                #print displayDisguise(song, guess)        
                    
            
        #if guess not in song:
        #    print hangmanGraphics[1]
        #if guess in song:
        #    print hangmanGraphics[0]
        #    print displayDisguise(song, guess) 

    if number_guesses == 6:
        print("GAME OVER! YOU LOSE.")
    
def startGame():
    """The function that starts everything. It waits for input from user. The 
    letter q always ends the program. Any other letter will start a new game,
    over and over again.
    """
    print ("Welcome to Taylor Swift's hangman game!")
    print ("Type p for play and q for quit.") 
     
    start = raw_input ('enter choice -> ')
    if start == 'q':
        print ('Thanks for playing, goodbye')
    elif start == 'p':
        print ('NEW GAME STARTS NOW!') 

		
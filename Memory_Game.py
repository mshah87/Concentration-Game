import random
        
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    # YOUR CODE GOES HERE

    from random import shuffle
    shuffle(deck)
    print("Shuffling the deck...")

    print("")
       
def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()

def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    # YOUR CODE GOES HERE
    #for i in range (len(original_board)):
    
    discovered[p1-1]= original_board[p1-1]
    
    discovered[p2-1] = original_board[p2-1]

    print_board(discovered)


   
#############################################################################
#   FUNCTIONS FOR OPTION 1 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board=[]

    # YOUR CODE GOES HERE

    playable_board = l.copy()
    
    for i in playable_board:
        if i == '*':
            
            playable_board.remove(i)
            
    for i in playable_board:
        
        if playable_board.count(i) == 1:
            
            playable_board.remove(i)
            
    for i in ((playable_board)):
        
        if ((playable_board.count(i)) %2) != 0:
            
            playable_board.remove(i)

    for i in ((playable_board)):
        
        if ((playable_board.count(i)) %2) != 0:

            playable_board.remove(i)
    

    return playable_board
    

    '''
    for i in playable_board:
        if i == '*':
            
            playable_board.remove(i)
            
        if playable_board.count(i) == 1:
            
            playable_board.remove(i)

        if ((playable_board.count(i)) %2) != 0:
            
            playable_board.remove(i)

        if ((playable_board.count(i)) %2) != 0:

            playable_board.remove(i)

    return playable_board
    '''

def is_rigorous(l):
    '''list of str->True or None
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''

    # YOUR CODE GOES HERE

    for x in range(len(l)):
        if l.count(l[x])!=2:
            return False
    return True
    

####################################################################3

def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''

    print("Ready to play ...\n")

    # this is the funciton that plays the game
    # YOUR CODE GOES HERE

    '''
    guess=0
    corguess =0
    
    while True:
        attempt +=1
        print("")   
        print("Enter two distinct locations on the board that you want revealed.")
        print("i.e. two integers in the range", [1, size])
        num1 = int(input("Enter position 1: "))
        num2 =int(input("Enter position 2: "))
        while num1==num2:
            print("")   
            print("Enter two distinct locations on the board that you want revealed.")
            print("i.e. two integers in the range", [1, size])
            num1 = int(input("Enter position 1: "))
            num2 =int(input("Enter position 2: "))
    '''

    discovered= len(board)*['*']
    print()
    print()
    print()
    
    ans= False
    guess = 0
    corguess = 0
    
    while ans == False :

        print("\n")
        
        print("Enter two distinct positions on the board that you want revealed.\ni.e two integers in the range [1," +str(len(board))+"]")
        p1= int(input("Enter position 1: "))
        p2= int(input("Enter position 2: "))
        if p1 == p2 :
            print("The position is the same")
            print("Please try agan.")
        elif (discovered[p1-1]!= "*") or(discovered[p2-1]!="*"):
            print("One or both of the chosen portions has already been paired")
            print("Please try agan. This guess did not count Your current number of guesses is " + str(guess))

        else:
            print_revealed(discovered,p1,p2,board)
            guess = guess+1 
            if discovered[p1-1]==discovered[p2-1]:
                corguess= corguess+1
                wait_for_player()
                
                print(85*"\n")
                print_board(discovered)
                
            elif discovered[p1-1] != discovered[p2-1]:
                discovered[p1-1] = "*"
                discovered[p2-1] = "*"
                wait_for_player()
                print(85*"\n")
                print_board(discovered)
        if corguess == (len(board) // 2):
            ans = True
            print(1000*"\n")
            print("Congratulations Amli you completed the game with "+str(guess)+ " guesses. Thats " + str(guess - (len(board) // 2)) + " more than the best possible. \n")



def draw_star(size):

    '''(size of board)->string
    This function prints the stars of the board according to the given size. 
    '''

    board=""
    for i in range(0,size):
        board+='*'
    return board


#main

n1= ("Welcome to my Concentration game")
print ("****" + len(n1)*"*"+ "****")
print ("*  " + len(n1)*" "+ "    *")
print ("*  _"+(n1)+ "_  *")
print ("*  " + len(n1)*" "+ "    *")
print ("****" + len(n1)*"*"+ "****")
print()
    
# YOUR CODE TO GET A CHOICE 1 or CHOCE 2 from a player GOES HERE

print("Would you like(enter 1 or 2 to indicate your choice: ")
pick= int(input("(1) me to generate a rigorous deck of cards for you \n(2) or, would you like me to read a deck from a file? \n "))


'''
while((pick is not 1) or (pick is not 2)):
    pick=int(input(str(pick) + " is not an existing option. Please try again. Enter 1 or 2 to indicate your option: "))
'''   
    

'''
while ((pick != '1') or (pick!= '2')):
    pick= input(pick + " is not an existing option. Please try again. Enter 1 or 2 to indicate your choice: ")
'''

# YOUR CODE FOR OPTION 1 GOES HERE
# In option 1 somewhere you need to and MUST have a call like this:
# board=create_board(size)

if(pick==1):
    print("You chose to have a rigorous deck generated for you" )
    print()

    print("How many cards do you want to play with?")
    size = int(input("Enter an even number between 2 and 52: "))
    while size % 2 != 0:
        print("How many cards do you want to play with?")
        size = int(input("Enter an even number between 2 and 52: "))        
       

    board = create_board(size)
    shuffle_deck(board)
    wait_for_player()

    
    #creates the board of the given size
    star_board = draw_star(size)
    print(" ")
    print_board(star_board)
    print(" ")
    play_game(board) 
        

   

# YOUR CODE FOR OPTION 2 GOES HERE
# In option 2 somewhere you need to and MUST have the following 4 lines of code one after another

elif(pick==2):
    print("You chose to load a deck of cards from a file")
    file=input("Enter the name of the file: ")
    file=file.strip()
    board=read_raw_board(file)
    board=clean_up_board(board)

    if is_rigorous(board)!=False:
        n2= ("This deck is now playable and rigorous and it has " + str(len(board)) + " cards")
        print ("****" + len(n2)*"*"+ "****")
        print ("*  " + len(n2)*" "+ "    *")
        print ("*  _"+(n2)+ "_  *")
        print ("*  " + len(n2)*" "+ "    *")
        print ("****" + len(n2)*"*"+ "****")
        print()

        wait_for_player()

        shuffle_deck(board)
        wait_for_player()


        
    else:
        n2= ("This deck is now playable but not rigorous and it has " + str(len(board)) + " cards")
        print ("****" + len(n2)*"*"+ "****")
        print ("*  " + len(n2)*" "+ "    *")
        print ("*  _"+(n2)+ "_  *")
        print ("*  " + len(n2)*" "+ "    *")
        print ("****" + len(n2)*"*"+ "****")
        print()

        wait_for_player()
        shuffle_deck(board)
        wait_for_player()


    size= int(len(board))
    
    makeb = create_board(size)
    star_board = draw_star(size)
    print(" ")
    print_board(star_board)
    print(" ")

    if(board==[]):
        print("The resulting board is empty. \nPlaying Concentration game with an empty board is impossibe. \nGood bye ")
    else:
        play_game(board) 




# coding: utf-8

# In[1]:


from IPython.display import clear_output
def display_board(board):
    
    clear_output() #Clears the board displayed on screen
    print('   |   |   ')
    print(' ' + board[7] + ' | '+ board[8] + ' | ' + board[9])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | '+ board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[1] + ' | '+ board[2] + ' | ' + board[3])
    print('   |   |   ')


# In[6]:


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O': #while loop for first player to choice marker
        marker = input('Player 1 X or O?: ').upper()
    if marker == 'X':
        return ('X', 'O') #Tuple List
    else:
        return ('O', 'X') #Tuple List


# In[3]:


def place_marker(board, marker, position):
    board[position] = marker


# In[4]:


def win_check(board, mark):
    return ((board[7] == mark and board [8] == mark and board[9] == mark) or #Row Top Win
            (board[4] == mark and board [5] == mark and board[6] == mark) or #Row Middle Win
            (board[1] == mark and board [2] == mark and board[3] == mark) or #Row Bottom win
            (board[7] == mark and board [4] == mark and board[1] == mark) or #Column Left Win
            (board[8] == mark and board [5] == mark and board[2] == mark) or #Column Middle Win
            (board[9] == mark and board [6] == mark and board[3] == mark) or #Column Right Win
            (board[7] == mark and board [5] == mark and board[3] == mark) or #Diagonal Win
            (board[1] == mark and board [5] == mark and board[9] == mark)) #Diagonal win


# In[5]:


import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# In[6]:


def space_check(board, position):
    return board[position] == ' '


# In[7]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
        else:
            return True   


# In[8]:


def player_choice(board):
    
    position = ' '
    
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Choose your next position: (1-9)')
    return int(position)


# In[ ]:


def replay():
    return (input('Do you want to play again? \(Yes or no\)'.lower().startswith('y')))


# In[ ]:


print('Welcome to Tic-Tac-Toe')

while True:
    theBoard = [' ']*10 #Populate a list representing the board
    player1_marker, player2_marker = player_input() #Tuple un-packing
    turn = choose_first()
    print(turn + ' Will go first')
    
    game_on = True
    
    while game_on:
        
        if turn == 'Player 1':
            display_board(theBoard) #Displays board as is, set as blank to start
            position = player_choice(theBoard) #Sends current status of board, asks positoin input, checks if available number
            place_marker(theBoard, player1_marker, position) #places choice on board
            
            if win_check(theBoard, player1_marker): #Checks for a win, if player 1 markers win, return win!
                display_board(theBoard) #Displays current board
                print('Player 1 win!')
                game_on = False
            
            else:
                
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Draw')
                    break
                else:
                    turn = 'Player 2'
                
        else: 
            display_board(theBoard) #Displays status of current board
            position = player_choice(theBoard) #Select a spot, checks if elligable
            place_marker(theBoard, player2_marker, position)
            
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 win!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('Draw')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break


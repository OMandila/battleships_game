import random

def board():
    """
    Return playground coordinates as a list of lists
    """
    board = [[' ',' ','1',' ','2',' ','3',' ','4',' ','5',' ','6',' ',' '],
             [' ',' ','*',' ','*',' ','*',' ','*',' ','*',' ','*',' ',' '],
             ['1','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
             ['2','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
             ['3','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
             ['4','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
             ['5','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
             ['6','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
             [' ',' ','*',' ','*',' ','*',' ','*',' ','*',' ','*',' ',' ']]
    return board

def create_board(board):
    """
    Display the playground as a board on the terminal
    """
    print()  # Print a newline before the board
    for row in board:  # Iterate over each row in the board
        for cell in row:  # Iterate over each cell in the row
            print(cell, end='')  # Print each cell in the row without a newline, but with a space
        print()  # Print a newline after each row

def select_space(board):
    """
    Ask the user to specify the location of their battleships
    By entering the coordinates of the ships in the terminal
    The function returns the number of battleships
    """
    ships=0
    battleships = int(input("How many battleships do you have: "))
    while True:
        try:
            if ships < battleships:
                # Select positions in an empty space on the board
                print("Identify the coordinates for the location of your battleships:\n")
                col = int(input("Enter column value: "))  # Collects user input for column value
                row = int(input("Enter row value: "))  # Collects user input for row value

                if (row <= 0 or row > 6) or (col <=0 or col > 6): # Check if row and col values are within the board range
                    print("Either row or column is out of range. You have to try again!")
                    continue

                if board[row+1][col*2] == ' ':
                    # Place ⊙ in the right spot in the board
                    board[row+1][col*2] = '⊙'
                    create_board(board)
                    ships += 1
                    print()
                    continue
                else:
                    print("The coordinates you provided are for a location that is already occupied.")
                    continue
            else:
                break
        except Exception as e:
            print(e)

    return battleships

def enemy_target(board):
    """
    Determines the coordinates of the location for the missiles to be dropped
    The function returns the number of battleships capsized
    """
    missiles = 0
    capsized = 0
    # Randomly select positions for opponent missiles
    while True:
        if missiles < random.randint(2, 20): # Keeping the total number of missiles deployed random
            row = random.randint(2, 7)  # Adjusted for the board's structure, account for zero indexing
            col = random.choice([2, 4, 6, 8, 10, 12])  # Columns numbers adjusted to account for spaces
            # Choose between Ⓧ and x to place in the board
            if board[row][col] == ' ':
                board[row][col] = 'x'
            elif board[row][col] == '⊙':
                board[row][col] = 'Ⓧ'
                capsized += 1
            else:
                board[row][col] = 'x'
            missiles += 1
            continue
        print("================================================================================\n")
        print("GAME ANALYSIS\n")
        print(f"Your opponent launched {missiles} missiles and capsized {capsized} battleship(s) here 'Ⓧ '. The other locations that were hit by the missiles are 'x'.\n")
        create_board(board)
        break

    return capsized

def calculate_scores(battleships, capsized):
    """
    Determines the scores for the players
    """
    if (battleships-capsized) > capsized:
        print ("\nYOU WIN!\n")
    else:
        print ("\nYOU LOSE!\n")

    print(f"Out of {battleships} battleships, {capsized} capsized by your opponent missiles.\n")
    print("================================================================================\n")

def main():
    """
    Runs all program functions.
    """
    while True:
        playground = board()
        create_board(playground)
        Battleships = select_space(playground)
        Capsized = enemy_target(playground)
        calculate_scores(Battleships, Capsized)
        end = input("\nDo you want to play again? Y/N: ").lower()
        if end == 'n':
            break

print()
print("-----------------------THE MINI BATTLESHIPS GAME-----------------------")
print("This is a strategy type guessing game for one player against the computer.")
print("You win by having more battleships than the ones destroyed by your opponent.")
main()

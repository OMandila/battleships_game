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
                print("\nIdentify the coordinates for the location of your battleships:\n")
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

def main():
    """
    Runs all program functions.
    """
    playground = board()
    create_board(playground)
    x = select_space(playground)

print()
print("-----------------------THE MINI BATTLESHIPS GAME-----------------------")
print("This is a strategy type guessing game for one player against the computer.")
main()

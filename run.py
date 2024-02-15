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

def main():
    """
    Runs all program functions.
    """
    playground = board()
    create_board(playground)

print()
print("-----------------------THE MINI BATTLESHIPS GAME-----------------------")
print("This is a strategy type guessing game for one player against the computer.")
main()

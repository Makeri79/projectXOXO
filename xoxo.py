import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    random.shuffle(players)
    current_player = players[0]

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        if current_player == 'X':
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
        else:
            row, col = computer_move(board)

        if board[row][col] == ' ':
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                return current_player
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                return 'Draw'
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Cell already taken. Try again.")

def computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells)

def main():
    wins = 0
    draws = 0
    losses = 0

    while True:
        result = play_game()

        if result == 'X':
            wins += 1
        elif result == 'O':
            losses += 1
        elif result == 'Draw':
            draws += 1

        print(f"Stats: Wins - {wins}, Draws - {draws}, Losses - {losses}")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()

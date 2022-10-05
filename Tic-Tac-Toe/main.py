board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
win_series = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def clear_board():
    board[0] = board[1] = board[2] = board[3] = board[4] = board[5] = board[6] = board[7] = board[8] = " "


def display_board():
    print(f"""
    {board[0]} | {board[1]} | {board[2]}   |   1 | 2 | 3 
   -----------  |  -----------            
    {board[3]} | {board[4]} | {board[5]}   |   4 | 5 | 6 
   -----------  |  -----------            
    {board[6]} | {board[7]} | {board[8]}   |   7 | 8 | 9
    """)


def ask_user_input(user_info):
    user_input = int(input(f"Player-{user_info[0]}'s turn. Choose a number to place your tic.\t"))
    place_tic(user_input - 1, user_info)


def place_tic(user_move, user_info):
    if board[user_move] == " ":
        board[user_move] = user_info[1]
        display_board()
    else:
        print("Enter a valid move you idiot!")
        ask_user_input(user_info)


def is_win():
    for i in win_series:
        if board[i[0]] == board[i[1]] == board[i[2]] and board[i[0]] != " ":
            return True


def play_again():
    again = input("Enter 'Y' to play again and 'N' to exit.\t").upper()
    if again == "Y":
        clear_board()
        start_game()
    else:
        return False


def start_game():
    win = False
    users = [[1, "X", 0], [2, "O", 0]]

    display_board()

    while not win:
        for user in users:
            ask_user_input(user)
            if is_win():
                user[2] += 1
                print(f"'{user[1]}' wins!\nScores: 'X'-{users[0][2]}  'O'-{users[1][2]}")
                if not play_again():
                    break


start_game()

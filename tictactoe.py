class TicTacToe:

    WIN_COMBINATIONS = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [6,4,2]
]

    board = [" "] * 9


    # def __init__(self):
    #     self.board = [" "] * 9
    

    def display_board(board):
        # board = self.board
        print(board[0] + '|' + board[1] + '|' + board[2])
        print("-+-+-")
        print(board[3] + '|' + board[4] + '|' + board[5])
        print("-+-+-")
        print(board[6] + '|' + board[7] + '|' + board[8])

    display_board(board) 

    def turn(board, WIN_COMBINATIONS):
        # board = self.board
    # for i in range(10):
    #     display_board(board) 
        player1 = "X"
        player2 = "O"
        turn = 1
        count = 0
        for i in range(10):
            user_input = input("please enter a number between 1 - 9: ")
            user_input = int(user_input) - 1

            print(board)

            if board[user_input] == " " and turn == 1:
                board[user_input] = player1
                turn = 2
                print(board)
                count += 1
                # display_board(board)
            elif board[user_input] == " " and turn == 2:
                board[user_input] = player2
                turn = 1
                print(board)
                count += 1
            else:
                print("place already filled, choose another number")
                continue
            # find_winner(board, WIN_COMBINATIONS)

            if count == 9:
                print("Draw, No winner")




    turn(board, WIN_COMBINATIONS)

    def find_winner(board, WIN_COMBINATIONS):
    # """Return the winner"""
        # board = self.board
        for combo in WIN_COMBINATIONS:
            group = list(map(lambda i: board[i], combo))
            for player in ['X', 'O']:
                if all(x == player for x in group):
                    return player
    
    find_winner(board, WIN_COMBINATIONS)

    # TicTacToe.new.turn()

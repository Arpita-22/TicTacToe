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

    # board = [" "] * 9

    board = {
        '1': " ", '2': " ", '3': " ",
        '4': " ", '5': " ", '6': " ",
        '7': " ", '8': " ", '9': " "
    }


    # def __init__(self):
    #     self.board = [" "] * 9
    

    def display_board(board):
        # board = self.board
        print(board['1'] + '|' + board['2'] + '|' + board['3'])
        print("-+-+-")
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print("-+-+-")
        print(board['7'] + '|' + board['8'] + '|' + board['9'])

    display_board(board) 

    def display_board1():
        print("hhhhhhahahahah")


    def turn(self, board):#WIN_COMBINATIONS):
        # board = self.board
        self.display_board1() 
        player1 = "X"
        player2 = "O"
        turn = 1
        count = 0
        for i in range(10):
            #display_board() 
            user_input = input("please enter a number between 1 - 9: ")
            user_input = int(user_input)

            print(board)

            if board[f'{user_input}'] == " " and turn == 1:
                board[f'{user_input}'] = player1
                turn = 2
                print(board)
                count += 1
                #display_board(board)
            elif board[f'{user_input}'] == " " and turn == 2:
                board[f'{user_input}'] = player2
                turn = 1
                print(board)
                count += 1
            else:
                print("place already filled, choose another number")
                continue
            # find_winner(board, WIN_COMBINATIONS)
            

            #if board['1'] == board['2'] and board['2'] == board['3'] and 
            if count == 9:
                print("Draw, No winner")
                return
            





    turn(board)

    def find_winner(board, WIN_COMBINATIONS):
    # """Return the winner"""
        # board = self.board
        for combo in WIN_COMBINATIONS:
            group = list(map(lambda i: board[i], combo))
            for player in ['X', 'O']:
                if all(x == player for x in group):
                    return player

    
    def won():
        turn(board)
        #if()

    
    # find_winner(board, WIN_COMBINATIONS)

    # TicTacToe.new.turn()

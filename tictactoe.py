import random
import math

# There are 2 modes to the game - 
#   Between 2 players
#   Between 1 player and computer
# It is assumed that the first player will always use a 'X' and next player will have 'O'
# When played between player and computer, it is assumed the player plays first.
class TicTacToe:

    # define a 9x9 board
    def __init__(self):
        self.board = {
            1: " ", 2: " ", 3: " ",
            4: " ", 5: " ", 6: " ",
            7: " ", 8: " ", 9: " "
        }
        self.space = "           "
        self.OKGREEN = "\033[92m"
        self.WARNING = "\033[91m"
        self.BLUE = "\033[94m"
        self.YELLOW = "\033[33m"
        self.ENDC = "\033[0m"
        self.player1 = self.BLUE + "X" + self.ENDC
        self.player2 = self.YELLOW + "O" + self.ENDC
        

    # function to display the current state of the board
    def display_board(self):
        board = self.board
        print(self.space + board[1] + ' | ' + board[2] + '| ' + board[3])
        print(self.space + "--+--+--")
        print(self.space + board[4] + ' | ' + board[5] + '| ' + board[6])
        print(self.space + "--+--+--")
        print(self.space + board[7] + ' | ' + board[8] + '| ' + board[9])
        print("===============================")

    # this function handles the game's turns
    def turn(self):
        board = self.board
        turn = 1
        count = 0
        
        input_play_with_computer = input("would you want to play with the computer (y/n) ")
        play_with_computer = (input_play_with_computer == "y")
         
        while count < 10:
            self.display_board() 
            
            move = False
            user_input = ''
            if not play_with_computer or turn == 1:
                user_input = input("please enter a number between 1 - 9: ")
            else:
                user_input = self.best_position()
                
            # input should strictly be a number between 0-9
            if not user_input.isnumeric() \
                or (user_input.isnumeric() and int(user_input) < 1 or int(user_input) > 9) :
                print(self.WARNING + "please choose a valid number" + self.ENDC)
                continue
            
            user_input = int(user_input)

            # swapping player's turn   
            if board[user_input] == " " and turn == 1:
                board[user_input] = self.player1
                turn = 2
            elif board[user_input] == " " and turn == 2:
                board[user_input] = self.player2
                turn = 1
            else:
                print(self.WARNING + "place already filled, choose another number" + self.ENDC)
                continue
            
            if count > 3:
                if self.did_win():
                    self.display_board() 
                    print(self.OKGREEN + "Player " + str((1, 2) [turn == 1]) + " wins!" + self.ENDC)
                    return

            count += 1
            
            # all 9 positions are filled up
            if count == 9:
                self.display_board() 
                print("Draw, No winner")
                return
            
    # check if there is a winner
    def did_win(self):
        for i in range(1, 4):
            if self.board[i] != " " and self.find_win_vertical(i, self.board[i]):
                return True
            if self.board[(i - 1) * 3 + 1] != " " and self.find_win_horizontal((i - 1) * 3 + 1, self.board[(i - 1) * 3 + 1]):
                return True
        
        if self.find_win_diagonal():
            return True

    # check horizontally in the game board, if all 3 pos have same symbol
    def find_win_horizontal(self, start_pos, symbol):
        row = (start_pos - 1) / 3
        column = (start_pos - 1) % 3
            
        for c in range(1, 4):
            new_position = row * 3 + c
            if self.board[new_position] != symbol:
                break
            elif self.board[new_position] == symbol and c == 3:
                return True
    
        return False

    # check vertically in the game board, if all 3 pos have same symbol
    def find_win_vertical(self, start_pos, symbol):
        row = (start_pos - 1) / 3
        column = (start_pos - 1) % 3
        
        for r in range(3):
            new_position = r * 3 + column + 1
            if self.board[new_position] != symbol:
                break
            elif self.board[new_position] == symbol and r == 2:
                return True
        
        return False

    # check diagonally in the game board, if all 3 pos have same symbol
    def find_win_diagonal(self):
        row, column = 0, 0
        
        left_corner_symbol = self.board[1]
        if left_corner_symbol != " " :
            for i in range(1, 4):
                new_position = (i - 1) * 3 + i
                if self.board[new_position] != left_corner_symbol:
                    break
                elif self.board[new_position] == left_corner_symbol and i == 3:
                    return True
        
        right_corner_symbol = self.board[3]
        if right_corner_symbol != " " :
            for i in range(1, 4):
                new_position = i * 2 + 1
                if self.board[new_position] != right_corner_symbol:
                    break
                elif self.board[new_position] == right_corner_symbol and i == 3:
                    return True
        return False


    # Mini-Max algorithm
    # This function is called to calculate computer's next move
    def minimax(self, symbol):
        if self.did_win(): 
            if symbol == self.player1: #computer wins, because this is called for player 'X'      
                return 1
            else: 
                return -1

        min_score = math.inf
        max_score = -math.inf

        for position in self.board:
            if self.board[position] == " ":
                self.board[position] = symbol
                if symbol == self.player2:
                    max_score = max(max_score, self.minimax(self.player1))
                else:
                    min_score = min(min_score, self.minimax(self.player2))
                self.board[position] = " "
        
        # its going to be draw
        if max_score == -math.inf and min_score == math.inf:
            return 0
        # this is not a winning combination
        if max_score == -math.inf:
            return min_score
        # this is a winning combination
        if min_score == math.inf:
            return max_score
            
        return max(min_score, max_score)
    
    # Check all the open positions and see what is the best move
    def best_position(self):
        draw = -1
        for position in self.board:
            if self.board[position] == " ":
                self.board[position] = self.player2
                score = self.minimax(self.player1)
                self.board[position] = " "
                if score == 1:
                    return str(position)
                if score == 0:
                    draw = str(position)
        if draw != -1:
            return draw
        return str(random.randint(1, 9))
            

    def main(self):
        self.turn()

if __name__ == "__main__":
    objName = TicTacToe()
    objName.main() 
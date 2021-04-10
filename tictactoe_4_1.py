import random
import math

class TicTacToe:

    def __init__(self):
        self.board = {
            1: " ", 2: " ", 3: " ",
            4: " ", 5: " ", 6: " ",
            7: " ", 8: " ", 9: " "
        }
        self.space = "           "

    def display_board(self):
        board = self.board
        print(self.space + board[1] + ' | ' + board[2] + '| ' + board[3])
        print(self.space + "--+--+--")
        print(self.space + board[4] + ' | ' + board[5] + '| ' + board[6])
        print(self.space + "--+--+--")
        print(self.space + board[7] + ' | ' + board[8] + '| ' + board[9])
        print("===============================")

    def turn(self):
        board = self.board
        player1 = "X"
        player2 = "O"
        turn = 1
        count = 0
        
        input_play_with_computer = input("would you want to play with the computer (y/n) ")
        play_with_computer = (input_play_with_computer == "y")
        # first_player = "2"
        # if play_with_computer:
        #     first_player = input("who goes first? Press 1 for computer, 2 for you... ")
        
        # if first_player == "1":
        #     turn = 2
         
        while count < 10:
            self.display_board() 
            
            move = False
            user_input = ''
            if not play_with_computer or turn == 1:
                user_input = input("please enter a number between 1 - 9: ")
            else:
                user_input = self.best_position()
                
            if not user_input.isnumeric() \
                or (user_input.isnumeric() and int(user_input) < 1 or int(user_input) > 9) :
                print("please choose a valid number")
                continue
            
            user_input = int(user_input)
                
            if board[user_input] == " " and turn == 1:
                board[user_input] = player1
                turn = 2
            elif board[user_input] == " " and turn == 2:
                board[user_input] = player2
                turn = 1
            else:
                print("place already filled, choose another number")
                continue
            
            if count > 3:
                if self.did_win():
                    self.display_board() 
                    print("Player " + str((1, 2) [turn == 1]) + " wins!")
                    return

            count += 1
            if count == 9:
                self.display_board() 
                print("Draw, No winner")
                return
            
    def did_win(self):
        for i in range(1, 4):
            if self.board[i] != " " and self.find_win_vertical(i, self.board[i]):
                return True
            if self.board[(i - 1) * 3 + 1] != " " and self.find_win_horizontal((i - 1) * 3 + 1, self.board[(i - 1) * 3 + 1]):
                return True
        
        if self.find_win_diagonal():
            return True

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




    def minimax(self, symbol):
        if self.did_win(): 
            if symbol == "X": #computer wins, because this is called for player 'X'      
                return 1
            else: 
                return -1

        min_score = math.inf
        max_score = -math.inf

        for position in self.board:
            if self.board[position] == " ":
                self.board[position] = symbol
                if symbol == "O":
                    max_score = max(max_score, self.minimax("X"))
                else:
                    min_score = min(min_score, self.minimax("O"))
                self.board[position] = " "
        
        if max_score == -math.inf:
            return min_score
        if min_score == math.inf:
            return max_score
            
        return max(min_score, max_score)
    
    def best_position(self):
        for position in self.board:
            if self.board[position] == " ":
                self.board[position] = "O"
                score = self.minimax("X")
                self.board[position] = " "
                if score == 1:
                    return str(position)
        return str(random.randint(1, 9))
            

    def main(self):
        self.turn()

if __name__ == "__main__":
    objName = TicTacToe()
    objName.main() 
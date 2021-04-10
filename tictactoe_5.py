import random

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
        
        input_play_with_computer = input("would you want to play with the computer (y/n)")
        play_with_computer = (input_play_with_computer == "y")
         
        while count < 10:
            self.display_board()     
            move = False
            user_input = 0
            if not play_with_computer or turn == 1:
                user_input = input("please enter a number between 1 - 9: ")
                user_input = int(user_input)
            else:
                user_input = random.randint(1, 9)
                # self.minimax(user_input, move, player1, score = 0)
                

            if user_input < 1 or user_input > 9:
                print("please choose a valid number")
                continue
                
            if board[user_input] == " " and turn == 1:
                board[user_input] = player1
                turn = 2
            elif board[user_input] == " " and turn == 2:
                board[user_input] = player2
                turn = 1
            else:
                print("place already filled, choose another number")
                continue
            
            while count > 3:
                self.display_board() 

            count += 1
            if count == 9:
                self.display_board() 
                print("Draw, No winner")
                return

        def win(self, count):

                if board[1] == board[2] == board[3] == player1 and board[1] == board[2] == board[3] != " ":
                    print(" player1 Wins!")
                    return True
                else:
                    print("player2 Wins !")
                    return True


                if board[4] == board[5] == board[6] == player1 and board[4] == board[5] == board[6] != " ":
                    print(" player1 Wins!")
                    return True
                else:
                    print("player2 Wins !")
                    return True

                if board[7] == board[8] == board[9] == player1 and board[7] == board[8] == board[9] != " ":
                    print(" player1 Wins!")
                    return True
                else:
                    print("player2 Wins !")
                    return True

                if board[1] == board[2] == board[3] == player1 and board[1] == board[2] == board[3] != " ":
                    print(" player1 Wins!")
                    return True
                else:
                    print("player2 Wins !")
                    return True

                if board[2] == board[5] == board[8] == player1 and board[2] == board[5] == board[8] != " ":
                    print(" player1 Wins!")
                    return True
                else:
                    print("player2 Wins !")
                    return True

                if board[3] == board[6] == board[9] == player1 and board[3] == board[6] == board[9] != " ":
                    print(" player1 Wins!")
                    return True
                else:
                    print("player2 Wins !")
                    return True

                if board[1] == board[5] == board[9] == player1 and board[1] == board[5] == board[9] != " ":
                    print(" player1 Wins!")
                    return True
                else:
                    print("player2 Wins !")
                    return True

                if board[3] == board[5] == board[7] == player1 and board[3] == board[5] == board[7] != " ":
                    print(" player1 Wins!")
                    return True
                else:
                    print("player2 Wins !")
                    return True
                    
                return False


            
    # def did_win(self):
    #     for i in range(1, 4):
    #         if self.board[i] != " " and self.find_win_vertical(i, self.board[i]):
    #             return True
    #         if self.board[(i - 1) * 3 + 1] != " " and self.find_win_horizontal((i - 1) * 3 + 1, self.board[(i - 1) * 3 + 1]):
    #             return True
        
    #     if self.find_win_diagonal():
    #         return True

    # def find_win_horizontal(self, start_pos, symbol):
    #     row = (start_pos - 1) / 3
    #     column = (start_pos - 1) % 3
            
    #     for c in range(1, 4):
    #         new_position = row * 3 + c
    #         if self.board[new_position] != symbol:
    #             break
    #         elif self.board[new_position] == symbol and c == 3:
    #             return True
    
    #     return False

    # def find_win_vertical(self, start_pos, symbol):
    #     row = (start_pos - 1) / 3
    #     column = (start_pos - 1) % 3
        
    #     for r in range(3):
    #         new_position = r * 3 + column + 1
    #         if self.board[new_position] != symbol:
    #             break
    #         elif self.board[new_position] == symbol and r == 2:
    #             return True
        
    #     return False

    # def find_win_diagonal(self):
    #     row, column = 0, 0
        
    #     left_corner_symbol = self.board[1]
    #     if left_corner_symbol != " " :
    #         for i in range(1, 4):
    #             new_position = (i - 1) * 3 + i
    #             if self.board[new_position] != left_corner_symbol:
    #                 break
    #             elif self.board[new_position] == left_corner_symbol and i == 3:
    #                 return True
        
    #     right_corner_symbol = self.board[3]
    #     if right_corner_symbol != " " :
    #         for i in range(1, 4):
    #             new_position = i * 2 + 1
    #             if self.board[new_position] != right_corner_symbol:
    #                 break
    #             elif self.board[new_position] == right_corner_symbol and i == 3:
    #                 return True
    #     return False



    # def minimax(self, user_input, move, symbol,score = 0):

    #     def maximizing(self,user_input, score):
    #         if self.board[user_input] != " ":
    #             move = True
    #         return score

    #     for position in self.board:
    #         if self.board[position] == " ":
    #             # self.minimax(position, move, symbol, score)
        
    #         if self.board[user_input] == "0" and self.did_win() == True:
    #             score = 1
    #             print(score)

    #         elif symbol == "X" and self.did_win() == True:
    #             score = -1
    #             print(score)
        
    #         else:
    #             score = 0


    #     print(score)
    #     return score

    
    #  def minimax(self, user_input, move, symbol):
    #     score = č
    #     # points ={
    #     #     win: +1,
    #     #     lose: -1,
    #     #     tie: 0
    #     # }

    #     for position in self.board:
    #         current_score = 0
    #         max_score = +1
    #         min_score = -1
    #         if(self.board[position] == " "):
    #             self.board[position] = "0"
    #             # max_score = Math.max(current_score, max_score)
    #             # maximizing 
    #             move = True
    #             if self.did_win() != True:
    #                 move = False
    #                 minimax(self, position, move_maximizing_player, symbol,score)
    #             elif symbol == '0' and self.did_win() == True:
    #                     current_score = +1
    #                     max_score = Math.max(current_score, max_score)
    #                     score = max_score)
    #             # return minimax(self, position, move, symbol, score)
    #             return score

    #             self.board[position] = "X"
    #             # minimizing
    #             min_score = Math.min(current_score,min_score)
    #                 if self.did_win() != True:
    #                     minimax(self, position, move = True, symbol)
    #                 if symbol == "X" and self.did_win() == True:
    #                     current_score = -1
    #                     min_score = Math.min(current_score,min_score)
    #                     score = min_score
    #             # return minimax(self, position, move, symbol,score)
    #             return score

    #     return score

    
    
    def main(self):
        self.turn()

if __name__ == "__main__":
    objName = TicTacToe()
    objName.main() 
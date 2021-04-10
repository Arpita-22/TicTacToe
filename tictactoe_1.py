class TicTacToe:

    def __init__(self):
        self.board = {
            '1': " ", '2': " ", '3': " ",
            '4': " ", '5': " ", '6': " ",
            '7': " ", '8': " ", '9': " "
        }
        self.space = "           "

        # self.adjacencyList = {
        #     '1':['2','4','5'],
        #     '2':['1','3','4','5','6'],
        #     '3':['2','5','6'],
        #     '4':['1','2','5'],
        #     '5':['1','2','3','4','6','7','8','9'],
        #     '6':['3','5','8','9'],
        #     '7':['4','5','8'],
        #     '8':['4','5','6','7','9'],
        #     '9':['5','6','8']
        # }

    def display_board(self):
        board = self.board
        print(self.space + board['1'] + ' | ' + board['2'] + '| ' + board['3'])
        print(self.space + "--+--+--")
        print(self.space + board['4'] + ' | ' + board['5'] + '| ' + board['6'])
        print(self.space + "--+--+--")
        print(self.space + board['7'] + ' | ' + board['8'] + '| ' + board['9'])
        print("===============================")

    def turn(self):
        board = self.board
        player1 = "X"
        player2 = "O"
        turn = 1
        count = 0
        
        while count < 10:
            self.display_board() 
            
            user_input = input("please enter a number between 1 - 9: ")
            user_input = int(user_input)
            if user_input < 1 or user_input > 9:
                print("please choose a valid number")
                continue
                
            if board[f'{user_input}'] == " " and turn == 1:
                board[f'{user_input}'] = player1
                turn = 2
            elif board[f'{user_input}'] == " " and turn == 2:
                board[f'{user_input}'] = player2
                turn = 1
            else:
                print("place already filled, choose another number")
                continue
            
            count += 1
            if count == 9:
                self.display_board() 
                print("Draw, No winner")
                return
            


    def bfs(self, start):
        queue = [start]
        visited = {}
        result = []
        visited[start] = True

        while len(queue):
           currentVertex = queue.pop(0)
           result.append(currentVertex)

           for neighbour in self.adjacencyList[currentVertex]:
            #    print(start)
            #    for player in self.board.values():
            #        if player == "X":             
                        if not neighbour in visited:
                            visited[neighbour] = True
                            queue.append(neighbour)

        print(result)
        return result


    def main(self):
        self.turn()
        # self.bfs('1')

if __name__ == "__main__":
    objName = TicTacToe()
    objName.main() 
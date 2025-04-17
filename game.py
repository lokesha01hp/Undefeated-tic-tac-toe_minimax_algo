from player import HumanPlayer,RandomComputerPlayer,SmartComputerPlayer
import time,math

class Tic_Tac_Tae():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]
    
    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        #tells us what number corresponds to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')


    def available_moves(self):
        #return [i for i,spot in enumerate(self.board) if spot == " "]
        moves = []
        for (i,spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self,square,letter):
        #if valid move,then make the move (assign square to letter) and then return true, if valid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self,square,letter):
        #first checking the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([s == letter for s in row]):
            return True
        #checking the column

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        
        #checking diagonals that is even no (0,2,4,6,8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False



def play(game,x_player,o_player, print_game=True):
    if print_game:
        print(' ')
        game.print_board_nums()

    letter = 'X'
    #iterate while the game still has empty squares don't have to worry about winner
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square,letter):
            if print_game:
                print(letter + f' makes a move to square {square} \n')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(f"🎉 Player {letter} takes the win! Game over.")
                return letter
            #to alter letter
            #letter = 'O' if letter == 'X' else 'X'
            if letter == 'X':
                letter = 'O'
            else:
                letter='X'
        
        if print_game:
            time.sleep(.5)


    if print_game:
        print("It's a tie! Nobody wins, but nobody loses either.")



if __name__ == "__main__":
    print("🎮 Welcome to the Ultimate Tic Tac Toe Showdown! 🧠")
    print("1️⃣  Human vs Human ")
    print("2️⃣  Human vs Smart AI (Warning: Brainpower required)")
    print("3️⃣  Human vs Random Bot (Expect chaos)")
    choice = input("Choose your battleground :")

    if choice == "1":
        x_player = HumanPlayer('X')
        o_player = HumanPlayer('O')
        t = Tic_Tac_Tae()
        result= play(t,x_player,o_player,print_game=True)
    
    elif choice == "2":
        x_player = HumanPlayer('X')
        o_player = SmartComputerPlayer('O')
        t = Tic_Tac_Tae()
        result= play(t,x_player,o_player,print_game=True)
    
    elif choice == "3":
        x_player = HumanPlayer('X')
        o_player = RandomComputerPlayer('O')
        t = Tic_Tac_Tae()
        result= play(t,x_player,o_player,print_game=True)

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
    



# To check the efficency of SmartComputerPlayer
    # x_wins = 0
    # o_wins = 0
    # tie = 0
    # for _ in range(1000):
    #     x_player = SmartComputerPlayer('X')
    #     o_player = RandomComputerPlayer('O')
    #     t = Tic_Tac_Tae()
    #     result= play(t,x_player,o_player,print_game=False)
    #     if result == 'X':
    #         x_wins += 1
    #     elif result == 'O':
    #         o_wins += 1
    #     else:
    #         tie += 1

    # print(f' x wins {x_wins} times and o wins {o_wins} times and the tie happened were {tie} times')

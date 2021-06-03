class OrthokonBoard:


    def __init__(self):
        self._board = [[" " for i in range(4)] for j in range(4)]
        # self._ptrack = [[" " for i in range(4)] for j in range(4)]
        self._current_state = "UNFINISHED"
        # self.fill = 0

    def get_current_state(self):
        return self._current_state

    def check(self,row,col,letter,player):

        if row < 2 and col < 2 :
            region = 1
        elif row < 2 and col >= 2:
            region = 2
        elif row >= 2 and col < 2 :
            region = 3
        elif row >= 2 and col >= 2:
            region = 4
        if region == 1:
            data = [self._board[0][0],self._board[0][1],self._board[1][0],self._board[1][1]]
            if letter in data:
                return False
        elif region == 2:
            data = [self._board[0][2],self._board[0][3],self._board[1][2],self._board[1][3]]
            if letter in data:
                return False
        elif region == 3:
            data = [self._board[2][0],self._board[2][1],self._board[3][0],self._board[3][1]]
            if letter in data:
                return False
        elif region == 1:
            data = [self._board[3][2],self._board[3][3],self._board[2][2],self._board[2][3]]
            if letter in data:
                return False
        for i in range(4):
            if self._ptrack[row][i] != player and self._board[row][i] == letter:
                return False
        for i in range(4):
            if self._ptrack[row][i] != player and self._board[row][i] == letter:
                return False
        return True

    def check_winner(self,row,col):


        if row < 2 and col < 2 :
            region = 1
        elif row < 2 and col >= 2:
            region = 2
        elif row >= 2 and col < 2 :
            region = 3
        elif row >= 2 and col >= 2:
            region = 4

        if region == 1:

            data = [self._board[0][0],self._board[0][1],self._board[1][0],self._board[1][1]]

            if sorted(data) == ['A','B','C','D']:
                return True



        elif region == 2:

            data = [self._board[0][2],self._board[0][3],self._board[1][2],self._board[1][3]]

            if sorted(data) == ['A','B','C','D']:
                return True



        elif region == 3:

            data = [self._board[2][0],self._board[2][1],self._board[3][0],self._board[3][1]]

            if sorted(data) == ['A','B','C','D']:
                return True


        elif region == 1:

            data = [self._board[3][2],self._board[3][3],self._board[2][2],self._board[2][3]]

            if sorted(data) == ['A','B','C','D']:
                return True


        for i in range(4):
            data = [self._board[row][0],self._board[row][1],self._board[row][2],self._board[row][3]]


            if sorted(data) == ['A','B','C','D']:
                return True


        for i in range(4):
            data = [self._board[0][col],self._board[1][col],self._board[2][col],self._board[3][col]]


            if sorted(data) == ['A','B','C','D']:
                return True

        return False

    def print_board(self):
        for i in range(4):
            print(self._board[i])

        print()

    def make_move(self,row,col,letter,player):

        if self.fill != 16 and self._board[row][col] == " " and self._current_state == "UNFINISHED" and self.check(row,col,letter,player):
            self._board[row][col] = letter
            self._ptrack[row][col] = player
            self.fill += 1
            if self.check_winner(row,col) == True:
                if player == 'x':
                    self._current_state = "X_WON"
                elif player == "o":
                    self._current_state = "O_WON"

            self.print_board()

            return True
        else:
            return False

board = OrthokonBoard()
board.make_move(0,0,'B','o')
board.make_move(3,3,'D','o')
print(board.get_current_state())
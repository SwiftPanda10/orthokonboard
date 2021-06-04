# Author: Samuel Bennett
# Date: 6/3/2021
# Description: Orthokon Board game on a 4x4 grid with Yellow and Red Players. (Unfinished)
class OrthokonBoard:

    def __init__(self):
        self._board = self.__build_board()
        self._current_state = "UNFINISHED"

    def __build_board(self):
        # empty 4 by 4 game board
        new_board = [[" " for i in range(0,3)] for j in range(0,3)]
        # add red to row 0
        for col in range(0, 3):
            new_board[0][col] = "R"
        # add yellow to row 3
        for col in range (0, 3):
            new_board[3][col] = "Y"
        return new_board

    def get_current_state(self):
        return self._current_state
    # moves game piece from start to end position
    # updates board if move is valid and returns true
    # return false otherwise
    def make_move(self, startRow, startCol, endRow, endCol):
        # ensure input is within range of game board otherwise return false
        if self.__position_off_board(startRow) or self.__position_off_board(startCol) or self.__position_off_board(endRow) or self.__position_off_board(endCol):
            return False


        # ensure start is different than end
        if startRow == endRow and startCol == endCol:
            return False

        # ensure there is a piece at the starting point otherwise return false
        if self._board[startRow][startCol] != " ":
            return False

        # grab the player piece color from board
        player = self._board[startRow][startCol]

        # update player piece and then board
        self.__update_piece(startRow, startCol, endRow, endCol, player)


    def __position_off_board(self, num):
        # if out of board space
        if num < 0 or num > 3:
            return False
        else:
            return True

    def __update_piece(self, startRow, startCol, endRow, endCol, player):
        # determine if move is diagonal or orthogonal and store type
        isMoveOrthogonal = self._is_move_orthogonal(startRow, startCol, endRow, endCol)

        # update the row one towards the endRow
        row = self._new_position(startRow, endRow)

        # update the col one towards the endCol
        col = self._new_position(startCol, endCol)

        # check if move is valid
        if self._move_is_invalid(row, col, player):
            return False

        # update board so old start position is blank
        self._board[startRow][startCol] = ""

        # move piece
        self._move_piece(self, row, col, endRow, endCol, player, isMoveOrthogonal)

        def _is_move_orthogonal(self, startRow, startCol, endRow, endCol):
            if startRow == endRow or startCol == endCol:
                return True
            else:
                return False

        # create new position from start and end
        def _new_position(self, start, end):
            # start is less than end then add one to start
            if start < end:
                return start + 1
            # else if start is greater than end subtract one from start
            elif start > end:
                return start - 1
            # else start and end are same and return start
            else:
                return start

        # check if move is valid
        def __move_is_invalid(self, row, col, player):
            if self.__position_off_board(row) or self.__position_off_board(col) or self._board[row][col] != player:
                return False
            else:
                return True

        def __move_piece(self, startRow, startCol, endRow, endCol, player, isMoveOrthogonal):
            # determine if move is still diagonal or orthogonal and if does not match return false
            if self.__is_move_orthogonal(startRow, startCol, endRow, endCol) != isMoveOrthogonal:
                return False

            # check if move is invalid
            if self.__move_is_invalid(endRow,endCol,player):
                self.__update_board(startRow, startCol, player)
                return True

            if startRow == endRow and startCol == endCol:
                self.__update_board(startRow, startCol, player)
                return True

            # update the row one towards the endRow
            row = self.__new_position(startRow, endRow)

            # update the col one towards the endCol
            col = self.__new_position(startCol, endCol)

            # update board so old start position is blank
            self._board[startRow][startCol] =" "
            # move piece
            self.__move_piece(self, row, col, endRow, endCol, player, isMoveOrthogonal)

            def __update_board(self, row, col, player):
                # check above convert to R or Y
                if not self.__position_off_board(row + 1):
                    currentPiece = self._board[row + 1][col]
                    if currentPiece !=" ":
                        self._board[row + 1][col] = player

            # check below convert to R or Y
            if not self.__position_off_board(row - 1):
                currentPiece = self._board[row - 1][col]
                if currentPiece !=" ":
                    self._board[row - 1][col] = player

            # check right convert to R or Y
            if not self.__position_off_board(col + 1):
                currentPiece = self._board[row][col + 1]
                if currentPiece !=" ":
                    self._board[row][col + 1] = player

            # check left convert to R or Y
            if not self.__position_off_board(col - 1):
                currentPiece = self._board[row][col - 1]
                if currentPiece !=" ":
                    self._board[row][col] = player

    def _move_is_invalid(self, row, col, player):
        pass

    def _new_position(self, startRow, endRow):
        pass

    def _move_piece(self, self1, row, col, endRow, endCol, player, isMoveOrthogonal):
        pass
# returns RED_WON if all pieces on board are red
# returns YELLOW_WON if all pieces on board are yellow
# returns UNFINISHED if pieces on board are read and yellow
# property to store lastSeenPlayer color
# loop over every row
# loop over every col in row
# if piece is at board row col
# if lastSeenPlayer color is empty
# set lastSeenPlayer
# else if piece at board row col != lastSeenPlayer
# return UNFINISHED
# if lastSeenPlayer is Red
# return RED_WON
# else
# return YELLOW_WON
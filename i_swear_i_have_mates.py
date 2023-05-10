from src.chess.pieces import Colour, Piece
from src.chess.pieces import Pawn, Knight, Bishop, Rook, Queen, King
from src.chess.moves  import Move

class PieceCreator:
    @staticmethod
    def king(colour : int):
        return King(colour)

    @staticmethod
    def queen(colour : int):
        return Queen(colour)

    @staticmethod
    def rook(colour : int):
        return Rook(colour)

    @staticmethod
    def bishop(colour : int):
        return Bishop(colour)

    @staticmethod
    def knight(colour : int):
        return Knight(colour)

    @staticmethod
    def pawn(colour : int):
        return Pawn(colour)

class Board:
    CREATE_PIECE = {
        'k' : PieceCreator.king,
        'q' : PieceCreator.queen,
        'r' : PieceCreator.rook,
        'b' : PieceCreator.bishop,
        'n' : PieceCreator.knight,
        'p' : PieceCreator.pawn
    }

    def __init__(self, board_input : list):
        self.pieces = self.generate_board(board_input)

    def generate_board(self, board_input : list):
        board = []
        size = len(board_input)

        # Append rows to the board
        for i in range(size):
            board.append([])

            # Append pieces to the rows
            for j in range(size):
                piece = self.letter_to_piece(board_input[i][j])
                board[i].append(piece)

        return board
    
    def letter_to_piece(self, letter : str) -> Piece:
        # Return None if the letter represents an empty tile
        if ('0' == letter):
            return None

        # Determine the piece colour
        piece_colour = -1

        if (True == letter.isupper()):
            piece_colour = Colour.BLACK
        elif (True == letter.islower()):
            piece_colour = Colour.WHITE
        else:
            raise ValueError("Piece colour could not be determined for letter",
                             letter, ".")
        
        piece_type = letter.lower()

        # Raise an error if the letter does not represent a valid piece
        if (letter not in Board.CREATE_PIECE.keys()):
            raise ValueError("Piece type could not be determined for letter",
                             letter, ".")

        # Create and return a new piece of the given type
        return Board.CREATE_PIECE[piece_type](piece_colour)

    def possible_moves(self, colour : int) -> list:
        possible_moves = []
        # .extend(list)
        pass

def main():
    lines = []

    for i in range(5):
        lines.append(input())

    board = Board(lines)

if (__name__ == '__main__'):
    main()
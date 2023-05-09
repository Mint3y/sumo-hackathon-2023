class Move:
    def __init__(self, start_position : tuple, end_position : tuple):
        self.start = start_position
        self.end = end_position

class Colour:
    WHITE = 0
    BLACK = 1

class Direction:
    UP = -1
    DOWN = 1

class Piece:
    def __init__(self, colour : int):
        self.colour = colour

class King:
    def __init__(self, colour : int):
        super().__init__(colour)

    def get_possible_moves(self, start_position : tuple, size : int):
        possible_moves = []
        
        # Add moves to adjacent tiles
        for i in range(-1, 1):
            # Skip the move if it places the piece outside of the board
            if ((start_position[0] + i) not in range(size)):
                continue

            for j in range(-1, 1):
                # Skip the move if it places the piece outside of the board
                if ((start_position[1] + j) not in range(size)):
                    continue
                
                end_position = (start_position[0] + i,
                                start_position[1] + j)

                possible_moves.append(Move(start_position, end_position))
        
        return possible_moves

class Queen:
    def __init__(self, colour : int):
        super().__init__(colour)

class Rook:
    def __init__(self, colour : int):
        super().__init__(colour)

class Bishop:
    def __init__(self, colour : int):
        super().__init__(colour)

class Knight:
    def __init__(self, colour : int):
        super().__init__(colour)

class Pawn:
    def __init__(self, colour : int):
        super().__init__(colour)

    def get_possible_moves(self, start_position : tuple, size : int):
        possible_moves = []
        
        direction = 0

        # Determine the direction of the pawn using its colour
        if (self.colour == Colour.WHITE):
            direction = Direction.UP
        elif (self.colour == Colour.BLACK):
            direction = Direction.DOWN
        else:
            raise ValueError("Pawn could not determine direction due to having "
                             "an invalid colour.")

        # Return no moves if the pawn is at the end of the board
        if (((direction == Direction.UP)   and (0        == start_position[0]))
        or  ((direction == Direction.DOWN) and (size - 1 == start_position[0]))):
            return possible_moves

        # Add moves to forward tile and forward left and right tiles
        for i in range(-1, 1):
            # Skip the move if it places the piece outside of the board
            if ((start_position[0] + i) not in range(size)):
                continue
                
            end_position = (start_position[0] + i,
                            start_position[1] + direction)
            
            possible_moves.append(Move(start_position, end_position))
        
        return possible_moves

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
        pass

def main():
    lines = []

    for i in range(5):
        lines.append(input())

    board = Board(lines)

if (__name__ == '__main__'):
    main()
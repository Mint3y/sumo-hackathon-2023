from .moves import Move, Direction

class Colour:
    WHITE = 0
    BLACK = 1

class Piece:
    def __init__(self, colour : int):
        self.colour = colour

class Pawn:
    def __init__(self, colour : int):
        super().__init__(colour)

    def get_possible_moves(self, start_position : tuple, board_size : int):
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
        board_start = 0
        board_end = board_size - 1

        # Return no moves if the pawn is at the end of the board
        if (((direction == Direction.UP)   and (board_start == start_position[0]))
        or  ((direction == Direction.DOWN) and (board_end   == start_position[0]))):
            return possible_moves

        # Add moves to forward tile and forward left and right tiles
        for i in range(-1, 1):
            # Skip the move if it places the piece outside of the board
            if ((start_position[0] + i) not in range(board_size)):
                continue
                
            end_position = (start_position[0] + i,
                            start_position[1] + direction)
            
            possible_moves.append(Move(start_position, end_position))
        
        return possible_moves

class Knight:
    def __init__(self, colour : int):
        super().__init__(colour)


class Bishop:
    def __init__(self, colour : int):
        super().__init__(colour)

class Rook:
    def __init__(self, colour : int):
        super().__init__(colour)

    def get_possible_moves(self, start_position : tuple, board_size : int):
        possible_moves = []

        radius = board_size - 1
        
        # Add moves to tiles in the same row and column
        for i in range(-radius, radius):
            # Add moves if they place the pieces within the board
            # Add row move
            if ((start_position[0] + i) in range(board_size)):
                end_position = (start_position[0] + i, start_position[1])
                possible_moves.append(Move(start_position, end_position))
            
            # Add column move
            if ((start_position[1] + i) in range(board_size)):
                end_position = (start_position[0], start_position[1] + i)
                possible_moves.append(Move(start_position, end_position))

        return possible_moves

class Queen:
    def __init__(self, colour : int):
        super().__init__(colour)

    def get_possible_moves(self, start_position : tuple, board_size : int):
        rook = Rook(self.colour)
        rook_moves = rook.get_possible_moves(start_position, board_size)

        bishop = Bishop(self.colour)
        bishop_moves = bishop.get_possible_moves(start_position, board_size)

        return [*rook_moves, *bishop_moves]

class King:
    def __init__(self, colour : int):
        super().__init__(colour)

    def get_possible_moves(self, start_position : tuple, board_size : int):
        possible_moves = []
        
        # Add moves to adjacent tiles
        for i in range(-1, 1):
            # Skip the move if it places the piece outside of the board
            if ((start_position[0] + i) not in range(board_size)):
                continue

            for j in range(-1, 1):
                # Skip the move if it places the piece outside of the board
                if ((start_position[1] + j) not in range(board_size)):
                    continue
                
                end_position = (start_position[0] + i,
                                start_position[1] + j)

                possible_moves.append(Move(start_position, end_position))
        
        return possible_moves
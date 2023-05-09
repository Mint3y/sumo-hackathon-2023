class Cell:
    WALL_COUNT = 4

    def __init(self, top : bool, right : bool, bottom : bool, left : bool):
        self.top    = top
        self.right  = right
        self.bottom = bottom
        self.left   = left

class Maze:
    def __init__(self, maze_structure : list):
        self.grid = self.generate_empty_grid(15)

        # Build the maze
        for structure in maze_structure:
            # Ignore empty lines
            if (0 == len(structure.strip())):
                continue
                
            cell_info = structure.split(' ')

            # Validate the cell info
            if (6 != len(cell_info)):
                raise ValueError("Maze was given an invalid structure.")

            # Store the instructed position of the cell
            cell_position = (int(cell_info[0]), int(cell_info[1]))

            # Store the active walls of the cell
            wall_active = []

            for i in range(2, 5):
                value = int(cell_info[i])

                if (value not in (0, 1)):
                    raise ValueError("Maze was given an invalid wall value.")

                wall_active.append(bool(value))

            # Update the cell at the instructed position
            self.grid[cell_position[0]][cell_position[1]] = Cell(*wall_active)

    def generate_empty_grid(self, size : int):
        grid = []

        # Create a grid of cells with no walls
        for i in range(size):
            grid.append([])

            for j in range(size):
                grid[i].append(Cell((False, False, False, False)))
        
        return grid

def main():
    filename = "maze.txt"
    file_contents_buffer = ""

    with open(filename, 'r') as maze_file:
        file_contents_buffer = maze_file.read()
    
    maze_structure = file_contents_buffer.split('\n')

    maze = Maze(maze_structure)

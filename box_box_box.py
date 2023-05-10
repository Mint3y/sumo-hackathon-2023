from src.box.sensor     import Header, Data
from src.box.reader     import SensorReader
from src.box.visualiser import Visualiser



def main():
    ###################
    ### Objective 1 ###
    ###################
    reader = SensorReader()

    input_lines = reader.read_lines("splits.txt")

    ###################
    ### Objective 2 ###
    ###################
    header, data = reader.parse_lines(input_lines)

    ###################
    ### Objective 4 ###
    ###################
    visualiser = Visualiser(header, data)

    visualiser.plot_lines('g')
    visualiser.plot_points('ro')
    visualiser.plot_labels()

    visualiser.show()

if (__name__ == '__main__'):
    main()
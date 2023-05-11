from src.box.sensor     import Header, Data
from src.box.reader     import SensorReader
from src.box.visualiser import Visualiser, SplitAnimator

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

    print("Animation may take a while to load. Please wait.")

    SplitAnimator.ANIMATION_SPEED = 0.03

    # visualiser.plot_lines()
    visualiser.plot_lines_animated()
    visualiser.plot_points('ro')
    visualiser.plot_labels()

    visualiser.show()

if (__name__ == '__main__'):
    main()
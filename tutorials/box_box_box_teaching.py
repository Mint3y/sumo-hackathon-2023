##################################################################
# This is a teaching file which demonstrates basic Python concepts
# such as loops, file I/O, string operations and list operations
##################################################################

###################
### Objective 1 ###
###################
filename = "splits.txt"

file_contents_buffer = ""

##############################################################
# The file automatically closes at the end of the 'with' block
# Without the 'with' block, this would look like:

# splits_file = open(filename, 'r')
# file_contents_buffer = splits_file.read()
# close(splits_file)
##############################################################

# Open the file in read-only mode
with open(filename, 'r') as splits_file:
    file_contents_buffer = splits_file.read()

input_lines = file_contents_buffer.split('\n')

###################
### Objective 2 ###
###################

############################################################################
# Note: INFO1910 despises the use of Python for loops and we will avoid them
#       at all costs.
# We would use list comprehensions, however due to there being a beginner
# in our team we will avoid them.
############################################################################

input_data = []

# Iterate the lines of input_lines
i = 0
i_end = len(input_lines)
while (i < i_end):
    # Append the data on each line as a list
    input_data.append(input_lines[i].split(','))
    
    # Iterate the rows of input_data
    j = 0
    j_end = len(input_data[i])
    while (j < j_end):
        # Remove leading and trailing whitespace for each entry
        input_data[i][j] = input_data[i][j].strip()

        j += 1

    i += 1

POSITION_DIMENSIONS = 2

# Obtain the header information (lap and sensor count) from input_data
lap_count    = int(input_data[0][0])
sensor_count = int(input_data[0][1])

sensor_data = []

# Iterate the rows of input_data starting after the header information
i = 1
i_end = len(input_data)
while (i < i_end):
    # Obtain the position of the sensor from input_data
    position_x = input_data[i][0]
    position_y = input_data[i][1]
    sensor_values = []

    # Iterate the columns of input_data starting after the sensor positions
    j = POSITION_DIMENSIONS
    j_end = POSITION_DIMENSIONS + lap_count
    while (j < j_end):
        # Append the sensor readings to a list
        sensor_reading = input_data[i][j]

        sensor_values.append(float(sensor_reading))
        j += 1
    
    # Append a tuple containing this data to sensor_data
    sensor_data.append((position_x, position_y, *sensor_values))

    i += 1
import os
import matplotlib as mpl

class Header:
    HEADER_LENGTH = 2
    POSITION_DIMENSIONS = 2

    def __init__(self, header : list):
        # Raise an error if the header length is incorrect
        if (HEADER_LENGTH != len(header)):
            raise ValueError("Attempted to read incorrect header.")

        # Validate and store lap_count
        if (False == header[0].isdecimal):
            raise ValueError("Header laps is in an incorrect format.")

        self.lap_count = header[0]

        # Validate and store sensor_count
        if (False == header[1].isdecimal):
            raise ValueError("Header laps is in an incorrect format.")

        self.sensor_count = header[1]

class Sensor:
    def __init__(self, sensor_data : list, header : Header):
        # Raise an error if the sensor data length is incorrect
        data_length = Header.POSITION_DIMENSIONS + header.lap_count
        if (len(sensor_data) != data_length):
            raise ValueError("Sensor data length is incorrect.")

        # Parse the sensor data
        data = parse_data(sensor_data)

        # Store the sensor's position and readings
        self.position = tuple(*data[:Header.POSITION_DIMENSIONS])
        self.readings = tuple(*data[Header.POSITION_DIMENSIONS - 1:])

    def parse_data(self, sensor_data : list):
        parsed_data = []

        # Validate and store sensor position
        for i in range(Header.POSITION_DIMENSIONS):
            value = sensor_data[i]

            if (False == value.isdecimal()):
                raise ValueError("Sensor position is incorrect.")
            
            parsed_data.append(int(value))
        
        # Validate and store sensor readings
        for i in range(Header.POSITION_DIMENSIONS, len(sensor_data)):
            # Remove the first decimal place (to identify floats)
            value = sensor_data[i].replace('.', '', 1)

            if (False == value.isdecimal()):
                raise ValueError("Sensor reading is invalid.")

            parsed_data.append(float(value))
        
        return parsed_data

class Data:
    def __init__(self, data : list, header : Header):
        # Raise an error if the sensor count is incorrect
        if (header.sensor_count != len(data)):
            raise ValueError("Attempted to read incorrect data.")

        # Store each sensor
        self.sensor_data = []

        for sensor in data:
            self.sensor_data.append(Sensor(sensor, header))
        
class SensorReader:
    def read_lines(self, filename : str) -> list:
        # Raise an error if the file does not exist
        file_exists = os.path.isfile(filename)

        if (False == file_exists):
            raise FileNotFoundError(filename + " was not found.")

        # Read the file contents into a buffer
        file_contents_buffer = ""

        with open(filename, 'r') as splits_file:
            file_contents_buffer = splits_file.read()

        # Split the buffer by newline characters
        input_lines = file_contents_buffer.split('\n')

        return input_lines
    
    def parse_lines(self, lines : list) -> list:
        # Raise an error if the input is empty
        if (0 == len(lines)):
            raise ValueError("Attempted to parse empty lines.")

        # Remove trailing whitespace and commas
        clean_lines = [line.rstrip(' ').rstrip(',') for line in lines]
        
        # Split each line by commas
        raw_input = [line.split(',') for line in clean_lines]

        # Strip all entries of whitespace
        stripped_input = []

        for line in raw_input_data:
            stripped_input.append([entry.strip() for entry in line])

        # Remove all empty lines
        clean_input = [line for line in stripped_input if (0 != len(line))]

        # Read the header information
        header = Header(clean_input[0])

        # Slice the data off the list of lines
        raw_data = clean_input[1:]

        # Read the data
        data = Data(raw_data, header)

        return (header, data)

def main():
    reader = SensorReader()

    ###################
    ### Objective 1 ###
    ###################
    input_lines = reader.read_lines("splits.txt")

    ###################
    ### Objective 2 ###
    ###################
    header, data = reader.parse_lines(input_lines)

if (__name__ == '__main__'):
    main()
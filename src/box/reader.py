import os

from .sensor import Header, Data

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

        for line in raw_input:
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
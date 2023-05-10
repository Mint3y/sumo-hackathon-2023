class Header:
    HEADER_LENGTH = 2
    POSITION_DIMENSIONS = 2

    def __init__(self, header : list):
        # Raise an error if the header length is incorrect
        if (self.HEADER_LENGTH != len(header)):
            raise ValueError("Attempted to read incorrect header.")

        # Validate and store lap_count
        if (False == header[0].isdecimal):
            raise ValueError("Header laps is in an incorrect format.")

        self.lap_count = int(header[0])

        # Validate and store sensor_count
        if (False == header[1].isdecimal):
            raise ValueError("Header laps is in an incorrect format.")

        self.sensor_count = int(header[1])

class Sensor:
    def __init__(self, sensor_data : list, header : Header):
        # Raise an error if the sensor data length is incorrect
        data_length = Header.POSITION_DIMENSIONS + header.lap_count
        if (len(sensor_data) != data_length):
            raise ValueError("Sensor data length is incorrect.")

        # Parse the sensor data
        data = self.parse_data(sensor_data)

        # Store the sensor's position and readings
        self.position = tuple([*data[:Header.POSITION_DIMENSIONS]])
        self.readings = tuple([*data[Header.POSITION_DIMENSIONS - 1:]])

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
import os
import glob
import csv


def load_sensor_data():
    sensor_data = []
    # This creates a list of csv file names in the datasets dir
    sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))
    for sensor_file in sensor_files:
        with(open(sensor_file)) as data_file:
            # This creates an instance of DictReader which is essentially a special dict
            # First line of csv (headers) are used as keys to create a map with all the values
            data_reader = csv.DictReader(data_file, delimiter=',')
            for row in data_reader:
                sensor_data.append(row)
    return sensor_data

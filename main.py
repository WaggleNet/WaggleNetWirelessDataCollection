import importlib
import os

files_in_sensors = os.listdir('sensors')

for file in files_in_sensors:
    class_name = file.split('.')[0]
    print(f'importing {class_name} from {file}')
    sensor_module = importlib.import_module(file, class_name)

import json
import database

def sensor_data_callback(payload: str) -> None:
    data = json.loads(payload)
    database.upload_sensor_data(data['hive_id'], data['sensor_id'], data['timestamp'], data['sensor_value'])
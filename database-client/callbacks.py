import json
import database

def sensor_data_callback(client, userdata, msg) -> None:
    data = json.loads(msg.payload)
    database.upload_sensor_data(data['hive_id'], data['sensor_id'], data['timestamp'], data['value'])

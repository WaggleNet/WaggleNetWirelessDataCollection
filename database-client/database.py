from pymongo import MongoClient
from datetime import datetime

HOST = "temp"
PORT = "temp"
DATABASE_NAME = "temp"

db_client = MongoClient(HOST, PORT)
db = db_client['hive-data']

def upload_sensor_data(hive_id: str, sensor_id: str, timestamp: int, sensor_value) -> None:
    data = {
        'hive_id': hive_id, # identifying string for which hive
        'sensor_id': sensor_id, # identifying string for which sensor within a hive
        'timestamp': timestamp, # unix timestamp in ms of when the data was retrieved
        'value': sensor_value, # sensor value
    }
    db.sensor_data.insert_one(data)

def get_sensor_data(hive_id: str, sensor_id: str, num_data_points: int, 
                    recent: bool=True, begin_time: int=0, end_time: int=-1) -> list:
    if(end_time == -1):
        # get current timestamp in ms
        end_time = int(datetime.now(datetime.timezone.utc).timestamp()) * 1000

    query_result = db.sensor_data.find({ 
        'hive_id': hive_id,
        'sensor_id': sensor_id,
        'time_stamp': {'gte': begin_time, 'lte': end_time}
    }).sort({
        'time_stamp', -1 if recent else 1
    }).limit(num_data_points)
    
    return list(query_result)
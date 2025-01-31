import sensor_data_pb2
import database

def sensor_data_callback(client, userdata, msg) -> None:
    message = sensor_data_pb2.SensorData()
    message.ParseFromString(msg.payload)
    value_dtype_field = message.WhichOneof("value")
    database.upload_sensor_data(message.hive_id, message.sensor_id, message.timestamp, getattr(message, value_dtype_field))
    print(client, userdata, message)
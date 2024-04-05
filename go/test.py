import requests
import time
import numpy as np

url = 'http://localhost:8080/upload'

for i in range(9999):
    data = {'number' : str(i), 'array' : None}
    data['array'] = list(np.random.randint(10, size=1000).astype(float))
    post = requests.post(url, json = data)
    print(f'request: {data} sent')
    print("not sleeping")
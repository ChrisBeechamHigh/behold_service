
import requests

url = "http://127.0.0.1:8080/predictions/resnet-18"
files = {'data': open('files/kitten.jpg','rb')}

resp = requests.post(url, files=files)

data = resp.json()
assert('tabby' in data.keys())
assert('monkey' not in data.keys())

files = {'data': open('files/dog.jpg','rb')}

resp = requests.post(url, files=files)

data = resp.json()
assert('German_shepherd' in data.keys())
assert('tabby' not in data.keys())


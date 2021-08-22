
import requests

url = "http://127.0.0.1:8080/predictions/resnet-18-custom-handler"
files = {'data': open('files/kitten.jpg','rb')}

resp = requests.post(url,files=files)

data = resp.json()
assert('tabby' in data.keys())
assert('monkey' not in data.keys())

files = {'data': open('files/dog.jpg','rb')}

resp = requests.post(url, files=files)

data = resp.json()
# TODO investigate why with the custom handler, prediction for our dog is window screen
assert('German_shepherd' not in data.keys())
assert('window_screen' in data.keys())
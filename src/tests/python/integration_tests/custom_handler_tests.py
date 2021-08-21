
import requests
import json

"""

5 archiver:
torch-model-archiver --model-name resnet-18-custom-handler --version 1.0 --model-file ./serve/examples/image_classifier/resnet_18/model.py --handler ./serve/custom_handler/custom_image_handler.py --extra-files ./serve/examples/image_classifier/index_to_name.json,./serve/custom_handler/custom_image_handler.py --export-path model_store --force


url points to the archived model file generated via the torch-model-archiver for the inference service
6. start torchserve to serve model (where do you run this from?)
torchserve.exe --start --ncs --model-store model_store --models resnet-18-custom-handler.mar

7. stop torchserve
torchserve.exe --stop
"""

url = "http://127.0.0.1:8080/predictions/resnet-18-custom-handler"
files = {'data': open('files/kitten.jpg','rb')}

resp = requests.post(url,files=files)

#print(resp.text)

data = resp.json()

print (data)

#print (data["tabby"])
#print (data.keys())

#assert(data.keys() == ['tabby', 'tiger_cat', 'Egyptian_cat', 'lynx', 'bucket'])

#assert('tabby' in data.keys())
#assert('monkey' not in data.keys())
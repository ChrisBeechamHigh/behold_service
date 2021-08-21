"""
manual steps to run the torchserver instance (use Anaconda Power Shell for windows as described here)

1. create new directory (e.g. torchserve)

2. got to new directory torchserve and clone TorchServe repo
git clone https://github.com/pytorch/serve.git

3. create folder model_store under new directory torchserve

4. download resnet-18.mar file from Model zoo https://pytorch.org/serve/model_zoo.html

5. archive model using model archiver
torch-model-archiver --model-name resnet-18 --version 1.0 --model-file ./serve/examples/image_classifier/resnet-18/model.py --extra-files ./serve/examples/image_classifier/index_to_name.json --serialized-file densenet161-8d451a50.pth --export-path model_store --handler image_classifier --force
[check step is this required and with what params - can we provide archived model in repo?]

6. start torchserve to serve model (where do you run this from?)
torchserve.exe --start --ncs --model-store model_store --models resnet-18.mar

[make sure using python 3.8
if multiple python environments in Anaconda Power Shell run:
conda env list
conda activate py38
]

7. run the script below and check that assertions pass

see
https://github.com/pytorch/serve/blob/master/README.md#serve-a-model

and windows instructions:
https://github.com/pytorch/serve/blob/master/docs/torchserve_on_win_native.md

TODO look at using torchserver docker container to avoid manual steps

"""


import requests
import json

url = "http://127.0.0.1:8080/predictions/resnet-18"
files = {'data': open('files/kitten.jpg','rb')}

resp = requests.post(url,files=files)

data = resp.json()

print (data["tabby"])
print (data.keys())

#data.keys will be e.g. ['tabby', 'tiger_cat', 'Egyptian_cat', 'lynx', 'bucket'])

assert('tabby' in data.keys())
assert('monkey' not in data.keys())


Running simple inference
========================

1. create new directory (e.g. torchserve)

2. got to new directory torchserve and clone TorchServe repo
git clone https://github.com/pytorch/serve.git

3. create folder model_store under new directory torchserve

4. download resnet-18.mar file from Model zoo https://pytorch.org/serve/model_zoo.html and copy to model_store folder

5. start torchserver server in e.g. Anaconda Powershell Prompt:

torchserve.exe --start --ncs --model-store model_store --models resnet-18.mar

[ensure python 3.8 installed on machine and run the following commands in Powershell to activate it if multiple environments
conda activate py38]

6. Run integration tests tests/python/integration_tests/simple_inference_tests.py in suitable IDE e.g. PyCharm or on command line and ensure no assertion errors

Running inference with custom handler
=====================================

1. download resnet18-f37072fd.pth file from https://download.pytorch.org/models/resnet18-f37072fd.pth and place in directory created in step 1 above

2. run archiver to create new .mar file:

torch-model-archiver --model-name resnet-18-custom-handler --version 1.0 --model-file ./serve/examples/image_classifier/resnet_18/model.py --handler ./serve/custom_handler/custom_image_handler.py --serialized-file resnet18-f37072fd.pth --extra-files ./serve/examples/image_classifier/index_to_name.json,./serve/custom_handler/custom_image_handler.py --export-path model_store --force

3. copy src/main/python/behold_service/handler/custom_image_handler.py to serve/custom_handler

4. start torchserver server in e.g. Anaconda Powershell Prompt:

torchserve.exe --start --ncs --model-store model_store --models resnet-18-custom-handler.mar

5. Run integration tests tests/python/integration_tests/custom_handler_tests.py in suitable IDE e.g. PyCharm or on command line and ensure no assertion errors


Security measures
=================



Application performance
========================

In AWS can configure GPU type and number of GPUs for improved throughput

See documentation below about number_of_gpu setting, number_of_gpu should usually match number of assigned

"https://github.com/pytorch/serve/blob/master/README.md#serve-a-model

Concurrency And Number of Workers

TorchServe exposes configurations that allow the user to configure the number of worker threads on CPU and GPUs.
There is an important config property that can speed up the server depending on the workload.
Note: the following property has bigger impact under heavy workloads. If TorchServe is hosted on a machine with GPUs,
there is a config property called number_of_gpu that tells the server to use a specific number of GPUs per model.
In cases where we register multiple models with the server, this will apply to all the models registered.
If this is set to a low value (ex: 0 or 1), it will result in under-utilization of GPUs.
On the contrary, setting to a high value (>= max GPUs available on the system) results in as many workers getting spawned per model.
Clearly, this will result in unnecessary contention for GPUs and can result in sub-optimal scheduling of threads to GPU.

ValueToSet = (Number of Hardware GPUs) / (Number of Unique Models)"

There are a number of other properties designed for performance tuning listed here:

https://pytorch.org/serve/configuration.html

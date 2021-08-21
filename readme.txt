Security measures


Application performance

In AWS can configure GPU type and number of GPUs for improved throughput

See documentation below about number_of_gpu setting

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

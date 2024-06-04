# TrojAI

The trojAI is the top-level module

`datagen` and `modelgen` are its two submodules. 
The required API functions are included in `datagen`, which allows you to easily create synthetic data that can be used to train machine learning models. The required API functions to quickly create DNN models from the generated data are included in the `modelgen` module. 

The trojai Package contains the required package to run the program. Below are the general details.

setup.py - Script to install trojai module into Python environment
  
    datagen - integration scripts showcasing datagen API functionality
    modelgen - integration scripts showcasing modelgen API functionality
  
  trojai - top level Python module (Package)
    └───datagen - data generation submodule
    └───modelgen - model generation submodule
    └───test - top level scripts directory
         └───datagen - contains unittests for the datagen submodule
         └───modelgen - contains unittests for the modelgen submodule

# Datagen
### Getting Started
# Activate the trojai environment 
# Download the MNIST Dataset to /tmp/mnist/clean/ as the root folder
>> python mnist_utils.py /tmp/mnist/clean/train.csv /tmp/mnist/clean/test.csv
# Generate the Badnets Dataset and store the output into root folder /tmp/mnist/badnets
>> python mnist_badnets.py /tmp/mnist/clean/train.csv /tmp/mnist/clean/test.csv --output /tmp/mnist/badnets

# Modelgen
# Activate the trojai environment 
# Generate MNIST badnets data, and train a trojaned model by training directly on the poisoned dataset
>> python gen_and_train_mnist.py
# Generate MNIST badnets data, and train a trojaned model using sequential training; first on the clean dataset, and second on the poisoned dataset
>> python gen_and_train_mnist_sequential.py


# Conclusion:
>>Introduced the trojai framework for generating triggered datasets and corresponding trojaned models.
>>Employed the created system to produce a substantial collection of compromised MNIST classifiers.
>>The training batch size, dataset poisoning percentage, and trigger type all have an impact on the successful embedding of trojans, according to MNIST results.
>>Tests and results show that the TrojAI software framework can be used to quickly and thoroughly test new trojan detection techniques. 
>>It will also help researchers understand the effects of different dataset configurations and training hyperparameters on the generated trojaned deep learning model

# References:
https://github.com/trojai
https://trojai.readthedocs.io/en/latest/
https://arxiv.org/abs/2003.07233
 Karra Kiran and Ashcraft Chace and Fendley Neil ,The TrojAI Software Framework: An OpenSource tool for Embedding Trojans into Deep Learning Models (2020)

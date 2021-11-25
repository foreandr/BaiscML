import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.python.client import device_lib

def get_available_gpus():
    local_device_protos = device_lib.list_local_devices()
    return [x.name for x in local_device_protos if x.device_type == 'GPU']

x1 = tf.Variable(1)

print(device_lib.list_local_devices())
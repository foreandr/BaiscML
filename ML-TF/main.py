#CAN'T USE TENSORFLOW TILL THIS SHIT IS FIXED
import tensorflow as tf

xint1 = tf.Variable(1)
xint2 = tf.Variable(2)
z = tf.add(xint1, xint2)
print(z)
# tf.test.gpu_device_name() # GPU isn't registering



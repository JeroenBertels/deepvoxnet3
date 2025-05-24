import tensorflow as tf

print(tf.config.list_physical_devices())
print(tf.test.is_built_with_cuda())
print(tf.test.is_gpu_available())

# Tensor created on CPU
with tf.device('/CPU:0'):
    x = tf.constant([1.0, 2.0, 3.0])
    print("x device:", x.device)

# Now use x in a GPU context
with tf.device('/GPU:0'):
    y = x * 2
    print("y device:", y.device)


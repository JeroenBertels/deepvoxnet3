import tensorflow as tf

print(tf.config.list_physical_devices())
print(tf.test.is_built_with_cuda())

# Tensor created on CPU
with tf.device('/CPU:0'):
    x = tf.Variable([1.0, 2.0, 3.0])
    print("CPU?: x device:", x.device)

print("CPU?: x device:", x.device)
# Now use x in a GPU context
with tf.device('/GPU:0'):
    print("GPU?: x device:", x.device)
    x_ = x
    print("GPU?: x_ device:", x_.device)
    y = x * 2
    print("GPU?: y device:", y.device)
    x__ = tf.Variable(x)
    print("GPU?: x__ device:", x__.device)
    x__[0].assign(9)

print("GPU?: x device:", x.device)
print("GPU?: x_ device:", x_.device)
print("GPU?: y device:", y.device) 
print("GPU?: x__ device:", x__.device)
print(x)
print(y)
print(x_)
print(x__)

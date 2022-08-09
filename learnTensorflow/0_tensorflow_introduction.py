# 0_tensorflow_introduction.py
# 
# prerequistics:
# pip install tensorflow
# or
# pip install tensorflow-gpu
# Usage:
# python 0_tensorflow_introduction.py

# import tensorflow library
import tensorflow as tf
# print tensorflow version
print(" Using tensorflow version:", tf.__version__)

# Datatype
#
# Tensor is a higher dimension data point. It can have 1, 2, 3, ... dimensions.
# Scalar is 1 value, vector is 1 dimensional array, matrix is 2 dimensions array.
# Finally a tensor is n dimensional array.

# Creating Tensors : it can be a string, integer and floating number
print("  We can create a tensor using tf.Variable command, it can be a string, integer or a floating number")
string   = tf.Variable("this is a string", tf.string)
number   = tf.Variable(123, tf.int16)
floating = tf.Variable(3.149, tf.float64)

# Rank of Tensors : It is the dimensions involved in the tensor.  The above tensors are of rank 0
# Scalers are rank 0 dimensions, since they don't have any dimensions. Array have dimensions thus
# they can have some dimensions. Esstially it is the deepest level of a the array.
#
# Rank 1 tensor 
rank1_tensor = tf.Variable(["This ", "is a ", "rank 1 tensor"], tf.string)
rank2_tensor = tf.Variable([["This", "is"],["a", " rank 2 tensor"]], tf.string)
# To get a tensor we can use a tf.rank command
print("  This is a rank of rank1_tensor", tf.rank(rank1_tensor))
print("  This is a rank of rank2_tensor", tf.rank(rank2_tensor))

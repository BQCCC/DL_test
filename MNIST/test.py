from __future__ import print_function

import argparse


# from keras.datasets import mnist
# from keras.layers import Input
import tensorflow
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Input

# from scipy.misc import imsave
import imageio

from Model1 import Model1
from Model2 import Model2
from Model3 import Model3
from configs import bcolors
from utils import *

a = tensorflow.Variable

# b = tensorflow.Variable()

t = tensorflow.ones((3, 3))
print("t: ", t)

# t = t * 3

t_2 = t*3.0

print("t: ", t)
print("t_2: ", t_2)

print("hello world")



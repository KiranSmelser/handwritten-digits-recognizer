"""_summary_
"""

from PIL import Image
import mnist
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix

def main():
    # Create training variables.
    x_train = mnist.train_images()
    y_train = mnist.train_labels()
    # Create testing variables.
    x_test = mnist.test_images()
    y_test = mnist.test_labels()
    # Format data.
    x_train = x_train.reshape((-1, 28*28))
    x_test = x_test.reshape((-1, 28*28))
    x_train = x_train / 256
    x_test = x_test / 256
main()
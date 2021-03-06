"""This program utilizes machine learning to determine which digit is present in an 28x28 pixel image file that contains a handwritten digit.
"""

from PIL import Image
import mnist
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from image_to_bytes import image_to_byte
from drawing_window import draw_with_mouse

def accuracy(confusion_matrix):
    """This fuction determines the accuracy of the created recognition model.
    Arguments: confusion_matrix is an array of integers.
    Returns: An accuracy score for the model.
    """
    diagonal = confusion_matrix.trace()
    elements = confusion_matrix.sum()
    return diagonal / elements

def main():
    # Create training variables
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
    # Create model.
    clf = MLPClassifier(solver='adam', activation='relu', hidden_layer_sizes=(64,64))
    clf.fit(x_train, y_train)
    predictions = clf.predict(x_test)
    acc = confusion_matrix(y_test, predictions)
    # Predicts digit based on user input.
    draw_with_mouse()
    digit = image_to_byte()
    digit = np.array(digit)/256
    digit = digit.reshape(1, -1)
    p = clf.predict(digit)
    print(f"Prediction: {p[0]}")
    # Accuracy of recognizer.
    print(f"Accuracy: {accuracy(acc)*100}%")

if __name__ == "__main__":
    main()
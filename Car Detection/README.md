Convolutional Neural Network for Car Recognition

The code contains a basic car recognizer using keras library.

We have implemented a simple convolutional neural network that achieves over 95% accuracy

In the architecture of the Conv net, we have a following layers:

    Conv layer
    ReLU activation
    Pool layer
    Conv layer
    ReLU activation
    Pool layer
    Fully connected layer
    Softmax layer

Datasets:

We have 1210 images along with label as Training dataset, and the remaining images as Testing dataset

Setup:

    Install sklearn using sudo pip install sklearn
    Install keras using sudo pip install keras
    Install skimage using sudo pip install scikit-image

Execute:

python car.py
(The directory of the datasets must be edited in the program accordingly.)

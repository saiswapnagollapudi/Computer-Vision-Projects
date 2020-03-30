from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
(X_train,y_train),(X_test,y_test) = mnist.load_data()
plt.subplot(221)
plt.imshow(X_train[0], cmap = plt.get_cmap('gray'))
plt.subplot(222)
plt.imshow(X_train[1], cmap = plt.get_cmap('gray'))
plt.subplot(223)
plt.imshow(X_train[2], cmap = plt.get_cmap('gray'))
plt.subplot(224)
plt.imshow(X_train[3], cmap = plt.get_cmap('gray'))
plt.show()
#first lets build a multi-layer perceptron model as base model
#flatten 28*28 to a vector of dimension 784 for each image
num_pixels  = X_train.shape[1] * X_train.shape[2]
(X_train,y_train),(X_test,y_test) = mnist.load_data()
X_train = X_train.reshape((X_train.shape[0],28,28,1)).astype('float32')
X_test = X_test.reshape((X_test.shape[0],28,28,1)).astype('float32')
X_train = X_train/255
X_test = X_test/255
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
num_classes = y_train.shape[1]

def cnn_model():
    model = Sequential()
    model.add(Conv2D(30,(5,5),input_shape=(28,28,1),activation = 'relu'))
    model.add(MaxPooling2D())
    model.add(Conv2D(15,(3,3),activation = 'relu'))
    model.add(MaxPooling2D())
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(128,activation = 'relu'))
    model.add(Dense(50,activation = 'relu'))
    model.add(Dense(num_classes, activation = 'softmax'))
    model.compile(loss = 'categorical_crossentropy',optimizer = 'adam', metrics = ['accuracy'])
    return(model)
model  = large_cnn()
model.fit(X_train,y_train,validation_data = (X_test,y_test),epochs = 10, batch_size = 200,verbose = 0)
scores = model.evaluate(X_test,y_test)
print("% of classification error for large cnn ",100 -scores[1]*100)

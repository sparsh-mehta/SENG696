import tensorflow as tf
import matplotlib.pyplot as plt
from keras.applications.vgg19 import VGG19
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
#from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg19 import decode_predictions
#import cv2

model = VGG19()

# load an image from file
image = load_img('cat.jpeg', target_size=(224, 224))
plt.imshow(image)
# convert the image pixels to a numpy array
image_array = img_to_array(image)
# reshape data for the model
image_array = image_array.reshape((1, image_array.shape[0], image_array.shape[1], image_array.shape[2]))
# predict the probability across all output classes
yhat = model.predict(image_array)
# convert the probabilities to class labels
label = decode_predictions(yhat)
#print(label)
# retrieve the most likely result, e.g. highest probability
label = label[0][0]
#print(label)
# print the classification
print('%s (%.2f%%)' % (label[1], label[2]*100))
image_array = image_array.reshape((image_array.shape[1], image_array.shape[2], image_array.shape[3]))
#plt.imshow(image, interpolation='nearest')
plt.imshow(image);
plt.title(f"prediction: {label[1]} - Accuracy: {label[2]*100}")
plt.show()
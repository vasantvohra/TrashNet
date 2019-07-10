import os
import cv2
import tensorflow as tf
import numpy as np

#import keras
def predict(filename):
    CATEGORIES=['cardboard','glass','metal','paper','plastic','trash']
 # so that our model classifies in these labels only


    def prepare(filepath): # we have to adjust our input image according to our training data set dimensions
        IMG_SIZE = 150  # 50 in txt-based
        img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
        return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

    model = tf.keras.models.load_model("trashnet98.h5") # this is tensorflow serving importing an keras deep leaerning save module

    prediction = model.predict([prepare(filename)]) # this is the image we want to classify

    os.remove(filename)
    d=float(prediction[0][0])
    text= CATEGORIES[np.argmax(prediction[0])]
    text= text+"\t"+ str(d)+'\n'+"Filename: \t"+str(filename)
    print("Classification :\n",text)
    return text

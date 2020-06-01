import os
#import cv2
import tensorflow as tf
import numpy as np
from keras.preprocessing import image
import json
from flask import Flask, render_template, request, jsonify,abort
from PIL import Image

app=Flask(__name__)
UPLOAD_FOLDER = os.path.basename('.')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
                    
def predict(img_path):
     labels={0: 'Cardboard', 1: 'Glass', 2: 'Metal', 3: 'Paper', 4: 'Plastic', 5: 'Trash'}
     img = image.load_img(img_path, target_size=(224,224))
     img = image.img_to_array(img, dtype=np.uint8)
     img = np.array(img)/255.0
     model = tf.keras.models.load_model("VGG16GarbageClassifier.h5")
     predicted = model.predict(img[np.newaxis, ...])
     prob = np.max(predicted[0], axis=-1)
     prob = prob*100
     prob = round(prob,2)
     prob = str(prob) + '%'
     print("p.shape:",predicted.shape)
     print("prob",prob)
     predicted_class = labels[np.argmax(predicted[0], axis=-1)]
     print("classified label:",predicted_class)
     result=''
     if predicted_class in ['Cardboard','Paper']:
          category = "Biodegradable"
          predicted_class = str(predicted_class)
          probability = str(prob)
          return category,predicted_class,probability
          #result += "Biodegradable" +'\n' + str(predicted_class) + '\n' + str(pro)
     elif predicted_class in ['Metal','Glass','Plastic']:
          category = "Non-Biodegradable"
          predicted_class = str(predicted_class)
          probability = str(prob)
          return category,predicted_class,probability
          #result += "Nonbiodegradable"+'\n'+ str(predicted_class) + '\n' + str(pro)
     else:
          category = "Categorizing Difficult"
          predicted_class = str(predicted_class)
          probability = str(prob)
          return category,predicted_class,probability
          #result = predicted_class + '\n' + str(pro)
     #return(result)
#category,predicted_class,probability = predict(Image_path)
     
@app.route("/", methods = ['POST']) #/file
def application():
     file = ""
     answer = None
     if request.method == "POST":
          file = request.files["file"]
          print(request.json)
          if file:
               f = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
               file.save(f)
               result = predict(file.filename)
               if result:
                    a = {"success":"True","result":result}
                    return json.dumps(a)
               else:
                    abort(400)

if __name__ == "__main__":
    app.run(debug=True)

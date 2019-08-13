#from flask import Flask
#from flask import render_template
#from flask import request
#from PIL import Image
from prediction import *
import os
import cv2
from flask import Flask, render_template, request,jsonify
from PIL import Image
import tensorflow as tf
#import jinja2
app=Flask(__name__)
#app.jinja_env.line_statement_prefix = '%'
UPLOAD_FOLDER = os.path.basename('.')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", methods=['GET', 'POST'])
def application():
    file=""
    answer = None
    error=""
    if request.method=="POST":
        try:
            file= request.files["image"]
            #if file.strip()=="":
              #  error="Pl. upload an Image"
            if file:
                #upload
                f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(f)
                print(file.filename)
                #read
                #image = cv2.imread(UPLOAD_FOLDER+"/"+file.filename)
                #filename = "{}.png".format(os.getpid())
                
                #cv2.imwrite(filename, image)
                #print(filename)
                
                # Deleting from path after uploading
                result=predict(file.filename)
                #os.remove(filename)
                if result=="":
                    error="Sorry!"
                    
        except(SyntaxError) as e:
            error ="Could not understand"
            print("Error:" + str(e))

        try:
            if result!="Sorry!":
                answer=result
        except Exception as e:
            print(e)

    return render_template('index.html', file=file,
                           answer=answer, error=error)


if __name__ == "__main__":
    app.run(debug=True)

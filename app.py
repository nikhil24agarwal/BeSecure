import os
from flask import Flask,flash,render_template,url_for,request,redirect
from werkzeug.utils import secure_filename
app = Flask(__name__)
import cv2
import string
from funtions import enc

app.config["IMAGE_UPLOADS"] = "C:/Users/Hp/Desktop/Projects/besure/static/image/uploads"

@app.route("/")
def home():
   return render_template('index.html')

    
@app.route("/dec")
def decryption():
    return "hello"



@app.route("/enc", methods=["GET", "POST"])

def encryption():
    if request.method == "POST":
        form = request.form
        key = form['key']
        msg= form['msg']

        if request.files:
            image = request.files["image"]
            print("hellooooooooooooooooooooooooooooooooooo")
            print(app.config["IMAGE_UPLOADS"])
            print(image.filename)
            print(app.config["IMAGE_UPLOADS"]+ "/" + image.filename)
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

            enc(key, 0, app.config["IMAGE_UPLOADS"] + "/" + image.filename ,  "hey my name is nikhil")
            return render_template('upload_image.html')
    return render_template("upload_image.html")




app.run(debug=True, use_debugger=False, use_reloader=False)
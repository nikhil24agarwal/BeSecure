import os
from flask import Flask,flash,render_template,url_for,request,redirect
from werkzeug.utils import secure_filename
app = Flask(__name__)
import cv2
import string
from funtions import enc
from funtions import dec

app.config["IMAGE_UPLOADS"] = "C:/Users/Hp/Desktop/Projects/besure/static/image/uploads"

@app.route("/")
def home():
   return render_template('index.html')

    
@app.route("/decry" , methods=["GET", "POST"])
def decryption():
    # print(request.method)
    if request.method == "POST":
        form = request.form
        key = form['key']
        # print(form)
        # print(request.files)
        if request.files:
            image = request.files["image"]
           
            # print("chuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
            a = dec(key, app.config["IMAGE_UPLOADS"] + "/" + image.filename)
            # print("prachuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
            # print(a)
            return render_template('index.html')
    return render_template('index.html')



@app.route("/encry", methods=["GET", "POST"])
def encryption():
    # print("heloooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")

    if request.method == "POST":
        form = request.form
        key = form['key']
        msg = form['msg']
        

        if request.files:
            image = request.files["image"]
            # print(app.config["IMAGE_UPLOADS"])
            # print(image.filename)
            # print(app.config["IMAGE_UPLOADS"]+ "/" + image.filename)
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

            enc(key, msg, app.config["IMAGE_UPLOADS"] + "/" + image.filename)
            return render_template('index.html')
    return render_template("index.html")




app.run(debug=True, use_debugger=False, use_reloader=False)
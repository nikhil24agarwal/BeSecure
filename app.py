import os
from flask import Flask,flash,render_template,url_for,request,redirect
from werkzeug.utils import secure_filename
app = Flask(__name__)
import cv2
import string
from funtions import enc
from funtions import dec
import random

app.config["IMAGE_UPLOADS"] = "C:/Users/Hp/Desktop/Projects/besure/static/image/uploads"

@app.route("/")
def home():
   return render_template('index.html')

    
@app.route("/decry" , methods=["GET", "POST"])
def decryption():
    # print(request.method)
    if request.method == "POST":
        form = request.form
        key1 = form['key1']
        key2 = form['key2']
        

        # print(form)
        # print(request.files)
        if request.files:
            image = request.files["image"]
           
            # print("chuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
            a = dec(key1, app.config["IMAGE_UPLOADS"] + "/" + image.filename)
            print(a,"dec init")
            msg = a
        
            k = int(key2)
            # print("prachuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
            msg_list = []
            for i in msg:
                if(ord(i)==32):
                    msg_list.append(" ")
                    continue
                ee=chr((((ord(i)-97+6)-k)%26)+65)
                msg_list.append(ee)
            msg="".join(msg_list)
            a = msg
            print(a, "fin dec a")
            return render_template('index.html',a=a)
    return render_template('index.html')



@app.route("/encry", methods=["GET", "POST"])
def encryption():
    #code for deffie hellman


    
    
    # print("heloooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo")
    if request.method == "POST":
        form = request.form
        key1 = form['key1']
        key2= form['key2']
        msg = form['msg']
        print(msg,"enc init")

        msg=msg.lower()
        msg_list = []
        k = int(key2)
        for i in msg:
            if(ord(i)==32):
                msg_list.append(" ")
                continue
            ee=chr((((ord(i)-97)+k)%26)+65)
            msg_list.append(ee)

        msg = "".join(msg_list)
        print(msg)
        if request.files:
            image = request.files["image"]
            # print(app.config["IMAGE_UPLOADS"])
            # print(image.filename)
            # print(app.config["IMAGE_UPLOADS"]+ "/" + image.filename)
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

            path=enc(key1, msg, app.config["IMAGE_UPLOADS"] + "/" + image.filename)
            return render_template('index.html',path=path)
    return render_template("index.html")




app.run(debug=True, use_debugger=False, use_reloader=False)
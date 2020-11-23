import cv2
import string
import os


def enc(key, choice, img, text):
    d={}
    c={}

    for i in range(255):
        d[chr(i)]=i
        c[i]=chr(i)

    x=cv2.imread(img)

    i=x.shape[0]
    j=x.shape[1]
    if (choice == 0):  #encrpyt
        kl=0
        tln=len(text)
        z=0 #decides plane
        n=0 #number of row
        m=0 #number of column

        l=len(text)

        for i in range(l):
            x[n,m,z]=d[text[i]]^d[key[kl]]
            n=n+1
            m=m+1
            m=(m+1)%3 #this is for every value of z , remainder will be between 0,1,2 . i.e G,R,B plane will be set automatically.
                        #whatever be the value of z , z=(z+1)%3 will always between 0,1,2 . The same concept is used for random number in dice and card games.
            kl=(kl+1)%len(key)
            
        cv2.imwrite("static/image/uploads/encrypted_img.jpg", x)
    return 


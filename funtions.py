import cv2
import string
import os


def enc(key, msg, img):
    # print(1)
    # print(img)
    d={}
    c={}
    for i in range(255):
        d[chr(i)]=i
        c[i]=chr(i)
    #print(c)
    x=cv2.imread(img)
    # print(x)
    # print("mannu lallu")
    

    msg = msg + " "*(200-len(msg))
    
    kl=0
    tln=len(msg)
    z=0 #decides plane
    n=0 #number of row
    m=0 #number of column



    for i in range(200):
        x[n,m,z]=d[msg[i]]^d[key[kl]]
        n=n+1
        m=m+1
        m=(m+1)%3 #this is for every value of z , remainder will be between 0,1,2 . i.e G,R,B plane will be set automatically.
                    #whatever be the value of z , z=(z+1)%3 will always between 0,1,2 . The same concept is used for random number in dice and card games.
        kl=(kl+1)%len(key)
        
    img = img.split("/")
    img[-1] = img[-1].split(".")[0]
    

    cv2.imwrite("/".join(img) + "_enc.png", x)
    return


def dec(key, img):
    d={}
    c={}
    for i in range(255):
        d[chr(i)]=i
        c[i]=chr(i)
    x=cv2.imread(img)

    kl=0
    z=0 #decides plane
    n=0 #number of rowimg/
    m=0 #number of column
    
    decrypt=""
    for i in range(200):
        decrypt+=c[x[n,m,z]^d[key[kl]]]
        n=n+1
        m=m+1
        m=(m+1)%3
        kl = (kl + 1) % len(key)
    # print("nikhilllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll", decrypt.strip())
    return decrypt.strip()





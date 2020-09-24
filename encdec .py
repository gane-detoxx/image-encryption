"""
Program for simple encryption and decryption of an image
authors:
gane-detoxx
jnth-glitch
"""

import time
from PIL import Image

def fn(i,abs_height,abs_width,pix):
    n=abs_width//2
    temp=1
    for k in range(i,abs_height-1):
        if k>=(i+abs_height)//2:
            temp=0
        for j in range(n):
                if temp:
                    pix[k,j],pix[k+(abs_height-i)//2+(abs_height-i)%2,j+n+abs_width%2]=pix[k+(abs_height-i)//2+(abs_height-i)%2,j+n+abs_width%2],pix[k,j]
                else:
                    pix[k,j],pix[k-(abs_height-i)//2+(abs_height-i)%2,j+n+abs_width%2]=pix[k-(abs_height-i)//2+(abs_height-i)%2,j+n+abs_width%2],pix[k,j]   

s="""
NOTE:
In order to access the image. File path of the image must be specified properly.
"""
print(s)
path=input("Enter the path of the image:").strip()
path=r'{}'.format(path)
key=125 
start_time=time.time()
img = Image.open(path)
img.save("original.png")
pix=img.load()
abs_height,abs_width=img.size       # height and width of the image
height,width=(abs_height//key)*key,(abs_width//key)*key 
temp=0
#Encryption
print("Encryption on process...\n")
for i in range(height):
    if i%(abs_height//key)==0:
        temp= 0 if temp else 1
    if i+abs_height//key>=height:
        fn(i,abs_height,width,pix)
        break
    for j in range(width//2):
        if temp:
            pix[i,j],pix[i+height//key,j+width//2+width%2]=pix[i+height//key,j+width//2+width%2],pix[i,j]
        else:
            pix[i,j],pix[i-height//key,j+width//2+width%2]=pix[i-height//key,j+width//2+width%2],pix[i,j]
            
temp=0
img.save("encrypt.png")
enc_time=time.time()
print("Encryption Successful.")
print("Encryption time:",enc_time-start_time)
#Decryption
print("\n\nDecryption on process...\n")
for i in range(height):
    if i%(abs_height//key)==0:
        temp= 0 if temp else 1
    if i+abs_height//key>=height:
        fn(i,abs_height,width,pix)
        break
    for j in range(width//2):
        if temp:
            pix[i,j],pix[i+height//key,j+width//2+width%2]=pix[i+height//key,j+width//2+width%2],pix[i,j]
        else:
            pix[i,j],pix[i-height//key,j+width//2+width%2]=pix[i-height//key,j+width//2+width%2],pix[i,j]


img.save("decrypt.png")
end_time=time.time()
print("Decryption Successful.")
print("Decryption time:",end_time-enc_time)
print("\n\n")
img.close()

print("Encryption and Decryption done in",end_time-start_time,"seconds")

import socket
import numpy as np
import PIL
from PIL import Image

# server settings
HOST = 'rgbmatrix'
PORT = 9737
length = 100;
height = 100;
maxsize = (length, height)

# connect socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
send = sock.send

# prepare image (open, convert to rgba, resize, convert to array)
img = Image.open('foo.png')
img = img.convert('RGBA')
img.thumbnail(maxsize, PIL.Image.ANTIALIAS)
arr = np.array(img)

# set a single pixel
def setPixel(x,y,r,g,b,a=255):
  if a == 255:
    send('PX %d %d %02x%02x%02x\n' % (x,y,r,g,b))
  else:
    send('PX %d %d %02x%02x%02x%02x\n' % (x,y,r,g,b,a))

# print a rectangle from x, y to x+w, y+h
def rect(x,y,w,h,r,g,b):
 for i in xrange(x,x+w):
   for j in xrange(y,y+h):
     setPixel(i,j,r,g,b)

# print image array
def image():
    for i in xrange(0, img.size[0]):
        for j in xrange(0, img.size[1]):
            setPixel(i, j, arr[j][i][0], arr[j][i][1], arr[j][i][2], 255)

# do wahtever
def loop():
    while 1:
        # rect(0, 0, 100, 100, 255, 0, 0)
        image()

if __name__ == '__main__':
    loop()

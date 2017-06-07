import socket
import numpy as np
import PIL
from PIL import Image

HOST = 'rgbmatrix'
PORT = 9737

length = 100;
height = 100;

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
send = sock.send

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

def loop():
    while 1:
        image()

def image():
    maxsize = (length, height)
    img = Image.open('foo.png')
    img.thumbnail(maxsize, PIL.Image.ANTIALIAS)
    arr = np.array(img)

    for i in xrange(0, length):
        for j in xrange(0, height):
            setPixel(i, j, arr[i][j][0], arr[i][j][1], arr[i][j][2], 255)


if __name__ == '__main__':
    loop()

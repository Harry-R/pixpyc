import socket

HOST = 'rgbmatrix'
PORT = 9737

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

def imageLoop():
    while 1:
        rect(0, 0, 500, 500, 0, 255, 0)

if __name__ == '__main__':
    imageLoop()

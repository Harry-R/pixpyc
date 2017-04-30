import socket

HOST = 'pixelflut-server'
PORT = 4242

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
send = sock.send

# set a single pixel
def setPixel(x,y,r,g,b,a=255):
  if a == 255:
    send('PX %d %d %02x%02x%02x\n' % (x,y,r,g,b))
  else:
    send('PX %d %d %02x%02x%02x%02x\n' % (x,y,r,g,b,a))


if __name__ == '__main__':
    setPixel(42, 42, 0, 255, 0)

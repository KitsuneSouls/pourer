from tkinter
import *
from os import *
import RPi. GPIO as GPIO
import time
from bluetooth import *

sock = BluetoothSocket( RFCOMM )
sock.bind(("",PORT_ANY))
sock.listen(1)
port = server_sock.getsockname()[1]
uuid = "pourer"
advertise_service( server_sock, "pourer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                    )

client, clientinfo = server_sock.accept()
print "Connection established"

while True:          
    try:
        req = client.recv(1024)
        
        if req == 'drinkOne'
            drinkOne()
            client.send('complete')
        elif req == 'drinkTwo'
            drinkTwo()
            client.send('complete')
        elif req == 'drinkThree'
            drinkThree()
            client.send('complete')
        elif req == 'close'
            client.close()
            server.close()
        else:
            client.send('bad request')

    except IOError:
        pass

GPIO .setmode( GPIO . BCM )
# BCM to use the "labels" rather than physical numbers
# init list with pin numbers to be used throughout project
pinList = [ 5 , 6 , 13 ]
# BCM 5 = 29, BCM 6 = 31, BCM 13 = 33
GPIO .setup(pinList, GPIO . OUT , initial = GPIO . LOW )
# sets pinList pins to "output" mode, and initial to LOW

def drinkOne ():
  GPIO .output(pinList[ 0 ], 1 )
  time.sleep( 5 )
  GPIO .output(pinList[ 0 ], 0 )
  GPIO .output(pinList[ 1 ], 1 )
  time.sleep( 2 )
  GPIO .output(pinList[ 1 ], 0 )
  GPIO .cleanup()

def drinkTwo ():
  GPIO .output(pinList[ 2 ], 1 )
  time.sleep( 3 )
  GPIO .output(pinList[ 2 ], 0 )
  GPIO .output(pinList[ 1 ], 1 )
  time.sleep( 1 )
  GPIO .output(pinList[ 1 ], 0 )
  GPIO .cleanup()

def drinkThree ():
  GPIO .output(pinList[ 0 ], 1 )
  GPIO .output(pinList[ 2 ], 1 )
  time.sleep( 3 )
  GPIO .output(pinList[ 0 ], 0 )
  GPIO .output(pinList[ 2 ], 0 )
  GPIO .output(pinList[ 1 ], 1 )
  time.sleep( 2 )
  GPIO .output(pinList[ 1 ], 0 )
  # GPIO.output(pinList[2], 1)
  # time.sleep(3)
  # GPIO.output(pinList[2], 0)
  GPIO .cleanup()
GPIO .cleanup()
root = Tk()
root.title( "Drink Mixer" )
root.geometry( "300x50" )
app = Frame(root)
app.grid()
button1 = Button(app, text = "Drink 1" , width = 10, command = drinkOne )
.grid( row = 1 , column = 0 , sticky = E)
button2 = Button(app, text = "Drink 2" , width = 10 , command = drinkTwo)
.grid( row = 1 , column = 2 , sticky = E)
button3 = Button(app, text = "Drink 3" , width = 10, command =
drinkThree ) .grid( row = 1 , column = 4 , sticky = E)
root.mainloop()

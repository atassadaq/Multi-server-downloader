import socket
import sys
from threading import *

# next create a socket object 
i = sys.argv[1] #status interval
n = sys.argv[2] #No-of servers
f = sys.argv[3] #file_location
p = sys.argv[4] #port num list



def main():
    global p,i
    s = socket.socket()		 
    print ("Socket successfully created")
    port = p
    s.bind((a, p))
    #ping all servers, whichever responds is chosen to bind		 
    print ("socket binded to %s" %(p) )
    # put the socket into listening mode 
    s.listen(5)	 
    print ("socket is listening") 
    # a forever loop until we interrupt it or 
    # an error occurs 
    serving1 = Timer(i,report) #send report after i seconds
    serving1.start()
    s.close() #close connection


def report():
    # send report here
    print("Hey")
import socket
from _thread import *
import sys

# next create a socket object 




def main():
    r = sys.argv[1] #resume
    i = float(sys.argv[2]) #interval_time_seconds
    o = sys.argv[3] #out_put directory
    a = sys.argv[4] #server IP
    p = int(sys.argv[5]) #port_list

    s = socket.socket()		 
    print ("Socket successfully created")
    port = p
    s.connect((a, p))
    #ping all servers, whichever responds is chosen to bind		 
    print ("Conn established to %s" %(p) )
    s.sendall(b'Hey bro')
    data = s.recv(1024)
    # put the socket into listening mode 
    print ("data recieved", repr(data)) 
    # a forever loop until we interrupt it or 
    # an error occurs 

main()
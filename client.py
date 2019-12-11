import socket
from _thread import *
import sys

# next create a socket object 

if __name__ == "__main__":
    main()


def main():
    r = sys.argv[1] #resume
    i = sys.argv[2] #interval_time_seconds
    o = sys.argv[3] #out_put directory
    a = sys.argv[4] #server IP
    p = sys.argv[5] #port_list

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

    s.close() #close connection
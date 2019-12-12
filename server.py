import socket
import sys
from threading import *

# next create a socket object 
i = float(sys.argv[1]) #status interval
n = int(sys.argv[2]) #No-of servers
f = sys.argv[3] #file_location
p = int(sys.argv[4]) #port num list



def main():
    global p,i
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 
    print ("Socket successfully created")
    port = p
    s.bind(('192.168.100.11', p))
    #ping all servers, whichever responds is chosen to bind		 
    print ("socket binded to %s" %(p) )
    # put the socket into listening mode 
    s.listen(5)	 
    print ("socket is listening") 
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print("data from client:" , repr(data))
            if not data:
                break
            conn.sendall(data)
    # a forever loop until we interrupt it or 
    # an error occurs 
    # serving1 = Timer(i,report) #send report after i seconds
    # serving1.start()
    # s.close() #close connection


def report():
    # send report here
    print("Hey")

main()
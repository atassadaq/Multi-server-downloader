import socket
import sys
from threading import Timer

# next create a socket object 
i = float(sys.argv[1]) #status interval


def main():
    report()
    

def report():
    # send report here
    global i
    print("Hey")
    Timer(i,report).start() #send report after i seconds
    
main()
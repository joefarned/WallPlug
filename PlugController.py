import socket, sys, getopt
import time

class PlugController:

    # Define plug port and IP
    UDP_IP = '10.0.1.15'
    UDP_PORT = 10000

    def sendMessage(self, message):
        # Establish connection
        sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP
        subscription_key = '6864001e636caccf2383ae1820202020202018ae8323cfac202020202020';
        sock.sendto(subscription_key.decode('hex'), (self.UDP_IP, self.UDP_PORT))

        time.sleep(5)

        # Send the message
        sock.sendto(message.decode('hex'), (self.UDP_IP, self.UDP_PORT))

    def turnOn(self):
        self.sendMessage('686400176463accf2383ae182020202020200000000001')

    def turnOff(self):
        self.sendMessage('686400176463accf2383ae182020202020200000000000')

    # Assign destination IP and port
    def __init__(self, ip, port):
        self.UDP_IP = ip;
        self.UDP_PORT = port;

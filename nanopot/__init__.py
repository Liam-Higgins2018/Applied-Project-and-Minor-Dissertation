import logging
import threading
from socket import socket
#Might want to change this later
BIND_IP = '0.0.0.0'

class HoneyPot(object):
    #35 min
    #Setting up the logic for the honeypot
    def __init__(self, ports, log_filepath):
        self.ports = ports
        self.log_filepath = log_filepath
        self.listeners = []
        if len(ports) < 1:
            raise Exception("No ports provided.")

        # set up logging to file - see previous section for more details
        self.logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%Y-%m-%d %H:%M',
                            filename=self.log_filepath,
                            filemode='w')
        #add the handler to the root logger
        self.logger = logging.getLogger(__name__)
        self.logger.info("HoneyPot initializing...")
        #for port in ports:
         #   print("Going to listen on %s" % port)

        def start_listening(self):
            for port in self.ports:
                #Create a new listener
                #store in self.listener[port] = new listener
                pass
            pass


        server = socket.socket{} #Defaults (socket.AF_INET, SOCK_STREAM)
        server.bind((BIND_IP, port))
        server.listener(5)

        def handle_connection(client_socket, ip, remote_port):
            data = client_socket.recv(64)
            logger.info("Connection form %s: %d - %s" % (ip, remote_port, data))
            #Client
            print("[*] Recieved %s" % request)
            client_socket.send("Acknowledged.\n")
            client_socket.close()

        while True:
            client, addr = server.accept()
            print("{*}Accepted connection form %s: %d" % (addr[0], addr[1]))
            client_handler = threading.Thread(target = handle_client,args = client,)
            client_handler.start()
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
        self.listeners = {}
        if len(ports) < 1:
            raise Exception("No ports provided.")

        # set up logging to file - see previous section for more details
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%Y-%m-%d %H:%M',
                            filename=self.log_filepath,
                            filemode='w')
        #add the handler to the root logger
        self.logger = logging.getLogger(__name__)
        self.logger.info("HoneyPot initializing...")
        #for port in ports:
         #   print("Going to listen on %s" % port)

    def handle_connection(self, client_socket, ip, remote_port):
        data = client_socket.recv(64)
        self.logger.info("Connection form %s: %d - %s" % (ip, remote_port, data))
        #Client
        #print("[*] Recieved %s" % request)
        #client_socket.send("Acknowledged.\n")
        client_socket.send("Access Denied.\n")
        client_socket.close()

    def start_new_listener_thread(self, port):
            # Create a new listener
            listener = socket() # Defaults (socket.AF_INET, SOCK_STREAM)
            listener.bind((BIND_IP, int(port)))
            listener.listen(5)

            #Whenever a client is gotten, a new thread is started
            while True:
                client, addr = listener.accept()
                # print("{*}Accepted connection form %s: %d" % (addr[0], addr[1]))
                client_handler = threading.Thread(target=handle_connection, args=(client, port, addr[0], addr[1]))
                client_handler.start()
            # Store in self.listeners[port]= new listener
            pass

    def start_listening(self):
        for port in self.ports:
            self.listeners[port] = threading.Thread(target=self.start_new_listener_thread, args=(port,))
            #Starts new listener thread on the port
            #start_new_listener_thread(port)
            self.listeners[port].start()

    def run(self):
        self.start_listening()
        while True:
            pass


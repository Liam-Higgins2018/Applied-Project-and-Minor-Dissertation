import logging

class HoneyPot(object):
    #35 min
    #Setting up the logic for the honeypot
    def __init__(self, ports, log_filepath):
        if len(ports) < 1:
            raise Exception("No ports provided.")

        # set up logging to file - see previous section for more details
        self.logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%Y-%m-%d %H:%M',
                            filename=log_filepath,
                            filemode='w')
        #add the handler to the root logger
        self.logger = logging.getLogger(__name__)
        self.logger.info("Test")
        #for port in ports:
         #   print("Going to listen on %s" % port)
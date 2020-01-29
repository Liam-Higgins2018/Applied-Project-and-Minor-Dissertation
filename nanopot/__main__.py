""""
HoneyPot

Simple TCP honeypot logger

Usage:
    nanopot --config FILE
Options:
    --config FILE    Path to config options .ini file
    -h --help    show this screen:
"""""

##from docopt import docopt
#args = docopt(__doc__)
#logger.info("Config file %s", args['[config_filepath]'])

#TODO replace with docopt args
import configparser
#config_filepath = '/etc/nanopot.ini'
import logging
import sys
from nanopot import HoneyPot
#Logger that
logger = logging.getLogger('__name__')

config_filepath = 'nanopot.ini'

#ports, log file path
config = configparser.ConfigParser()
config.read(config_filepath)

ports = config.get('default', 'ports', raw=True, fallback='22,80,443,8080,8888,9999,3306')
log_filepath = config.get('default', 'logfile', raw=True, fallback='/var/log/nanopot.log')

#Prints out .ini ports and logfile location
logger.info("[*] Ports: %s" % ports)
logger.info("[*] LogFile: %s" % log_filepath)

ports_list = []
try:
    listOfPorts = ports.split(',')
except Exception as e:
    logger.error('[-] Error parsing ports: %s. \nExiting.', ports)
    sys.exit(1)
#Import the honeypot package from itself
honeypot = HoneyPot(listOfPorts, log_filepath)
honeypot.run()
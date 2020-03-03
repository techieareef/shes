"""
Utilities Having:
1. Logging
"""
import traceback
import logging
import os
import sys
import time
import json
from logging import handlers
import glob


# +++++++++++++++++Log Error tracking++++++++++++++++++++++++
def log_except():
    '''When you enable the console errors the activate the bellow code'''

    # colors = {'pink': '\033[95m', 'blue': '\033[94m', 'green': '\033[92m', 'yellow': '\033[93m', 'red': '\033[91m','ENDC': '\033[0m'}
    # styles_define={'bold': '\033[1m', 'underline': '\033[4m'}
    #
    # def str_color(color,styles, data):
    #     return colors[color] +styles_define[styles]+ str(data) + colors['ENDC']
    #
    # exc_type, exc_value, exc_traceback = sys.exc_info()
    # lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    # logging.error(str_color("blue","underline","******************** Error Started ********************"))
    # logging.error(str_color("red",'bold',''.join( line for line in lines)))
    # logging.error(str_color("blue","underline","******************** Error Ended **********************"))

#     if dont want to print the logfile errors in console activate below code.
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    logging.error("******************** Error Started ********************")
    logging.error(''.join( line for line in lines))
    logging.error("******************** Error Ended **********************")

# +++++++++++++++++Log Initializing and creating directory+++++++++++++++++++++++++++

# ++++++++++++++++++++This function will be used to just log the log file entries +++++++
def write_log_file():



    log = logging.getLogger('')

    # Add file handler
    loglist = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL)
    with open('Const/config.json') as i:
        json_const = json.load(i)
    default_log = json_const['APP_LOG_LEVEL']
    loglevel = loglist[default_log]

    log.setLevel(loglevel)
    format = logging.Formatter('%(asctime)s  %(levelname)-2s [%(filename)s:%(lineno)d]  %(message)s',
                               datefmt='%d-%b-%Y  %H:%M:%S')

    # # console enable the message
    #
    # ch = logging.StreamHandler(sys.stdout)
    # ch.setFormatter(format)
    # log.addHandler(ch)
    #
    fh = handlers.RotatingFileHandler('Log/' + "Applog_" + str(time.strftime('%d-%b-%Y')) + '.log')
    fh.setFormatter(format)
    log.addHandler(fh)

# +++++++++++++++++++Log File limitation based on config file+++++++++++++++++++


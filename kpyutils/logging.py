
import logging
from logging import addLevelName
import logging.handlers
import os
import sys
import inspect
import traceback
import re





VERBOSE = 15
TRACE = 5



# LOGFILE_PATH = '/var/lib/zmirror/log.st'

def prepare_logger(identifier):


  # Configure the root logger
  logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)7s: %(message)s',
    handlers=[
        # logging.FileHandler(logfile_path + datetime.now().strftime("%d-%m-%Y_%H:%M:%S.%f") ),  # File handler
        logging.StreamHandler(sys.stdout)   # Stream handler for stdout
    ]
  )

  logger = logging.getLogger(identifier)
  logger = logging.LoggerAdapter(logger, {'SYSLOG_IDENTIFIER': identifier})


  def verbose(msg, *args, **kwargs):
    """
    Delegate a debug call to the underlying logger.
    """
    logger.log(VERBOSE, msg, *args, **kwargs)
  logger.verbose = verbose

  def trace(msg, *args, **kwargs):
    """
    Delegate a debug call to the underlying logger.
    """
    logger.log(TRACE, msg, *args, **kwargs)
  logger.trace = trace





  return logger

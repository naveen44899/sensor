from sensor.logger import logging
from sensor.exception import SensorException
import os
import sys

def test_exception():
    try:
        logging.info("error has poccured")
        1/0
    except Exception as e:
        raise SensorException(e,sys)
    
if __name__=='__main__':
    try:
        test_exception()
    except Exception as e:
        print(e)


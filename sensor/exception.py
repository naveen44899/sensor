import sys
from  sensor.logger import logging

class SensorException(Exception):
    def __init__(self,error_message,error_detail:sys):
        self.error_message = error_message
        _,_,exc_tb = error_detail.exc_info()
        self.filename = exc_tb.tb_frame.f_code.co_filename
        self.lineno = exc_tb.tb_lineno

    
    def __str__(self):
        return(
            f"error occured in the python file name[{self.filename}]"
            f"at the line number [{self.lineno}]"
            f"the error was [{self.error_message}]"
        )
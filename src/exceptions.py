import sys
from src.logger import logging
# we are doing this for proper debuuging 
# we will give a clear eroor so we can debug by default it is complex eror message and not detailed

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error)
     )
    return error_message
    

# i will inherit by default cutom class and chnge message according to me 
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message =  error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
#When you raise an exception and try to print it, Python automatically calls __str__() to determine what message should be displayed.
# __str__() controls what gets printed when the exception is raised.
#  Without __str__(), Python would just print an object reference like <CustomException object at 0x...>.


# if any eroor occured n any files any i have called exception in try and except block
# than it prints
#Error occurred in script [data_ingestion.py] at line [12]: FileNotFoundError: Test file not found


# if __name__ == "__main__":

#     try:
#         a = 1/0

#     except Exception as e:

#        logging.info("Divide by zero error")
#        raise CustomException(e,sys)

from logging import Logger
import sys
from networksecurity.logging import logger


class NetworksecurityException(Exception):
    def __init__(self, message: str, error_detail:sys) -> None:
        self.error_message = message
        _,_,self.traceback = error_detail.exc_info()

        self.lineno = self.traceback.tb_lineno
        self.filename = self.traceback.tb_frame.f_code.co_filename


    def __str__(self):
        return "Error in {0} line number {1} error message {2}".format(self.filename, self.lineno, self.error_message)



if __name__ == "__main__":
    try:
        logger.logging.info("This is a test log")
        a = 1/0
    except Exception as e:
        raise NetworksecurityException("This is a test exception", sys)

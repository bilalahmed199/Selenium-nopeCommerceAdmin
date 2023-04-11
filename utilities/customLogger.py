#this class is used to save logs

import logging

class LogGenerator:

    #static methods are used so that we dont need to pass any parameter
    @staticmethod
    def log_generator():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                        format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


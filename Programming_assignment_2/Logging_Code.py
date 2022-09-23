import logging

"""This module is to log details, it contains main code of logging"""

logging.basicConfig(filename='logs.log', level=logging.INFO,
                    format='[%(asctime)s : %(levelname)s : %(module)s] : %(message)s')
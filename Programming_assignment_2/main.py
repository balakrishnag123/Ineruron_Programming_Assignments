import logging

import Logging_Code
from Assignment2 import Assignments_2

if __name__ == '__main__':
    logging.info("entering into main function")
    logging.info("creating object for assingment_2")
    ass2 = Assignments_2()
    logging.info("calling kmtomiles")
    miles = ass2.KmtoMiles(5)
    logging.info("miles values is"+str(miles))
    logging.info("calling celcius to farenheit function")
    frnht = ass2.celciustofahrenheit(34)
    logging.info("farenheit values is" + str(frnht))
    logging.info("entering into display calender function")
    Calender = ass2.displayCalender(2022, 9)
    logging.info("calling quadraticEquation function")
    qdrt = ass2.quadraticExquation(4, 5, 6)
    logging.info("quadratic solution are "+str(qdrt))
    swptn = ass2.swaptwonumbers(4, 7)
    logging.info(swptn)
    logging.info("=============================================")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

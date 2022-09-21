import logging
import calendar
import cmath

import Logging_Code
class Assignments_2:

    def KmtoMiles(self, km):
        logging.info("Entering into KmtoMiles module")
        logging.info("Assigned local variable with miles converter value")
        milesconverter = 0.621371

        if type(km) == str:
            logging.exception("please enter the values which can calculates km to Miles")
        else:
            try:
                return km * milesconverter
                logging.info("succesfully executed kmtomiles")
            except Exception as ex:
                logging.info("!!! Caught an exception")
                logging.exception(ex)

    def celciustofahrenheit(self,temp):
        logging.info("entering into celciustofahrenheit function")
        try:
            return (temp*9/5) + 32
            logging.info("celcius to fahrenheit completed")
        except Exception as ex:
            logging.exception(ex)

    def displayCalender(self,yyyy,mm):
        logging.info("entering into display calender function")
        return calendar.month(yyyy,mm)
        logging.info("entering into display calender function")

    def quadraticExquation(self,a,b,c):
        logging.info("enterting into quadratic equation function")
        try:
            logging.info("calculating d values")
            d = (b**2) - 4*a*c
            logging.info("finding values of x")
            sol1 = (-b-cmath.sqrt(d))/(2*a)
            sol2 = (-b + cmath.sqrt(d)) / (2 * a)
            return sol1,sol2
            logging.info("finding values of x and exiting quadratic equation function")
        except Exception as ex:
            logging.exception(ex)

    def swaptwonumbers(self,a,b):
        return b,a





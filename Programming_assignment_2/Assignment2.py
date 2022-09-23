import logging
import calendar
import cmath

import Logging_Code
class Assignments_2:
    ''' This class has assignment related functions'''

    def KmtoMiles(self, km):
        '''This functions takes input as kilometer and returns miles if the input is in number'''
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
        '''This functions takes temprature in kilometer, and convert to forenheit and returns'''
        logging.info("entering into celciustofahrenheit function")
        try:
            return (temp*9/5) + 32
            logging.info("celcius to fahrenheit completed")
        except Exception as ex:
            logging.exception(ex)

    def displayCalender(self,yyyy,mm):
        ''' This functions takes year and month as input and returns calender of that montha and year'''
        logging.info("entering into display calender function")
        return calendar.month(yyyy,mm)
        logging.info("entering into display calender function")

    def quadraticExquation(self,a,b,c):
        """ This functions returs variables of expression by takeing contant values"""
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
        """ This functions takes two input values and returns swaping them without using temporary variable"""
        return b,a





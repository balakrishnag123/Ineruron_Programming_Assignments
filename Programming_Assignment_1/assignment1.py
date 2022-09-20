import logging
import random


class assignment1solution:
    def __init__(self, a, b):
        logging.info("intialised objects")
        self.a = a
        self.b = b

    def hellopython(self):
        logging.info("entering hellopython function")
        print("Hello Python")
        logging.info("exiting hellopython function")

    def Addition(self,a,b):
        if type(a) != int or type(b) != int or type(a) != float or type(b) != float :
            pass
        else:
            logging.exception("make sure you enter both the elements as interger or float")
            logging.info('entering addition function with operands')
        try:
            return a+b
            logging.info("exiting Addition function withh successfully")
        except Exception as ex:
            logging.info("excepiton caught")
            logging.exception(ex)



    def divistion(self,a,b):
        if type(a) != int or type(b) != int or type(a) != float or type(b) != float :
            pass
        else:
            logging.exception("make sure you enter both the elements as interger or float")
        try:
            logging.info("entering division function")
            return a/b
            logging.info("exiting divitions function")
        except Exception as ex:
            logging.info("entered exception")
            logging.exception(ex)


    def areaoftraingle(self,a,b):
        if type(a) != int or type(b) != int or type(a) != float or type(b) != float :
            pass
        else:
            logging.exception("make sure you enter both the elements as interger or float")

        logging.info("entering area of triangle where a is hieght and b is base")
        return 0.5*a*b
        logging.info("exiting area of triangle function")

    def swap(self,a,b):
        logging.info("entering swapping function")
        return b,a
        logging.info("swapping function finised")

    def randongeneration(self):
        logging.info("Entering random number generation function")
        return random.random()
        logging.info("exiting random numner generation")



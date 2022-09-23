
from Logging_Code import logging

class operations :
    """This class contains the Programming assignments 3 solutions"""
    def __init__(self, number):
        """This is constructor for Operations class"""
        logging.info("The obejcts creation started")
        self.number = number
        logging.info("objects are created successfully")
        logging.info("--------------------------------------------------------------------------------")

    def checkNumber(self):
        "This checks if the entered number is positve,negitive and zero"
        logging.info("entered into checknumber function")
        try:
            if self.number == 0:
                return 'zero'
            elif self.number > 0:
                return "Positive"
            else:
                return 'Negative'

        except Exception as ex:
            logging.exception(ex)
        logging.info("checknumber functions completed")
        logging.info("--------------------------------------------------------------------------------")

    def OddorEven(self):
        "This checks if the entered number is even or odd"
        logging.info("oddoreven fucntion entered")
        try:
            if self.number % 2 == 0:
                return "even"
            else:
                return "odd"
            logging.info("oddoreven functions exited")
        except Exception as ex:
            logging.exception(ex)
        logging.info("--------------------------------------------------------------------------------")

    def leapyear(self):
        "This checks if the entered number is leapyear or not"
        logging.info("entering into leapyear functions")
        try:
            if self.number < 100 :
                if self.number % 4 == 0:
                    return "leap year"
                else :
                    return "not a leap year"
            else:
                if self.number % 100 == 0 and self.number % 400 == 0:
                    return "Leap year"
                else:
                    return "Non leap year"
        except Exception as ex:
            logging.exception(ex)
        logging.info("exiting leapyear functions")
        logging.info("--------------------------------------------------------------------------------")

    def primeNumber(self):
        "This checks if the entered number is Primenumber or not"
        logging.info("Entering  primenumber functions")
        try:
            sum = 0
            for i in range(1,self.number):
                if self.number / i == 0:
                    sum = sum + 1
                if sum == 2:
                    return "Prime Number"
                else:
                    return "Not Prime"
        except Exception as ex:
            logging.exception(ex)
        logging.info("exiting primenumber functions")
        logging.info("--------------------------------------------------------------------------------")


    def allprimetill10000(self):
        logging.info("eebtering allprimenumber till 100000 function")
        "This functions prints all even numbers till 10000"
        try:
            lst = []
            for i in range(1,10000):
                if i%2 == 0:
                    lst.append(i)
            return lst
            logging.info("exiting allprimetill10000 functions")
        except Exception as ex:
            logging.exception(ex)
        logging.info("--------------------------------------------------------------------------------")





import Logging_Code
from Logging_Code import logging
from NumberOperations import operations

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logging.info("entering into Main function ")
    try:
        logging.info("creating object")
        ass3 = operations(int(input("Enter a integer number")))
        logging.info("calling checknumber object")
        checkNumber = ass3.checkNumber()
        logging.info(checkNumber)
        logging.info("calling primeNumber object")
        primeNumber = ass3.primeNumber()
        logging.info(primeNumber)
        logging.info("calling leapyear object")
        leapyear = ass3.leapyear()
        logging.info(leapyear)
        logging.info("calling OddorEven object")
        OddorEven = ass3.OddorEven()
        logging.info(OddorEven)
        logging.info("calling allprimetill10000 object")
        allprimetill10000 = ass3.allprimetill10000()
        logging.info("exiting main method")
        logging.info(allprimetill10000)
    except Exception as ex:
        logging.info("entering into main exception")
        logging.exception(ex)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

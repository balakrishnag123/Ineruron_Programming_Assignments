import logging
import Logging_Code

from Assignment_4 import Number_Operations

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logging.info("entered Main functions")
    try:
        logging.info("creating object for number operation function")
        ass4 = Number_Operations(9)
        logging.info("calling factorialofNumber function")
        fac = ass4.factorialofNumber()
        logging.info("the result is ")
        logging.info(fac)
        logging.info("calling multiplication_table function")
        table = ass4.multiplication_table()
        logging.info("the result is ")
        logging.info(table)
        logging.info("calling fabanicciSeries function")
        fabseries = ass4.fabanicciSeries()
        logging.info("the result is ")
        logging.info(fabseries)
        logging.info("calling Armstrongornot function")
        armstr = ass4.Armstrongornot(531)
        logging.info("the result is ")
        logging.info(armstr)
        logging.info("calling rangeArmstrong function")
        rangearmstr = ass4.rangeArmstrong(2000)
        logging.info("the result is ")
        logging.info(rangearmstr)
        logging.info("calling sumnofNaturalNumbers function")
        sumofnat = ass4.sumnofNaturalNumbers()
        logging.info("the result is ")
        logging.info(sumofnat)
        logging.info("Exiting Main function")
        logging.info("---------------------------------------------------------------------------------")
    except Exception as ex:
        logging.exception(ex)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

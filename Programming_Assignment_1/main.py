# This is a sample Python script.
import logging

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Logs import Logging
from assignment1 import assignment1solution
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Logging.logging.info("Main Method Execution started")
    logging.info("acquiring a value")
    try:
        a = int(input(" enter a Value "))
        logging.info("acquiring b value")
        b = int(input("enter b Value "))
        logging.info("intiating object")
    except Exception as ex:
        logging.exception(ex)
    else:
        assign_1 = assignment1solution(a,b)
        logging.info("calling hellopython function")
        assign_1.hellopython()
        logging.info("calling addition function")
        add = assign_1.Addition(a,b)
        logging.info("the result of addtion is : " + str(add))
        logging.info("calling divistion function")
        div = assign_1.divistion(a,b)
        logging.info("the result of division is : " + str(div))
        logging.info("calling area of traingle function")
        area = assign_1.areaoftraingle(a,b)
        logging.info("area of traingle is :" + str(area))
        logging.info("calling swap of two variables function")
        swap = assign_1.swap(a,b)
        logging.info("the result of swap is : " + str(swap))
        logging.info("calling generation of random number function")
        randomnumber = assign_1.randongeneration()
        logging.info("the random number generated is " + str(randomnumber))
    finally:
        logging.info("Main method exited")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

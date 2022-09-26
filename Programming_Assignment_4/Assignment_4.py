import logging

class Number_Operations:
    def __init__(self,number):
        'This initialte the variable numner, requires one parameter'
        logging.info("Initializing variable values")
        self.number = number

    def factorialofNumber(self):
        'this function returns factorial value of input provided numner'
        logging.info("entered into factorialofNumber function")
        fact = 1
        try:
            for i in range(1,self.number + 1):
                fact = fact*i
            logging.info("exiting factorialofNumber")
            return fact
        except Exception as ex:
            logging.exception(ex)

    def multiplication_table(self):
        'this function returns the multiplication table of provided input number'
        logging.info("entered into multiplication_table function")
        table = ""
        try:
            for i in range(1,11):
                table = table + str(self.number) +' * '+str(i)+" = "+str(i*self.number)+"\n"
            logging.info("exiting multiplication_table")
            return table
        except Exception as ex:
            logging.exception(ex)

    def fabanicciSeries(self):
        'this fucntion returns fabanicci series of provided input number'
        logging.info("entered into fabanicciSeries function")
        i = 0
        j = 1
        temp = 0
        fab = [0]
        try:
            for k in range(self.number):
                fab.append(j)
                temp = j + i
                i = j
                j = temp
            logging.info("exiting fabanicciSeries")
            return fab
        except Exception as ex:
            logging.exception(ex)

    def Armstrongornot(self,armnumber):
        'this functions reutrns the result if provided number is armstrong or not'
        input = str(armnumber)
        total = len(input)
        cal = 0
        try:
            for i in input:
                cal = cal + int(i)**total
            if cal == int(input) and total > 2:
                return "argmstrong"
            else:
                return "not armstrong"
            logging.info("exiting Armstrongornot")
        except Exception as ex:
            logging.exception(ex)

    def rangeArmstrong(self,rangenumner):
        'this functions returns range or number which are armstrong between one to limit provided'
        lst = []
        try:
            for i in range(1,rangenumner):
                if self.Armstrongornot(i) == 'argmstrong':
                    lst.append(i)
            return lst
        except Exception as ex:
            logging.exception(ex)
        logging.info("exiting rangeArmstrong")



    def sumnofNaturalNumbers(self):
        'this fucntions provide sum of all naturnal numbers'
        logging.info("entered into sumnofNaturalNumbers function")
        sum = 0
        try:
            for i in range(self.number):
                sum = sum + i
            return sum
            logging.info("exiting sumnofNaturalNumbers")
        except Exception as ex:
            logging.exception(ex)



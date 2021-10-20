####################> Helps to get all array elements in str format <####################
# требуется:
# - из терминала скопировать полученный кортеж
# - добавить нули в начало чисел с 1 до 9, пример('01', '02')
# - добавить кавычки в начале и конце массива
# - переместить полученный кортеж в переменную массива, пример(route = [])

import re
from main import driver
from timing import timer_s
from file_writer import writer
from filter import recipient_of_numbers

def path():
    '''receives from the site a list of numbers and main activities 'without subgroups' in a single line. 
       Writes the received data to the file 'path.txt.
       Returns a value by calling a function from 'filter.py', which processes the received data 
       and filters only numbers of the type ' '01', '02', ..., '99' '. 
       Needed for compiling list navigation when executing 'find_road.py' '''
    driver.get('https://URL')
    # get site for analysis

    timer_s() # loding timer
    # content download timer

    elements = driver.find_elements_by_xpath('//ul[@class="clokved__main clokved__full"]')
    # gets the main elements of a list without expanding subgroups

    timer_s() # loding timer

    writer(elements, 'path')    
    # writes to the file 'path.txt'    

    return recipient_of_numbers('path')
    # returns the received value by processing it in another function 'filter.py'

    #!!!The browser does not close the session at this stage, as an error will occur when executing 'find_road.py'!!!
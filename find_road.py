import os, json
os.system('cls' if os.name == 'nt' else 'clear')

from main import driver
from timing import timer_s
from string_route_for_find_road import path

####################> Getting a list of names and codes <####################
def road_finder(route):
    '''The function opens the tabs of the list and gets all the main and nested elements.'''

    for x in range(0, len(route)):
        '''this part opens all tabs of lists,
        if the given HTML element contains the text fragment necessary for the search and has the status visible to the user in the browser''' 

        if driver.find_element_by_xpath(f'//div/*[contains(text(), "{route[x]} − ")]').is_displayed():
            timer_s() # loding timer
            driver.find_element_by_xpath(f'//div/*[contains(text(), "{route[x]} − ")]').click()
            
            plus = driver.find_elements_by_xpath('//div/*[@class="clokved__switch clokved__plus"]')
            # An array variable (counter) stores the elements in order to understand how many 
            # iterations to perform functions by the number of elements.

            for x in range(0, len(plus)):
                # this part opens all tabs of lists if has the status visible

                if driver.find_element_by_xpath('//*[@class="clokved__switch clokved__plus"]').is_displayed():
                    driver.find_element_by_xpath('//*[@class="clokved__switch clokved__plus"]').click()
                    plus = 0

    timer_s() # loding timer

    ele = driver.find_elements_by_xpath('//*[@class="clokved__level clokved__level-second"]')
    # stores a variable list of all content from open HTML elements

    
    for x in range(0, len(ele)):
        # saving the received data from the variable 'ele' to a file

        with open('work.txt', 'a', encoding='utf-8') as filehandle:
            filehandle.writelines(f"{ele[x].text}\n")


    driver.quit()

    # The argument 'route' receives from 'string_route_for_find_road.py',
    # which passes the text file 'path.txt' in turn to 'filter.py' - the function 'def recipient_of_numbers (text_file)', 
    # which returns ['01', '02 ', ...] - 'route'.
#############################################################################                   
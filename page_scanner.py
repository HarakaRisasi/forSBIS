import random
from main import driver
from timing import timer_s
from timing import timer_b
from map_road import path
from file_writer import writer_single
from fun_wait import wiki


####################> Page Scanner  <####################
def tp():
    """The scanner checks the status and collects the number of operating companies"""
    count_corp = destroy_counter = count = count_path = 0 
    # counters for:
    #   count_corp - counter of companies
    #   destroy_counter - counter of destroyed companies
    #   count - checker counter
    
    for num in range(1919, len(path)): 
        # use to activate the random redirection generator

        rand = random.randint(10, 15) # element of random redirection generator
    
        for x in range(num, len(path)):
            timer_s() # loding timer

            #-------------------------- prevent the occurrence of recaptcha
            # the random redirection generator helps bypass recapcha lock algorithms
            count_path += 1
            if  count_path == rand:
                count_path = 0
                print(f"Please wait: 30 - 52 sec")
                wiki()                 
                  

            for y in range(1, 9999):
                # the number of pages that are involved in the scan
                timer_s() # loding timer

                driver.get(f'https://www.SCRAPER.ru/codes/{path[x]}/{y}/')
                # get path from array 'map_road'

                #-------------------------- company count module 
                timer_s() # loding timer
                corp = driver.find_elements_by_xpath("//*[@class='company-item']")
                # saves to the array the number of elements found on the page and marked with a specific anchor

                count_corp += len(corp)
                # since the scan will go through a series of pages, the total number of items received is stored in this array

                #-------------------------- 404 module
                count_404 = driver.title 
                # get title

                if count_404 == "404":
                    timer_s() # loding timer
                    break  
                count_404 = 0
                # Stop scanning if a 404 error is detected

                #-------------------------- warning-text module 
                if driver.find_elements_by_xpath("//*[@class='warning-text']"):
                    # red elements(stop status) search

                    count = driver.find_elements_by_xpath("//*[@class='warning-text']")
                    # Counter of red elements(stop status) detected on the page

                    destroy_counter += len(count)
                    # counter of red elements(stop status) that are detected after scanning the entire cycle

                    timer_s() # loding timer
                    if len(count) > 1:
                        # if the counter of red elements(stop status) on the current page exceeds the limit, then the cycle can be stopped
                        break

                    count = 0
                    # reset counter after page scan
            corp = 0
            # reset counter after scanning

            #-------------------------- recording module if recaptcha is not detected
            result = str(count_corp - destroy_counter)

            recapcha = driver.find_elements_by_xpath("//*[@class='g-recaptcha']")
            # recaptcha detection

            if recapcha:
                driver.quit()
            else:    
                writer_single(path[x] + " " + result, 'result')
            # writing to a file


            count_corp = destroy_counter = recapcha = 0
            # reset counter after scanning

        driver.quit() # close browser
        break
#########################################################
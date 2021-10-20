import os, main
# очистка терминала(больше сделано для красоты)
os.system('cls' if os.name == 'nt' else 'clear')

from page_scanner import tp
from timing import timer_s
from main import driver
from find_road import road_finder
from string_route_for_find_road import path

####################> Get address <####################
#driver.get("https://www.SCRAPER.ru/codes/")
#print(driver.title) # get title

#timer_s() # loding timer

#find_elements.search()
#road_finder(path())
# The function works in the following sequence:
# start <= find_road <= string_route_for_find_road => file_writer(path.txt) => filter => string_route_for_find_road  => find_road ==> give (work.txt)

# > 'start.py' call function 'road_finder ()'.
# > Passes the argument 'path ()' to it.
# > 'path ()' - formed in 'string_route_for_find_road.py'.
# > 'string_route_for_find_road.py' gets the desired list and calls 
#    the function 'writer (elements, 'path')' from 'file_writer.py' and writes the received data to the file 'path.txt'.
# > After that, it passes 'path.txt' as an argument to the function 'function recipient_of_numbers ()' from 'filter.py'.
# > Function 'function recipient_of_numbers ('path')' processes the received file and returns
#   the value of 'route' via the function 'return recipient_of_numbers (' path ')' in 'string_route_for_find_road.py'.
# > Now 'road_finder.py' receives the argument 'route', performs processing of all the tabs on the site, 
#   then receives a detailed list of all the elements and saves the received information to the created file 'work.txt'.

tp() # function from turn_pages
# The function works in the following sequence:
# start <= page_scanner <= map_road => page_scanner ==> give (result.txt)


timer_s() # loding timer

driver.quit() # close browser
#######################################################

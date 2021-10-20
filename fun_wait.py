from main import driver
from timing import timer_b
from timing import timer_s

def wiki():
    '''Opens the site in the browser and clicks on the button'''
    driver.get('https://ru.wikipedia.org/')
    timer_s()
    driver.find_element_by_id("n-randompage").click()
    timer_b()


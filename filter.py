import os, re
from pathlib import Path

os.system('cls' if os.name == 'nt' else 'clear')

####################> Filters <####################
def recipient_of_numbers(text_file):
    '''remove newline in text and get only numbers ['01', '02', ...]'''
    clean = open(f'{text_file}.txt', encoding='utf-8').read().replace('\n', '')
    route = re.findall(r"\d{2}", clean)
    return route

def recipient_of_main_path_numbers(text_file):
    '''finds in the text and returns a sequence of the form '11.11.11 -' consisting of one two or three pairs of numbers'''
    clean = open(f'{text_file}.txt', encoding='utf-8').read()
    route = re.findall(r"\d*.\d*.\d* −", clean)
    return route
    
def character_padding(str_el_array):
    '''in a text array, deletes the characters '-', '.', 
       measures the length of each element and adds characters, making the elements the same length, 6 characters'''
    for x in range(0, len(str_el_array)):
        full = str_el_array[x].replace(' −', '').replace('.', '')
        while len(full) < 6:
            full += "0"
        str_el_array.remove(str_el_array[x])
        str_el_array.insert(x, full)        
    return str_el_array
    # return data, values of the type '['011100', '011110', '011111', ...]'
###################################################

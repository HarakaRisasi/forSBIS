####################> Write element to the file  <####################
def writer(note, filename): 
    '''writes to the file all the data of all cells in the array'''   
    for x in range(0, len(note)):
        with open(f'../scrap/{filename}.txt', 'a', encoding='utf-8') as filehandle:
            filehandle.writelines(f"{note[x].text}\n")

def writer_single(note, filename):
    '''writes the value of one variable to a file'''
    with open(f'../scrap/{filename}.txt', 'a', encoding='utf-8') as filehandle:
        filehandle.writelines(f"{note}\n")
######################################################################
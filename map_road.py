from filter import character_padding
from filter import recipient_of_main_path_numbers

path = character_padding(recipient_of_main_path_numbers('./scrap/work'))
# The variable receives a value of the type '['011100', '011110', '011111', ...]'
print(path)
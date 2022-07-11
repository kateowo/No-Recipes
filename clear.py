# clear all vanilla recipes

# import
import os
# custom colours in terminal
from colorama import init
from colorama import Fore, Back, Style
init()

warning = input(f'{Back.RED}{Style.BRIGHT}[WARNING]{Style.RESET_ALL} Proceeding will overwrite {Back.RED}{Style.BRIGHT}ALL{Style.RESET_ALL} files in this and corresponding directories. Are you sure? [y/n] ')
if warning == 'y':
    for filename in os.scandir():
        if filename.is_file() and filename.path != '.\clear.py':
            print (filename.path)
            with open(filename.path,'w') as file:
                file.write('''{
    "type": "minecraft:crafting_shaped",
    "key": {
        "#": {
            "item": "minecraft:air"
        }
    },
    "pattern": [
        "#"
    ],
    "result": {
        "item": "minecraft:barrier"
    }
}''')

    print (f'{Back.GREEN}{Style.BRIGHT}[DONE]{Style.RESET_ALL}')
else:
    print (f'{Back.GREEN}{Style.BRIGHT}[ABORTED]{Style.RESET_ALL}')
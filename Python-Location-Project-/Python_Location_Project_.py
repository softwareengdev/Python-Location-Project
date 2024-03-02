# import tkinter as tk
# from tkinter import filedialog

# root = tk.Tk()
# root.withdraw()

# file_path = filedialog.askopenfilename()

# from keyboard import keyboard, on_press, on_press_key
# from pynput.keyboard import Key, Listener

from main_read_file import Read_file_case_
import asyncio

async def Start_program():
    
    print(' ')
    print(' ')
    print('############################################################################################################################################################')
    print('#######################################################################. HELLO TO THIS PYTHON APP .#########################################################')
    print('############################################################################################################################################################')
    print(' ')
    print(' ')    

async def End_program():
    
    print(' ')
    print(' ')
    print('############################################################################################################################################################')
    print('#######################################################################. END FROM FROM THIS PYTHON APP .####################################################')
    print('############################################################################################################################################################')
    print(' ')
    print(' ')
    
# START PRORGAM 
asyncio.run(Start_program())

# CASE 1
asyncio.run(Read_file_case_.Main_case_1())

# END PROGRAM 
asyncio.run(End_program())

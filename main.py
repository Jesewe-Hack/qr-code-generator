import time
import colorama
import ctypes
import os
import pyqrcode
import png
from pyqrcode import QRCode
from colorama import init, Fore
init()
ctypes.windll.kernel32.SetConsoleTitleW('QR Code Generator | By Jesewe Hack')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

banner="""
                    .▄▄▄  ▄▄▄       ▄▄·       ·▄▄▄▄  ▄▄▄ .     ▄▄ • ▄▄▄ . ▐ ▄ ▄▄▄ .▄▄▄   ▄▄▄· ▄▄▄▄▄      ▄▄▄  
                    ▐▀•▀█ ▀▄ █·    ▐█ ▌▪▪     ██▪ ██ ▀▄.▀·    ▐█ ▀ ▪▀▄.▀·•█▌▐█▀▄.▀·▀▄ █·▐█ ▀█ •██  ▪     ▀▄ █·
                    █▌·.█▌▐▀▀▄     ██ ▄▄ ▄█▀▄ ▐█· ▐█▌▐▀▀▪▄    ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌▐▀▀▪▄▐▀▀▄ ▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄ 
                    ▐█▪▄█·▐█•█▌    ▐███▌▐█▌.▐▌██. ██ ▐█▄▄▌    ▐█▄▪▐█▐█▄▄▌██▐█▌▐█▄▄▌▐█•█▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
                    ·▀▀█. .▀  ▀    ·▀▀▀  ▀█▄▀▪▀▀▀▀▀•  ▀▀▀     ·▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀ .▀  ▀ ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀
"""

while True:
    os.system("cls")
    print(bcolors.OKGREEN + banner)
    print(bcolors.OKBLUE + """
                                [ Made by Jesewe Hack : https://github.com/Jesewe-Hack ]
    """ + bcolors.ENDC)
    try:
        link = input(bcolors.OKCYAN + '                                  Please enter link or text: ')
        url = pyqrcode.create(link)
        url.png('qrcode.png', scale=8)
    except Exception as e:
        os.system('cls')
        print(bcolors.FAIL + '\n                                    [!] Error: Failed to create QR Code')
        input(bcolors.OKGREEN + "\n                                    Press Enter to exit the menu... ")
    else:
        print(bcolors.OKGREEN + '\n                                    [+] QR Code successfully created!')
        print(bcolors.OKGREEN + '\n                                    [+] QR Code saved as qrcode.png')
        input(bcolors.OKGREEN + "\n                                    Press Enter to exit the menu... ")

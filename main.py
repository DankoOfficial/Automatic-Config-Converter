import os
import time
from datetime import datetime
from colorama import *
init()

Info = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
converted = 0

choice = input("[1] SVB => LOLI\n[2] LOLI => SVB")
if choice == "1":
    print(Fore.LIGHTWHITE_EX)
    os.system('cls')
    base = os.path.dirname(__file__)
    for file in os.listdir(base):
        if ".py" in file:
            pass
        elif '.loli' in file:
            pass
        else:
            ya = (file.replace('.svb',''))
            os.rename(file, f"{ya}.loli")
            converted +=1
            print(f"[{Info}] {Fore.LIGHTWHITE_EX}[LOGS] [{Fore.LIGHTBLUE_EX}SVB {Fore.LIGHTWHITE_EX}-> {Fore.LIGHTMAGENTA_EX}LOLI] {Fore.LIGHTBLUE_EX}{file} {Fore.LIGHTWHITE_EX}-> {Fore.LIGHTMAGENTA_EX}{ya}.loli")
    print(f"\n\n\n{Fore.LIGHTWHITE_EX}[{Info}] {converted} Configs from Silverbullet to Openbullet [SVB -> LOLI] - Press enter to exist")
    input()
elif choice == "2":
    print(Fore.LIGHTWHITE_EX)
    os.system('cls')
    base = os.path.dirname(__file__)
    for file in os.listdir(base):
        if ".py" in file:
            pass
        elif '.svb' in file:
            pass
        else:
            ya = (file.replace('.loli',''))
            os.rename(file, f"{ya}.svb")
            converted +=1
            print(f"[{Info}] {Fore.LIGHTWHITE_EX}[LOGS] [{Fore.LIGHTBLUE_EX}LOLI {Fore.LIGHTWHITE_EX}-> {Fore.LIGHTMAGENTA_EX}SVB] {Fore.LIGHTBLUE_EX}{file} {Fore.LIGHTWHITE_EX}-> {Fore.LIGHTMAGENTA_EX}{ya}.svb")
    print(f"\n\n\n{Fore.LIGHTWHITE_EX}[{Info}] {converted} Configs from Silverbullet to Openbullet [SVB -> LOLI] - Press enter to exist")
    input()

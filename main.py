# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(AG_legend)s
"""

# ---- Auto Install Required Modules ----
# ---- Auto Install Required Modules ----
import importlib
import subprocess
import sys

def check_and_import(modules: dict):
    loaded = {}
    for pkg_name, pkg_install in modules.items():
        try:
            loaded[pkg_name] = importlib.import_module(pkg_name)
        except ImportError:
            print(f"⚠️  {pkg_name} پیدا نشد → نصب {pkg_install} ...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_install])
            importlib.invalidate_caches()
            loaded[pkg_name] = importlib.import_module(pkg_name)
            print(f"✅  {pkg_name} نصب شد.")
    return loaded

# لیست ماژول‌های مورد نیاز
modules_needed = {
    "pystyle": "pystyle==2.9",
    "colorama": "colorama==0.4.6",
    "requests": "requests==2.31.0",
    "user_agent": "user_agent==0.1.10",
    # Plugins اگر پکیج PyPI نباشه، اینجا خطا میده
    # "Plugins": "Plugins"
}

libs = check_and_import(modules_needed)

# حالا می‌تونی مستقیم استفاده کنی:
pystyle = libs["pystyle"]
colorama = libs["colorama"]
requests = libs["requests"]
user_agent = libs["user_agent"]

# ---- End Auto Install ----

# import requests as req
from os import path, system


if path.exists("./requirements.txt"):
    with open("./requirements.txt") as file:
        libs = [i.split("==")[0] for i in file.readlines()]
    
    for lib in libs:
        print(lib)
        try:
            __import__(lib)
        except ModuleNotFoundError:
            system("pip install "+lib)


from pystyle import Col, Center, System
from Plugins.api_list import handler
from colorama import Fore
from Plugins.functions import Functions

r, g = Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX

if __name__ == "__main__":
    logo = f''' {Fore.CYAN}
        ___   ______     __                          __
       /   | / ____/    / /__  ____ ____  ____  ____/ /
      / /| |/ / __     / / _ \/ __ `/ _ \/ __ \/ __  / 
     / ___ / /_/ /    / /  __/ /_/ /  __/ / / / /_/ /  
    /_/  |_\____/____/_/\___/\__, /\___/_/ /_/\__,_/   
               /_____/      /____/                     {Fore.RED}
                               __                    __             
       _________ ___  _____   / /_  ____  ____ ___  / /_  ___  _____
      / ___/ __ `__ \/ ___/  / __ \/ __ \/ __ `__ \/ __ \/ _ \/ ___/
     (__  ) / / / / (__  )  / /_/ / /_/ / / / / / / /_/ /  __/ /    
    /____/_/ /_/ /_/____/  /_.___/\____/_/ /_/ /_/_.___/\___/_/     
                                                                    
    {Col.yellow}(by Arash)
    '''




    while True:
        System.Clear()
        print(Center.XCenter(logo))

        try:
            proxy_state = Fore.GREEN + "Enabled" if Functions.proxy_state() else Fore.RED + "Disabled"
            choices = {
                "1": "call",
                "2": "sms"
            }
            print(f"{Col.yellow}[!]{Col.gray} Proxies are {proxy_state}")
            print(f"{Col.yellow}[!]{Fore.CYAN} Choices: ")

            for ch in choices:
                print(f"   {Fore.CYAN}{ch}- {Fore.GREEN}{choices[ch].capitalize()} Bomber ")
            
            print()
            choice = Functions.get_input(f"{Fore.CYAN}[=]{Col.gray} Enter Your Choice: {Col.green}", lambda x: x in [str(i) for i in choices])
            number = Functions.get_input(f"{Fore.CYAN}[=]{Col.gray} Enter the phone number {Fore.CYAN}[9xxxxxxxxx]{Col.gray}: {Col.green}", checker=lambda x: x != "" and x.isnumeric() and x.startswith("9") and len(x) == 10)
            count = Functions.get_input(f"{Fore.CYAN}[=]{Col.gray} Enter spam count: {Col.green}", lambda x: x.isnumeric() and int(x) >= 0)

            Functions.start(choices[choice], number, int(count))


        except KeyboardInterrupt:
            print("\n" + Fore.BLUE, "Exiting...")
            exit()
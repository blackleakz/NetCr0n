import os
import sys
import subprocess
import time
import socket
import pyfiglet
import colorama
import datetime
import argparse
from datetime import datetime
from colorama import Fore, Back, Style, init
from socket import *
from queue import Queue
from threading import Thread, Lock


def init_menu():
    distance_from_top = 20
    while True:
        print("\n " * distance_from_top)
        print(Fore.RED + "          __--==={ }===--__   ")
        print(Fore.RED + "          __--==/|N|\==--__   ")
        print(Fore.RED + "          __--==| € |==--__   ")
        print(Fore.RED + "          __--==| 1 |==--__   ")
        print(Fore.RED + "          __--==| C |==--__   ")
        print(Fore.RED + "          __--==| R |==--__   ")
        print(Fore.RED + "          __--==| 0 |==--__   ")
        print(Fore.RED + "          __--==| N |==--__   ")
        print(Fore.RED + "          __--=/|||||\=--__   ")
        time.sleep(0.1)
        os.system('CLS')
        distance_from_top -= 1
        if distance_from_top < 0:
            distance_from_top = 20
            menu()
            return False


def menu():
    print("\n")
    time.sleep(2)
    print(Fore.GREEN + "\n")
    os.system("CLS")
    res = pyfiglet.figlet_format("NETCR0N")
    print(res)
    print("\n")
    print(Fore.RED + "||__--=====================================--__||")
    print(Fore.RED + "||__--==NETCR0N    | Version: 1          ==--__||")
    print(Fore.RED + "||__--=====================================--__||")
    print(Fore.RED + "||__--== 1: netstat       || 2: arp      ==--__||")
    print(Fore.RED + "||__--== 3: ping          || 4: portscan ==--__||")
    print(Fore.RED + "||__--== 5: portscan2     || 6: crawler  ==--__||")
    print(Fore.RED + "||__--== 7: hostname      || 8: tracert  ==--__||")
    print(Fore.RED + "||__--== 9: ipconfig      || n: nslookup ==--__||")
    print(Fore.RED + "||__--== i: pathping      || 8: tracert  ==--__||")
    print(Fore.RED + "||__--== d: full_docs     || h: help     ==--__||")
    print(Fore.RED + "||__--== x: fast portscan || s: sysinfo  ==--__||")
    print(Fore.RED + "||__--=====================================--__||")


    print("\n")

    choice = input("Your choice: ")

    if choice == "1":
        netstat()
    if choice == "2":
        arp()
    if choice == "3":
        ping()
    if choice == "4":
        portscan()
    if choice == "5":
        portscan2()
    if choice == "6":
        crawl()
    if choice == "7":
        hostname()
    if choice == "8":
        tracert()
    if choice == "9":
        ipconfig()
    if choice == "n":
        nslookup()
    if choice == "i":
        pathping()
    if choice == "h":
        helpx()
    if choice == "d":
        docs()
    if choice == "x":
        portscan_fast()
    if choice == "s":
        sysnfo()


def sysnfo():
    os.system("CLS")
    print("Collecting systeminfo... .. .")
    os.system("start cmd /k systeminfo")
    menu()

def portscan_fast():
    os.system("CLS")
    print("Starting fast portscan... .. . ")
    l = input("Enter target-ip:~$ ")

    os.system("start cmd /k python3 portscan_fast.py " + l)
    menu()

def docs():
    os.system("CLS")
    print(Fore.GREEN + "\n")
    print("Go to 'https://blackzspace.cf/docs' for full docs")
    menu()

def helpx():
    os.system("CLS")
    print(Fore.GREEN + "\n")
    print("Comming soon... .. .")
    menu()

def pathping():
    os.system("CLS")
    print(Fore.GREEN + "\n")
    print("\n")
    print("Starting pathping... .. .")
    os.system("pathping /?")
    pathpingx = input("Enter target & parameters :~$ ")
    os.system("start cmd /k pathping " + pathpingx)
    menu()

def nslookup():
    os.system("CLS")
    print(Fore.GREEN + "\n")
    print("\n")
    print("Starting nslookup... .. .")
    os.system("nslookup /?")
    dns = input("Enter target:~$ ")
    os.system("start cmd /k nslookup " + dns)
    menu()

def ipconfig():
    os.system("CLS")
    print(Fore.GREEN + "\n")
    print("\n")
    print("Get ipconfig... .. .")
    os.system("ipconfig /?")
    inp = input("Enter parameter: ")
    os.system("start cmd /k ipconfig " + inp)
    menu()

def hostname():
    os.system("CLS")
    print(Fore.GREEN + "\n")
    print("\n")
    print("Your hostname: ")
    os.system("hostname")
    menu()

def netstat():
    os.system("CLS")
    print(Fore.GREEN + "\n")
    print("\n")
    print("Starting netstat-scan... .. .")
    os.system("netstat /?")
    inpn = input("Enter netstat- parameters:~$ ")
    os.system('start cmd /k netstat '+ inpn)
    menu()

def arp():
    os.system("CLS")
    print(Fore.GREEN + "\n")
    print("\n")
    print("Starting arp-scan... .. .")
    os.system("arp /?")
    inps = input("Enter parameters:~$ ")
    os.system("start cmd /k arp ")
    menu()

def ping():
    os.system("CLS")
    print(Fore.GREEN + "\n")
    print("\n")
    print("Starting ping-test... .. .")
    os.system("ping /?")
    ip = input("Enter target parameters:~$ ")
    os.system("start cmd /k ping " + ip)
    menu()

def tracert():
    os.system("CLS")
    print(Fore.GREEN + "\n")
    print("\n")
    print("Starting trace... .. .")
    print("You can add following params::")
    os.system("tracert /?")
    target = input("Enter target-ip:~$ ")
    os.system("start cmd /k tracert " + target)
    menu()

def portscan():
    os.system("CLS")
    print(Fore.GREEN + "\n")
    print("\n")
    print("Starting portscan... .. .")
    import socket
    from colorama import init, Fore

    init()
    GREEN = Fore.GREEN
    RESET = Fore.RESET
    GRAY = Fore.LIGHTBLACK_EX

    def is_port_open(host, port):
        """
        determine whether `host` has the `port` open
        """
        s = socket.socket()
        try:
            s.connect((host, port))
            s.settimeout(0.2)
        except:
            return False
        else:
            return True
    host = input("Enter the host:~$ ")
    for port in range(1, 1025):
        if is_port_open(host, port):
            print(f"{GREEN}[+] {host}:{port} is open      {RESET}")
        else:
            print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")

    menu()





def main():
    init_menu()





if __name__ == '__main__':


    main()

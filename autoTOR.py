# -*- coding: utf-8 -*-
import time
import os
import subprocess

try:
    import requests
except ImportError:
    print('[+] python3-requests is not installed. Installing now...')
    os.system('pip3 install requests requests[socks]')
    import requests

def ensure_tor_installed():
    try:
        subprocess.check_output('which tor', shell=True)
    except subprocess.CalledProcessError:
        print('[+] Tor is not installed. Installing...')
        subprocess.call('sudo apt update', shell=True)
        subprocess.call('sudo apt install tor -y', shell=True)
        print('[!] Tor installed successfully.')

def start_tor():
    try:
        subprocess.call('service tor start', shell=True)
    except:
        try:
            subprocess.call('systemctl start tor', shell=True)
        except Exception as e:
            print(f'[!] Could not start Tor service: {e}')

def reload_tor():
    try:
        subprocess.call('service tor reload', shell=True)
    except:
        try:
            subprocess.call('systemctl reload tor', shell=True)
        except Exception as e:
            print(f'[!] Could not reload Tor service: {e}')

def ma_ip():
    url = 'http://checkip.amazonaws.com'
    try:
        get_ip = requests.get(url, proxies=dict(
            http='socks5://127.0.0.1:9050',
            https='socks5://127.0.0.1:9050'
        ), timeout=10)
        return get_ip.text.strip()
    except Exception as e:
        return f'[!] Failed to get IP: {e}'

def change():
    reload_tor()
    print('[+] Your IP has been changed to:', ma_ip())

def main():
    ensure_tor_installed()
    os.system("clear")
    
    print('''\033[1;32;40m
                _          _______
     /\\        | |        |__   __|
    /  \\  _   _| |_ ___      | | ___  _ __
   / /\\ \\| | | | __/ _ \\     | |/ _ \\| '__|
  / ____ \\ |_| | || (_) |    | | (_) | |
 /_/    \\_\\__,_|\\__\\___/     |_|\\___/|_|
                V 2.1
from mrFD
''')
    print("\033[1;40;31m http://facebook.com/ninja.hackerz.kurdish/\n")
    
    start_tor()
    time.sleep(3)
    print("\033[1;32;40m Set your SOCKS to 127.0.0.1:9050 \n")
    
    x = input("[+] Time delay to change IP in seconds [default=60] >> ") or "60"
    lin = input("[+] How many times to change IP? (Enter 0 or leave blank for infinite) >> ") or "0"

    try:
        delay = int(x)
        lin = int(lin)

        if lin == 0:
            print("[*] Starting infinite IP change. Press Ctrl+C to stop.")
            while True:
                time.sleep(delay)
                change()
        else:
            for _ in range(lin):
                time.sleep(delay)
                change()

    except ValueError:
        print("[!] Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()

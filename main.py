from sys import platform
from shutil import copyfile
import os


class FirefoxTreeTweaker:
    def __init__(self):
        self.src = 'userChrome.css'
        self.windows_path = f'{os.path.expanduser("~")}/AppData/Roaming/Mozilla/Firefox/Profiles'
        self.mac_path = f'{os.path.expanduser("~")}/Library/Application Support/Firefox/Profiles'
        self.linux_path = f'{os.path.expanduser("~")}/.mozilla/firefox'

    def execute(self):
        if platform == "linux" or platform == "linux2":
            profile = os.listdir(self.linux_path)[0]
            copyfile(self.src, f'{self.linux_path}/{profile}/{self.src}')
        elif platform == "darwin":
            profile = os.listdir(self.mac_path)[0]
            copyfile(self.src, f'{self.mac_path}/{profile}/{self.src}')
        elif platform == "win32":
            profile = os.listdir(self.windows_path)[0]
            copyfile(self.src, f'{self.windows_path}/{profile}/{self.src}')


run = FirefoxTreeTweaker()

run.execute()
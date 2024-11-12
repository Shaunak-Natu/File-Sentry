from os import listdir, system
from time import sleep

def main():
    desktop_path = "C:\\Users\\[username]\\Desktop"
    items = listdir(path=desktop_path)
    print(items)
    if "iamhere.txt" in items:
        exit()
    else:
        system("shutdown /s /t 0")

n = 10
sleep(n)
main()


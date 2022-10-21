from scraper import *
from manager import *
from adder import *
from colorama import init, Fore

init()

y = Fore.YELLOW

def banner():
    f = pyfiglet.Figlet(font='slant')
    banner = f.renderText('Telegram')
    print(f'{y}{banner}{n}')
    print("\n")


def main(access_what):
    if access_what == 1:
        manager_launch()
    if access_what == 2:
        scraper_launch()
    if access_what == 3:
        main_launch()

if __name__ == "__main__":
    banner()
    access_what = int(input("What do you want to access?\n1: Manager\n2:Scraper\n3:Adder\n"))
    main(access_what)

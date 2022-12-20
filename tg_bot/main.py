from adder import *
from manager import *
from scraper import *

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
        adder_launch()


if __name__ == "__main__":
    while True:
        banner()

        access_what = int(input("What do you want to access?\n[1] Manager\n[2] Scraper\n[3] Adder\n[4] Quit\n"))
        if access_what == 4:
            quit()
        main(access_what)
        clr()

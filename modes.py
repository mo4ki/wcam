from time import sleep
import os
from colorama import init, Fore, Back, Style
import subprocess

init()

sleep(1)
os.system("clear")
sleep(0.7)
print(Fore.CYAN)
print("""							╭╮╭╮╭╮  ╭━━━╮  ╭━━━╮  ╭━╮╭━╮
							┃┃┃┃┃┃╱╱┃╭━╮┃╱╱┃╭━╮┃╱╱┃┃╰╯┃┃
							┃┃┃┃┃┃╱╱┃┃╱╰╯╱╱┃┃╱┃┃╱╱┃╭╮╭╮┃
							┃╰╯╰╯┃╱╱┃┃╱╭╮╱╱┃╰━╯┃╱╱┃┃┃┃┃┃
							╰╮╭╮╭╯╭╮┃╰━╯┃╭╮┃╭━╮┃╭╮┃┃┃┃┃┃
							 ╰╯╰╯ ╰╯╰━━━╯╰╯╰╯ ╰╯╰╯╰╯╰╯╰╯""")

sleep(1)

print(Fore.RESET+"Выберите режим:")

sleep(0.6)

print("")
sleep(0.2)

print("[0] "+Fore.YELLOW+"Установка комлектующих"+Fore.RESET)
sleep(0.2)

print("[1] "+Fore.RED+"Атака"+Fore.RESET+" D")
sleep(0.2)

print("[2] "+Fore.RED+"Атака"+Fore.RESET+" B")
sleep(0.2)

print("[3] "+Fore.RED+"Атака"+Fore.RESET+" A")
sleep(0.2)

print("[4] "+Fore.RED+"Атака"+Fore.RESET+" F")
sleep(0.2)

print("[5] "+Fore.RED+"Атака"+Fore.RESET+" L")
sleep(0.2)

print("[6] "+Fore.YELLOW+"Активный"+Fore.RESET+" режим")
sleep(0.2)

print("[7] "+Fore.GREEN+"Спокойный"+Fore.RESET+" режим")
sleep(0.2)

print("[8] "+Fore.YELLOW+"Захват всех пакетов"+Fore.RESET+" т.д. в округе")
sleep(0.2)

print("[9] "+Fore.YELLOW+"Поиск блютуз девайсов "+Fore.RESET+" в окрестностях")
sleep(0.2)

print("[10]"+Fore.WHITE+Style.DIM+" Выход"+Style.RESET_ALL)
sleep(0.2)

print(Fore.RESET+"[88]"+Fore.GREEN+" инфо. ")

os.system("python3 modes2.py")

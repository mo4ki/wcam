import configs
import os
import psutil
import functions



def main():
	while True:
		os.system('clear')

		print(configs.wcam)
		print('Select action:')

		choice = input('''
[1] attack Deauth
[2] attack BeaconFlood
[3] attack AuthFlood
[4] attack CrazyPacket
[5] attack BluetoothDDOS
[6] Adapter monitoring mode
[7] Adapter default mode
[8] Capturing all AP packets 
[9] Search for bluetooth devices 
[10] info
[88] exit. 
: ''')


		try:
			choice = int(choice)
		except:
			print('It\'s not a number')

		functions.choice_action(choice)

if __name__ == '__main__':

	if os.getuid() != 0:

		print(configs.non_root)
		exit(0)

	os.system('clear')

	print(configs.hello)
	print(configs.version + '\n')

	adapters = list(psutil.net_if_addrs())

	for adapter in adapters:

		adapter_index = adapters.index(adapter)
		print(f'[{adapter_index}] {adapter}')

	choice = input('\nChoice your adapter: ')

	try:
		choice = int(choice)
	except:
		print('It\'s not a number')
		exit()

	configs.adapter_name = adapters[adapter_index]
	configs.adapter_name_mon = adapters[adapter_index] + 'mon'

	main()

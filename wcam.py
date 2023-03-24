import functions
import configs
import subprocess
import os


def main():

	while True:

		print(configs.console_clear) 
		print(configs.wcam)

		print(' Select action:')

		try:

			choice = input(configs.variant)
			choice = int(choice)

			functions.choice_action(choice)

		except ValueError:
			print(' It\'s not a number')

		except KeyboardInterrupt:
			print('')
			functions.choice_action(88)

		except Exception as exc:
			print(f' Error: {exc}')

def choice_adapters_names():

    print(' Choose your adapter:\n')
    adapters_list = os.listdir(os.path.join('/', 'sys', 'class', 'net'))

    for i, adapter in enumerate(adapters_list):
        print(f' [{i}]. {adapter}')

    try:

       	adapter_index = input(' : ')
        adapter_index = int(adapter_index)
        adapter = adapters_list[adapter_index]

    except ValueError:
        print(' Please enter a number')

    except IndexError:
        print(' Invalid index')
    
    if 'mon' in adapter:
    	
    	configs.adapter_name = adapter[:-3]
    	configs.adapter_name_mon = adapter
    
    else:
    	
    	configs.adapter_name = adapter
    	configs.adapter_name_mon = adapter + 'mon' 



if __name__ == '__main__':

	if os.getuid() != 0:

		print(configs.non_root)
		exit(0)

	print(configs.console_clear) 

	print(configs.hello)
	print(configs.version + '\n')

	choice_adapters_names()
	main()

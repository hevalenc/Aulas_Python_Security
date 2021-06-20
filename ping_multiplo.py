import os
import time

print("### PING MÚLTIPLO ###")

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print("\n-> Verificando o IP: ", ip)
        os.system('ping -n 4 {}'.format(ip))
        print("-" * 60)
        time.sleep(5)

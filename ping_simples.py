import os

print("### PING SIMPLES ###")
ip_ou_host = input("\nDigite o IP ou HOST a ser verificado: ")

os.system('ping -n 6 {}'.format(ip_ou_host))

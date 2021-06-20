import ipaddress

ip = '192.168.0.255'

endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network('192.168.0.0/24', strict=False)

print("Endereço: ", endereco)
print("Endereço + 100: ", endereco - 100)
print("Endereço - 100: ", endereco + 100)
print("Rede: ", rede)

print()
for ip in rede:
    print(ip)


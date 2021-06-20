import random
import string

tamanho = 16
rnd = random.SystemRandom()
chars1 = string.ascii_letters + string.digits + '!@#$%&*()-=+!?'
chars2 = string.ascii_lowercase + string.digits + '!@#$%&*()-=+!?'
chars3 = string.ascii_letters + string.digits

print("\nExemplo com letras maiúsculas, minúsculas, números e caracteres especiais:")
print("".join(rnd.choice(chars1) for i in range(tamanho)))

print("\nExemplo com letras minúsculas, números e caracteres especiais:")
print("".join(rnd.choice(chars2) for i in range(tamanho)))

print("\nExemplo com letras maiúsculas, minúsculas e números:")
print("".join(rnd.choice(chars3) for i in range(tamanho)))

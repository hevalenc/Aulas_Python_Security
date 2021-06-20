import itertools

string = input("Digite uma palavra: ")

#resultado = itertools.permutations('abcdef', 5) #o número será o tamanho da palavra
resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))

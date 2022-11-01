import string

alf = list(string.ascii_lowercase)
enc = 1
entrada = input("Encriptar: ")
for x in range(len(entrada)):
    print(entrada[x])
    print(alf.index(entrada[x]))
    if alf.index(entrada[x]) + enc >= len(alf):
        resto = alf.index(entrada[x]) - len(alf) + enc
        entrada[x] = alf[resto]
    else:
        resto = alf.index(entrada[x]) + enc
        entrada[x] = alf[resto]

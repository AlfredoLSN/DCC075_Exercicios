#Primeiro numero primo
p = 10259

#Segundo numero primo
q = 10639

n = p * q


#Semente
s = 513


def geraSequencias(s, n,  qnt):
    x = (s ** 2) % n
    resultado = ""
    for i in range(qnt):
        x = (x ** 2) % n
        lsb = x & 1
        resultado += str(lsb)
    return resultado

print(geraSequencias(s, n, 1024))


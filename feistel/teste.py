teste = 5
teste2 = 255
#print(bin(teste))
#print(bin(resultado))
resultado = teste ^ teste2
print(f"{(teste):08b}")
print(f"{(teste2):08b}")
print(f"{(resultado):08b}")


print(f"{(resultado ^ teste2):08b}")

#PUBLIC
p = 10259
g = 10639



#Alice private 1
a = 573

#Bob private 2
b = 723



A = (g**a) % p
B = (g**b) % p


#Alice Key
keyAlice = (B**a) % p

#Bob Key
keyBob = (A**b) % p

print("Alice Key: ", keyAlice)
print("Bob Key: ", keyAlice)
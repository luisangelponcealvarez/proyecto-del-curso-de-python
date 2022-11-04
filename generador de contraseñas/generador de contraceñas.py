from random import choice 
longitud = 20
valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
p = ""
p = p.join([choice(valores)for i in range(longitud)])
print(p)
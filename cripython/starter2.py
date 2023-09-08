mensaje = 12 # exponente 
e = 65537
p = 17
q = 23
n = (p*q)
respuesta = pow(mensaje, e, n)
print(respuesta)
### Nota aclaratoria - e = A

def cifrar(texto,k):
    s = ""
    for i in (texto):
        if(ord(i) != 32):
            s = s + chr(ord(i)+k)
            
        else:
            s = s + i
    return s



mensaje = input("Ingrese su mensaje a cifrar: \n")
k = int(input("Ingrese un número k (desplazamientos): \n"))
print(cifrar(mensaje,k))

#97 a 122
#65 a 90
def cifrar(texto,k):
    s = ""
    for i in (texto):
        if(ord(i) != 32):
            s = s + chr(ord(i)+k)
            
        else:
            s = s + i
    return s

def alfabeto(n, k):
    if(n-k < 97):
      return(123 - (97-(n-k)))
    else:
      return(n-k)

def alfabeto2(n, k):
    if(n-k < 65):
      return(91 - (65-(n-k)))
    else:
      return(n-k)

def descifrar(texto,k):
    s = ""
    for i in (texto):
        if(ord(i) != 32):
          if(i.islower() == True):
            tt = alfabeto(ord(i),k)
          else:
            tt = alfabeto2(ord(i),k)
          s = s + chr(tt)
            
        else:
            s = s + i
    return s

def menu():
  print("Para cifrar escriba 1 para descifrar escriba 2: \n")
  opcion = int(input())
  if (opcion ==1):
    mensaje = input("Ingrese su mensaje a cifrar: \n")
    k = int(input("Ingrese un número k (desplazamientos): \n"))
    print(cifrar(mensaje,k))
  elif(opcion == 2):
    mensaje = input("Ingrese su mensaje a descifrar: \n")
    for i in range(1, 26):
      print(descifrar(mensaje, i))
  else:
    print("Escoge bien conchetuma'e")

menu()
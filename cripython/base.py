#bytes.fromhex()función se puede usar para convertir hexadecimal a bytes.
#Devuelve la cadena codificada.
#Base64 es el proceso de convertir los datos binarios, en un juego de caracteres limitado a 64 caracteres.
respuesta=bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")
import base64
print(base64.b64encode(respuesta).decode("utf-8"))
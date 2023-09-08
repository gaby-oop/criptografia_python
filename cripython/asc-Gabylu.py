#El código ASCII precisamente nos permite  codificar combinaciones de caracteres y símbolos,El código ASCII en informática se compone de 7 bits para 
# la representación de caracteres y define códigos para 32 caracteres no imprimibles
# y más de 95 caracteres imprimibles.Con octavo bit que se reserva para análisis.
#La función ord() de Python toma el argumento de cadena de un solo carácter Unicode y devuelve su valor de punto de código Unicode entero
# la función chr() toma un argumento entero y lo convierte en carácter


numeros = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

for  numero in numeros:
    print(chr(numero), end=" ")
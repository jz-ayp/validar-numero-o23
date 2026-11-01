# Verifica si la cadena es un número real válido
# Usando idioms de Python

# Declaraciones
DIGITOS = "0123456789"
SIGNOS = "+-"
VALIDOS = DIGITOS + SIGNOS + "."

# Entradas
cadena = input("Introduzca cadena a probar: ")

# Proceso
# Solo caracteres válidos
ok_caracteres = all(c in VALIDOS for c in cadena)
# Máximo un punto decimal
ok_punto = cadena.count(".") <= 1
# Máximo un signo
signos = cadena.count("+") + cadena.count("-")
ok_signos = (
    signos == 0
    or signos == 1 and (cadena[0] in SIGNOS or cadena[-1] in SIGNOS)
)

# Salidas
if ok_caracteres and ok_punto and ok_signos:
    print("Sí es un número válido")
else:
    print("No es un número válido")

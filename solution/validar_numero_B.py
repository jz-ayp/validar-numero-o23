# Verifica si la cadena es un número real válido

# Declaraciones
DIGITOS = "0123456789"
SIGNOS = "+-"
VALIDOS = DIGITOS + SIGNOS + "."

# Entradas
cadena = input("Introduzca cadena a probar: ")

# Proceso
puntos = 0
signos = 0
error = False
for caracter in cadena:
    # Sólo dígitos, puntos o signos + o -
    if caracter in VALIDOS:
        # Sólo un punto
        if caracter == ".":
            puntos += 1
            if puntos > 1:
                error = True
        # Solo un signo
        elif caracter in SIGNOS:
            signos += 1
            if signos > 1:
                error = True
    else:
        # Ningún otro carácter es válido
        error = True
    if error:
        break
if signos == 1:
    # Si se encontró un signo debe estar al principio o al final
    if not (cadena[0] in SIGNOS or cadena[-1] in SIGNOS):
        error = True

# Salidas
if not error:
    print("Sí es un número válido")
else:
    print("No es un número válido")

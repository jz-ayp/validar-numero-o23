# Verifica si la cadena es un número real válido

# Entradas
cadena = input("Introduzca cadena a probar: ")

# Proceso
puntos = 0
signos = 0
error = False
for posicion, caracter in enumerate(cadena):
    # Sólo dígitos, puntos o signos + o -
    if not caracter.isdigit():
        # Sólo un punto
        if caracter == ".":
            puntos += 1
            if puntos > 1:
                error = True
        # Solo un signo
        elif caracter in "+-":
            signos += 1
            if signos > 1:
                error = True
            # Y tiene que ir al principio o al final
            if posicion != 0 and posicion != len(cadena) - 1:
                error = True
        else:
            # Ningún otro carácter es válido
            error = True
    if error:
        break

# Salidas
if not error:
    print("Sí es un número válido")
else:
    print("No es un número válido")

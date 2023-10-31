# Ejercicio examen parcial 2
# Algoritmos y Programación
# Otoño 2023

def validar_numero(cadena):
    "Verifica si la cadena es un número real válido"
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
                    break
            # Solo un signo
            elif caracter in "+-":
                signos += 1
                if signos > 1:
                    error = True
                    break
                # Y tiene que ir al principio o al final
                if posicion != 0 and posicion != len(cadena) - 1:
                    error = True
                    break
            else:
                # Ningún otro carácter es válido
                error = True
    return not error


# Probar función
cadena = input("Introduzca cadena a probar: ")
print(validar_numero(cadena))

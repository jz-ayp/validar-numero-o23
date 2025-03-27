# Estructuras de repetición

## Ejercicio: Validar número real

## Enunciado

**Escribe un programa en Python que verifique si una cadena de texto se trata de un número real válido**, para lo cual debe cumplir con los siguientes requisitos:
    1. No puede contener caracteres diferentes a dígitos, punto, signo más o signo menos.
    2. Si tiene punto decimal, sólo puede ser uno.
    3. Puede tener máximo un signo, positivo (+) o negativo (-), exclusivamente al principio o al final de la cadena.

> ***Nota***: Como ya se mencionó, a las reglas anteriores, faltó añadir una más: que la cadena contenga al menos un dígito. *No debes codificar esta regla en tu solución*". 

## Instrucciones
- Codifica tu solución en el archivo [`validar_numero.py`](validar_numero.py).
   
- Utiliza los siguientes ejemplos para dar formato a tus salidas:
  ```
  Introduzca un número: -123
  El texto introducido sí cumple con los requisitos
  
  Introduzca un número: 123+
  El texto introducido sí cumple con los requisitos

  Introduzca un número: +A12
  El texto introducido no cumple con los requisitos
  ```
  
- Prueba tu programa corriéndolo varias veces con diferentes entradas. Verifica que tu algoritmo produzca las salidas correctas. Identifica y pon atención especial a los casos que pudieran ser problemáticos de manejar (casos límite).

- Añade una cadena de documentación a tu programa.

  
## Entrega
Completa éste y el resto de los ejercicios y compila, para cada uno, el enunciado, análisis, diagrama de flujo, código y pruebas de ejecución, en un informe tal como se describe en los requisitos para entrega de tareas en Canvas. No olvides incluir portada y conclusiones.


## Casos de prueba de ejemplo
| Entradas | Salidas |
|:---------|:--------|
| `-123`   | `True`  |
| `123+`   | `True`  |
| `+A12`   | `False` |

## Rúbrica
Verifica tu entrega contra la rúbrica disponible en Canvas para maximizar tu calificación.

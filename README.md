# Estructuras de decisión

## Ejercicio: Validar número real

## Instrucciones
- Elabora el análisis y el algoritmo ***antes de escribir el código***. 
- Utiliza un diagrama de flujo para representar tu algoritmo e ilustrar su lógica.

- **Escribe una función en Python que verifique si una cadena de texto se trata de un número real válido**, para lo cual debe cumplir con los siguientes requisitos:
    1. No puede contener caracteres diferentes a dígitos, punto, signo más o signo menos.
    2. Si tiene punto decimal, sólo puede ser uno.
    3. Puede tener máximo un signo, positivo (+) o negativo (-), exclusivamente al principio o al final de la cadena.

- Codifica tu solución en el archivo [`validar_numero.py`](validar_numero.py).
   
- El calificador necesitará entradas y salidas para validar la función, así que deberás escribir un programa principal que utilice la función para generar salidas con un formato como el de los siguientes:
  ```
  Introduzca un número: -123
  El texto introducido sí cumple con los requisitos
  
  Introduzca un número: 123+
  El texto introducido sí cumple con los requisitos

  Introduzca un número: +A12
  El texto introducido no cumple con los requisitos
  ```
  
- Prueba tu programa corriéndolo varias veces con diferentes entradas. Verifica que tu algoritmo produzca las salidas correctas. Identifica y pon atención especial a los casos que pudieran ser problemáticos de manejar (casos límite).

- Añade una cadena de documentación (*docstring*) a tu función.

  
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

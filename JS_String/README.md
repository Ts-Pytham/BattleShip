# JS.string
Es un módulo creado por Johan Sánchez en el cuál simula las funciones de la librería estándar de C pero que tiene influencia de Pawn, esta actualmente contiene más de 10 funciones principales, desde strcmp hasta strcpy. Las funciones son:
- Strcmp. 
- Strlen.
- Strcat.
- Strcpy.
... (Próximamente)

<h2> ¿Cómo funciona strcmp? </h2>
Sencillo, esta cuenta con 3 parámetros en el cual los 2 primeros sirven para comparar las dos cadenas y el tercer parámetro que viene verdadero por defecto. Verdadero: Compara las cadenas, no importa si una de las 2 tiene un caracter en mayúscula o en minúscula, retorna 0. Falso: Compara las cadenas sí y solo sí las 2 son exactamente igual, si una de ellas tiene una mayúscula retornará 1.

Ejemplo: 

          if strcmp("Hola", "hola") == 0:  
              print("Son iguales!")
              
Anotación 1: Encontramos que la condición se cumple si la función retorna a 0, por lo tanto la condición se cumple porque las 2 cadenas son iguales sin importar que comience en mayúscula o un caracter tenga una mayúscula o minúscula.

Anotación 2: Tenemos que tener en cuenta que el tercer parámetro está por defecto por lo tanto será verdadero, si le das valor falso al tercer parámetro no entrará a la condición porque encontró que "H" es diferente a "h".

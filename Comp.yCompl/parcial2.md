# Parcial 2

## Metaheurísticas

## ¿Qué es una metaheurística? #card
La metaheurística es un tipo general de método de solución que organiza la interacción entre los procedimientos de mejora local y las estrategias de más alto nivel para crear un proceso que sea capaz de escapar de un óptimo local y realizar una búsqueda vigorosa de una región factible

## ¿Cuáles son las MH más usadas? #card
Tabu search, simulated annealing y genetical algorithm.

## Mencione características del Tabu search #card

* Tiene una lista tabú (tenencia tabú), es decir, tiene **mem. adaptiva**, por lo que evita regresarse.
* El tabu search se basa en la idea de subir una montaña, siempre sube, pero si tiene que bajar (no queda de otra) entonces baja lo menos posible.
* Vecindad dinámica: Solo explora una parte de los vecinos, los que no son tabú.
* Vecindad adaptiva: Mem. corto plazo, mediante el mecanismo de prohibición temporal. Y también tiene memoria a largo plazo mediante frecuencia, intesificación y diversificación.
* Path relinking.
* Criterio de aspiración.
* Oscilación estratégica.

## ¿Qué pasos sigue Tabu search? #card

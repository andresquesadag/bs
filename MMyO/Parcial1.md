# Investigación de Operadores
1. ¿ Qué elementos componen un modelo?
  * Función objetivo (Z)
  * Variables de decisión (x1, x2, ...)
  * Restricciones (x1 > 0, ...)
2. ¿ Qué tipo de modelos existen?
  * Estático y dinámico: Un solo periodo y más de un solo periodo de tiempo.
  * Lineal y No lineal: Con función objetivo lineal o no lineal.
  * Entero y No entero: Variables de decisión enteras o no enteras.
  * Determinístico y estocástico: Es cuando para cualquier valor de las variables de decisión, se conoce con certeza el valor de la función objetivo y si las restricciones se cumplen o no. Suelen ser aproximaciones de modelos
    reales pero dan información muy valiosa..
3. ¿Qué tipos de programación existen? 
  * Lineal.
  * Entera.
  * Red.
  * Dinámica.
  * No Lineal.
4. Mencione los 7 pasos para construir un Modelo.
  **Plantear** el problema-Reunir **información** para estimar el valor de parámetros que afectan el problema-**Elaborar** el modelo-**Revisar** si el modelo se acopla a la realidad-
  **Seleccionar** el modelo adecuado-**Presentar** el modelo-Ponerlo en **marcha** y **evaluarlo**.


# Método Gráfico
![simbologiaPLineal](images/simbologiaGrafPLineal.jpg)

0. Crear una tabla de restricciones con los datos proporcionados por el problema.
  ![tablaEstandar](images/tablaEstandarGrafPlineal.jpg)
1. Identificar los valores de las variables de decisión que son permitidos por las restricciones del problema.
  ![formaEstandar](images/formaEstandarGrafPLineal.jpg)
    * Dibujar la recta de cada restricción usando las intersecciones con 0 cero de ambas variables de decisión. 
2. Dibujar la región factible. Esta región debe de ser un area que cubren todas las restricciones al mismo tiempo.
3. Obtener los puntos de Intersección entre las rectas que estén en la región factible.
4. Probar todos los puntos vértice dentro de la región factible en Z. El **menor** será la solución factible que **minimiza Z**, el **mayor** el que la **maximiza**.

## Casos posibles al realizar Programación Lineal:
### Más de una solución óptima factible o Infinitas soluciones:
Gráficamente se puede ver como un segmento entero que está delimitado por una recta cuyos puntos dan lo mismo en Z.
### No tiene solución factible
1. No tiene soluciones factibles (que entren en la región factible).
2. Va hacia el infinito y por ende mejora de forma constante (falta de restricciones).

* ``Soluciones FEV: Factibles En los Vértices (Esquinas de la región factible) -También se les conoce como esquinas o puntos extremos de la región factible-``

## Supuestos
1. **Proporcionalidad**: La contribución de cada actividad es proporcional (en Z) al nivel de actividad x_j. Por eso a_ij*x_j. Por ende los problemas solo pueden ser lineales.
2. **Aditividad**: C/a función del modelo es la suma de las constribuciones individuales de las actividades respectivas.
3. **Divisibilidad**: Las variables de desición pueden tomar cualquier valor real, siempre y cuando cumplan con las restricciones.
4. **Certidumbre**: Los valores asignados a cada parámetro son conocidos con certeza.

--------------------------------------------------------
# Método Simplex algebraico

# Método Simplex tabular

# Gran M

# Dos fases 
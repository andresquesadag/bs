# Parcial 2 de Bases de Datos

## GROUP BY

## PROCEDURE

## FUNCTION

## SEQUENCE

## INDEX

Son como los índices de los libros, sirven para acceder a datos de una tabla rápidamente.

En Oracle si se hace una consulta sin índices lo que se hace es recorrer todas las tablas comparando las condiciones que se definieron en la consulta. Mientras que si se tienen índices entonces se recorre una estructura de árbol (Como en un libro donde se va al índice y ahí nos indica en qué página está lo que buscamos). **Aceleramos las consultas**

- `Índice compuesto o concatenado`: Se crea en múltiples columnas en una tabla.
- `Basado en funciones o expresiones`: Incluye uso de funciones. Ej:

  ```sql
  CREATE INDEX I_upp_employees_lname
  ON employees (UPPER(last_name));

  /*Al existir "I_upp_employees_lname" en la B.D. Cuando se haga este tipo de consulta
  se usará "por debajo" el índice en lugar de hacer la consulta de forma "normal".
  Optimizando este tipo de consulta*/
  SELECT * FROM employees
  WHERE UPPER(last_name) = 'KING';
  ```

Lo bueno:

- Optimiza el acceso a los datos.
- Perfecto si hay muchos datos.
- Perfecto si se combinan tablas.

Lo malo:

- Consume espacio en el disco.
- Mayor costo de mantenimiento.

### Consultar índices creados

```sql
SELECT index_name, index_type, uniqueness
FROM user_indexes -- general
WHERE table_name= '<nombre_tabla>'; --específico
```

### Crear índice

```sql
CREATE UNIQUE INDEX <nombre_índice> -- datos únicos
ON <nombre_tabla> (<nombre_columna>);

CREATE INDEX <nombre_índice> -- datos repetibles
ON <nombre_tabla> (<nombre_columna>);
```

### Eliminar índice

```sql
DROP INDEX <nombre_índice>;
```

## SYNONYM

Un SYNONYM (sinónimo) es un alias o un nombre alternativo asignado a un objeto de base de datos (como una tabla, vista, secuencia o procedimiento) en Oracle SQL. Este alias permite a los usuarios referirse al objeto de manera más sencilla y, en ocasiones, evita tener que especificar el nombre completo del objeto.

### Consultar sinónimos creados

![alt text](image.png)

```sql
SELECT SYNONYM_NAME, TABLE_OWNER, TABLE_NAME, DB_LINK
FROM USER_SYNONYMS
WHERE SYNONYM_NAME = '<nombre_sinonimo>';
```

### Crear sinónimo

```sql
-- PUBLIC -> ¿disponible para todo usuario de la BD?
CREATE [OR REPLACE] [PUBLIC]
SYNONYM <nombre_sinonimo>
FOR <nombre_objeto>;

```

### Eliminar sinónimo

```sql
DROP [PUBLIC] SYNONYM <nombre_sinonimo>;
```

## VIEW
````

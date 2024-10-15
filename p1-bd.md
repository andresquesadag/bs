# Parcial I Bases de Datos

- Registro o instancia: Fila de una tabla
- Campo o atributo: Columna de una tabla

1. **¿Qué es una base de datos?** Un conjunto estructurado y centralizado de datos en un sistema de computadores.
2. **¿Qué tipos de modelo de bases de datos existen?**

- `Archivo plano:` Son tablas en archivos con un cierto formato que no tienen estructuras de relaciones complejas. Ej: CSV
- `Jerárquico:` Organiza los datos en una estructura de árbol con una jerarquía padre-hijo. Cada nodo padre puede tener múltiples nodos hijos, pero cada hijo tiene solo un padre. Es útil cuando los datos siguen una estructura rígida y clara de jerarquía.Ej: Subcarpetas.
- `De red:` Es una evolución del modelo jerárquico, pero en este caso, los nodos pueden tener múltiples padres y múltiples hijos, permitiendo relaciones más complejas. Está diseñado para reflejar relaciones enredadas entre datos. Ej: Una base de datos que gestiona productos y proveedores, donde un proveedor puede proporcionar varios productos, y un producto puede ser suministrado por varios proveedores.
- `Orientado a objetos:` Combina conceptos de bases de datos con la programación orientada a objetos. Aquí, los datos se almacenan como "objetos", que contienen tanto información (propiedades) como comportamiento (métodos). Esto permite representar estructuras de datos más complejas y mejorar la reutilización del código. Ej: Un sistema de inventario donde los productos se representan como objetos con propiedades como nombre, precio y métodos para calcular descuentos
- `Relacional:` Organiza los datos en tablas (o relaciones) que están formadas por filas (registros) y columnas (atributos). Las tablas pueden estar relacionadas entre sí a través de claves primarias y claves externas, lo que facilita consultas avanzadas. Ej: Una base de datos SQL donde hay una tabla de clientes relacionada con una tabla de pedidos mediante un ID de cliente.

3. **¿Qué es un modelo conceptual?** Es el modelo que incluye las entidades que se convertirán en tablas de una base de datos y sus relaciones con otras entidades
4. **¿Qué es un modelo lógico?** Es el modelo que incluye las entidades con sus atributos (con su obligatoriedad y cardinalidad) y sus relaciones con otras entidades. Se les llama ERM y se suele representar en ERDs.
5. **¿Qué es un modelo físico?** Es el modelo que incluye todo lo de los otros dos pero además especifíca los tipos de dato de todos los campos (incluído sus límites [ej: VARCHAR(10) - String de 10 chars]).
6. **¿Qué tipos de entidades existen?**

- `Principal` -> Independientes
- `Característica` -> Salen de una entidad `principal`
- `Intersección` -> Salen de dos o más entidades

7. **¿Qué es una `instancia` en una entidad?** Es una única incidencia de una entidad.
8. **¿Qué es un `atributo`?** Detalles de un solo valor de una entidad. (Ej: phone_num, age, name, etc.).

- Se caracterizan como obligatorios(\*) u opcionales(o)
- Pueden ser volátiles o no. (Ej: age - v, birth - nv).
- Pueden ser únicos o compuestos. (Ej: id - u, name[1stname + middlename + lastname1 + lastname2] - c).
- Pueden tener uno o más valores. (Ej: lastname1 = Apellido1, pero address = DirecciónPrincipal y DirecciónSecundaria y ...)

9. **¿Qué componentes tiene una relación entre entidades?** Nombre (en minusculas), cardinalidad y opcionalidad.
10. **¿Qué caracteriza a una entidad intersección?**  
    <img src="image-1.png"  width="400"/>
11. **¿Qué es transferabilidad?** Es la capacidad de una entidad de cambiar a lo largo del tiempo entre dos instancias. Si NO es transferible se representa con un `diamante.`
12. **¿Qué es un subtipo?** Existen subtipos y supertipos, un supertipo es una entidad "general" que tiene dos o más "especializaciones" llamadas subtipos. Estos subtipos heredan todas las relaciones y atributos de la entidad supertipo, además de sus claves primarias (PK), también pueden tener sus propio subtipos. La forma de representar entidades subtipo es dentro del supertipo. `Siempre que se tenga una instancia de un supertipo se tiene la de uno de sus subtipos, es decir, una instancia no puede ser de un supertipo sin ser "clasificada" (solo puede ser de un subtipo)`. Ej:  
    <img src="image-2.png"  width="250"/>

13. **Describa los niveles de normalización**

- Nivel 1: Atributos atómicos(indivisibles), que haya único(s) (UID) y las columnas de la tabla no deben ser variantes.
- Nivel 2: Todo atributo depende del UID. Es decir si los campos de una tabla representan a su entidad o si se pueden poner en otra tabla al describir otra entidad.
- Nivel 3:Eliminar o mover a otra entidad a los campos o atributos que no sean dependientes de la UID.

14. **¿Cómo crear una tabla en SQL Oracle?**

```sql
CREATE TABLE [esquema].nombre_tabla(
  atributo datatype(n),
  atributo datatype(n),
  atributo datatype(n)
);
```

para mostrar las CAMPOS, NULLABLE y DATATYPE de la tabla:

```sql
DESCRIBE nombre_tabla;
```

15. **¿Cómo poner CONSTRAINTS en una tabla?**

- A nivel de columna
  ```sql
  CREATE TABLE [esquema].nombre_tabla(
    /*Para especificar not nullable se hace así*/
    -- NOT NULL solo se puede a nivel de columna
    atributo datatype(n) NOT NULL,
    /*Forma general*/
    atributo datatype(n) CONSTRAINT nombre_constraint CONSTRAINT_TYPE,
    /*ej:*/
    id_empleado NUMBER(6 /*dígitos*/) CONSTRAINT emp_empid_pk PRIMARY KEY,
    correo_empleado VARCHAR2(20 /*chars*/) CONSTRAINT emp_email_uk UNIQUE
  );
  ```
- A nivel de tabla
  ```sql
  CREATE TABLE [esquema].nombre_tabla(
    atributo datatype(n),
    atributo datatype(n),
    atributo datatype(n),
    CONSTRAINT nombre_constraint CONSTRAINT_TYPE (atributo_al_que_aplica)
    /*Ej:*/
    id_empleado NUMBER(6),
    CONSTRAINT emp_empid_pk PRIMARY KEY (id_empleado)
  );
  ```

16. **¿Cómo se aplica el CONSTRAINT foreign key?**

```sql
CREATE TABLE [esquema].nombre_tabla(
  /*Col level*/
  atributo datatype(n) CONSTRAINT nombre_constraint FOREIGN KEY REFERENCES nombre_otra_tabla (atributo_otra_tabla),
  /*Table level*/
  atributo datatype(n),
  CONSTRAINT nombre_constraint FOREIGN KEY (atributo_al_que_aplica) REFERENCES nombre_otra_tabla (atributo_otra_tabla)
  /*Después de esa línea de seguido se puede poner la forma de "delete"*/
  ON DELETE CASCADE /*ó*/ ON DELETE SET NULL
);
```

17. **¿Cómo utilizar el CONSTRAINT check?**

```sql
atributo datatype(n) CONSTRAINT nombre_constraint CHECK (condición) --Funciona como assert(x) en C
```

18. **¿Cuáles son algunos comandos para modificar tablas en Oracle SQL?**

- ALTER:

  ```sql
  ALTER TABLE nombre_tabla <modificación>;
  ```

- ADD:
  ```sql
  -- Agregar columna
  ALTER TABLE nombre_tabla ADD col_nueva;
  ```
- MODIFY:
  ```sql
  ALTER TABLE nombre_tabla MODIFY (atributo <valor por defecto, datatype o tamaño>);
  ```
- DROP:
  - Borrar una columna
    ```sql
    ALTER TABLE nombre_tabla DROP (col_descartable);
    ```
  - Borrar una tabla entera
    ```sql
    DROP TABLE nombre_tabla;
    ```
- SET UNUSED: Para marcar campos inutilizados para borrarlos cuando se tenga menos uso de la tabla.
  ```sql
  ALTER TABLE nombre_tabla SET UNUSED (col_descartable);
  -- Alternativamente se puede poner "COLUMN".
  ALTER TABLE nombre_tabla SET UNUSED COLUMN (col_descartable);
  -- También se pueden marcar varias a la vez
  ALTER TABLE nombre_tabla SET UNUSED (col_descartable1, col_descartable2);
  ```
- DROP UNUSED: Eliminaría a todas los campos marcados como inutilizados.
  ```sql
  ALTER TABLE nombre_tabla DROP UNUSED COLUMNS;
  ```
- Se pueden bloquear cambios o permitirlos con:
  ```sql
  -- Prohibir escritura
  ALTER TABLE nombre_tabla READ ONLY;
  -- Permitir escritura
  ALTER TABLE nombre_tabla READ WRITE;
  ```

19. **¿Cómo se haría una copia de una tabla?**

```sql
-- Tomar en cuenta que no se copian las restricciones al hacer esto.
CREATE TABLE copia_de_tabla_existente AS (SELECT * FROM tabla_existente)
```

20. **¿Cómo insertar valores a una tabla?**

```sql
-- Si se ponen en orden, no hace falta decir la columna.
INSERT INTO nombre_tabla VALUES (value_para_col1, value_para_col2, ...);
-- Si no quiere insertar un valor
INSERT INTO nombre_tabla VALUES (value_para_col1, NULL, value_para_col3, ...);
--Si quiero mantener el valor DEFAULT?
INSERT INTO nombre_tabla VALUES (value_para_col1, DEFAULT, value_para_col3, ...);
-- Si se ponen en cualquier orden o algún valor de la fila se dejará en el por defecto.
-- Pónga los valores en orden en que nombra las cols.
-- Si no pone una col. es implícito que no quiere poner un valor
INSERT INTO nombre_tabla (col1, col2, ...) VALUES (value_para_col1, value_para_col2, ...);
```

21. **¿Cómo poner un autoincremental en una columna?**

```sql
CREATE TABLE nombre_tabla(
  -- De uno en uno automático
  col1 NUMBER GENERATED ALWAYS AS IDENTITY,
  -- Si uno quiere personalizarlo
  col2 NUMBER GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
  ...
);
```

22. **¿Cómo editar una fila?**

```sql
-- Ponga ese valor a todas las filas en la col. "col1"
UPDATE nombre_tabla SET col1 = 'value';
-- Ponga ese valor en una fila específica
UPDATE nombre_tabla SET col1 = 'value' WHERE atributo_único = 'value';
-- Ponga ese valor en varias filas específicas
UPDATE nombre_tabla SET col1 = 'value' WHERE atributo_no_único = 'value';
```

23. **¿Cómo eliminar filas?**

```sql
-- Todas las filas a la mierda
DELETE FROM nombre_tabla;
-- Filas con atributo == 'value' a la mierda
DELETE FROM nombre_tabla WHERE atributo = 'value';
/*DELETE borra todas las filas y por ende la estructura de la tabla.
Si no se quiere eso sino solo borrar los values se usa TRUNCATE*/
TRUNCATE TABLE nombre_tabla;
```

24. **¿Qué sentencias TCL existen?**

- `COMMIT` -> Equivalente a `git commit`: Commitea todos los cambios de sentencias DML no commiteados anteriormente.
- `SAVEPOINT <nombre>` -> Equivalente a `git tag` o `git stash`: Un "checkpoint" de la grabación actual.
- `ROLLBACK` -> Equivalente a `git reset --hard`: Desecha todos los cambios pendientes.
- `ROLLBACK TO SAVEPOINT <nombre>` -> Equivalente a `git reset <commit>`: Desecha todos los cambios hechos hasta el SAVEPOINT.

25. **¿Qué operaciones aritméticas tiene SQL?** Suma (+), Resta(-), Multiplicación(\*) y División(/).

26. **¿Cómo se usa SELECT con alias?**

```sql
-- AS es opcional
SELECT nombre_columna AS nom_col FROM nombre_tabla;
SELECT nombre_columna nom_col FROM nombre_tabla;
SELECT nombre_columna "Nombre de Columna" FROM nombre_tabla;
```

27. **¿Cómo concatenar en un SELECT?**

```sql
SELECT nombre || apellido1 || apellido2  AS "Nombre completo" FROM tabla_con_nombres;
```

28. **¿Cuándo utilizar qué comillas?**

- Simples: Para valores. Ej: `valor = 'Value'`
- Dobles: Para identificadores. Ej: `tabla AS "Tabla Épica"`
- Q: Cuando hay comillas dentro de los operadores "comilla". Ej: `q'[McDonald's]'`

29. **¿Qué hago para quitar las filas duplicadas de mi SELECT?** Usar `DISTINCT`

```sql
SELECT DISTINCT id_equipo, nombre_equipo FROM campeones_ligueros;
```

30. **¿Qué operación precede a WHERE?** FROM tabla

31. **Describa los operadores de comparación**

- `WHERE`: WHERE x = y;
- `=`: x = y;
- `>`, `<`, `>=`, `<=`: x < y;
- `<>`: x <> y -> x != y
- `BETWEEN ... AND ...`: BETWEEN 10 AND 20;
- `IN <set>`, `NOT IN <set>`: manager_id IN (100, 101, 201);
- `LIKE`: Coincide con un conjunto. name LIKE '\_S%' -> aSiento;
  - % - cero o más chars.
  - \_ - un char.
- `IS NULL`, `IS NOT NULL`

## Notación Barker y otras

![alt text](image.png)

## Tipos de datos SQL Oracle

| **Tipo de Dato**                 | **Descripción**                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------------------ |
| **NUMÉRICOS**                    |                                                                                            |
| `NUMBER(p,s)`                    | Números de punto fijo y flotante, con precisión `p` y escala `s`.                          |
| `FLOAT`                          | Números en formato de coma flotante.                                                       |
| `BINARY_FLOAT`                   | Números de coma flotante de precisión simple.                                              |
| `BINARY_DOUBLE`                  | Números de coma flotante de doble precisión.                                               |
| **CARACTERES (TEXTO)**           |                                                                                            |
| `CHAR(size)`                     | Cadenas de caracteres de longitud fija, rellenadas con espacios si es necesario.           |
| `VARCHAR2(size)`                 | Cadenas de caracteres de longitud variable.                                                |
| `CLOB`                           | Almacena grandes bloques de texto, hasta 4 GB.                                             |
| **FECHA Y HORA**                 |                                                                                            |
| `DATE`                           | Almacena fecha y hora con precisión de segundos (día, mes, año, horas, minutos, segundos). |
| `TIMESTAMP`                      | Almacena fecha y hora con fracciones de segundo.                                           |
| `TIMESTAMP WITH TIME ZONE`       | Almacena fecha, hora y zona horaria.                                                       |
| `TIMESTAMP WITH LOCAL TIME ZONE` | Almacena fecha y hora ajustada según la zona horaria local del servidor.                   |
| **BINARIOS**                     |                                                                                            |
| `RAW(size)`                      | Datos binarios de longitud fija.                                                           |
| `BLOB`                           | Almacena grandes objetos binarios, como imágenes o videos, hasta 4 GB.                     |
| **PRECISIÓN FIJA Y NUMÉRICA**    |                                                                                            |
| `INTEGER`                        | Números enteros.                                                                           |
| `DECIMAL(p,s)`                   | Números decimales con precisión y escala definidas.                                        |
| **ESPECIALES**                   |                                                                                            |
| `ROWID`                          | Almacena el ID de la fila en una tabla, único para cada fila.                              |
| `UROWID`                         | ROWID extendido para tablas indexadas externamente.                                        |
| `XMLTYPE`                        | Almacena datos XML estructurados.                                                          |
| **BOOLEANO (solo PL/SQL)**       |                                                                                            |
| `BOOLEAN`                        | Valores booleanos: `TRUE`, `FALSE`, o `NULL` (solo en PL/SQL, no en tablas SQL).           |

## Prioridad de operadores

![alt text](image-3.png)

## Funciones útiles

- `TO_DATE('escrito', 'formato')`: TO_DATE('Sep 04, 2020', 'MON DD, YYYY')
- `NVL(expresión, valor_reemplazo)`: NVL(nombre, 'Desconocido') -> Si nombre es NULL lo cambia por "Desconocido".
- `COALESCE(expresión1, expresión2, ..., expresiónN)`: Mostrar el primer valor no NULL.

# Cap 1

## Conceptos 1

* **Programa de arranque(bootstrap):** Toda compu tiene uno, se encarga de
  iniciar todo aspecto de l sistema, el SO, inicializar los registros del CPU, drivers
  de los I/O, etc. Se suele guardar en el firmaware del hardware.
* **Demonio(daemon),servicio o subsistema del sistema**: Son servicios(procesos) del sistema
  que no están en el Kernel, se ejecutan en **tiempo de arranque**.
  Corren durante el tiempo que esté el Kernel.
* **Interrupciones y Excepciones/trampas**: Las Excepciones son Interrupciones
  que ocasionan el Software de usuario, ya sea por algúnm error o por
  alguna acción del usuario. de aquí vienen los **System Call**.
* **Proceso**: Ejecución de un programa en CPU en un Sistema **Multiprogramado**
* **Intrucción privilegiada**: Son intrucciones que solo se ejecutan
  en modo Kernel, si se intenta hacer una de estas en modo Usuario,
  el hardware la atrapa en el SO. Ej: Manejo de tiempo, Interrupciones,
  control de I/O, etc.
* **Vector de syscalls**: Las API guardan en una lista los syscall.
  Entonces su uso se hacer indexando el número de syscall.
* **Aros de protección**: Así se le llama a los modos en un
  sistema multimodos.
* **Drivers de dispositivos**: Normalmente, los sistemas operativos tienen un controlador de dispositivo para cada controlador de dispositivo. Este controlador de dispositivo entiende el controlador de dispositivo y proporciona al resto del sistema operativo una interfaz uniforme para el dispositivo. La CPU y los controladores de dispositivo pueden ejecutarse en paralelo, compitiendo por ciclos de memoria. Para garantizar un acceso ordenado a la memoria compartida, un controlador de memoria sincroniza el acceso a la memoria.
* **Vector de interrupciones**: Ya que se tiene que hacer bastante seguido interrupciones, el sistema tiene un vector de interrupciones en las posiciones bajas de la memoria, este vector contiene las direcciones de las rutinas de servicio de interrupciones para el dispositivo que intenta interrumpir.
* **Encadenamiento de interrucpiones**: Cada elemento del vector de interrupciones apunta a una lista de manejadores de interrupciones. Se llama uno por uno a los manejadores hasta que se encuentra el servicio que se pidió al interrumpir.
* **Núcleo(core)**: Componente de CPU que se encarga de ejecutar instrucciones y registros para guardar datos localmente.
* **CPU**: Hardware que ejecuta instrucciones.
* **Procesador**: Chip físico que contiene uno o más CPUs.
* **Núcleo(core)**: Unidad básica de computación(cálculos) del CPU.
* **NUMA (non-uniform mem. access)**: Cuando todos los CPUs comparten espacio de mem. física.

## Preguntas 1

1. **¿Cuáles son las tres partes de un SO?**  
Hardware(CPU, I/O, etc.), Software (Apps, programas) y Usuario.  
2. **¿Qué hace un SO?**  
  Permite a un usuario hacer uso de aplicaciones
  que a su vez hacen uso de los recursos que provee
  el SO, es decir, un SO entrelaza a sus partes.
3. **¿Cómo se inicia el SO?**  
   El bootstrap lo busca en el **Kernel** del SO y lo carga en mem.
4. **¿Cómo funciona un Sistema Multiprogramado?**
   En este Sistema se tienen **procesos** los cuales van intercambiadose
   el uso del CPU, cada vez que hay un estado de IDLE puede haber una
   espera(pausa) en cuanto al uso de CPU para el proceso, cuando uno
   espera el otro puede seguir su ciclo.
5. **¿Cómo distingue el SO entre código de usuario y código del Sistema?**  
   Tiene que haber al menos dos modos: **Modo usuario** y **modo Kernel/sistema/
   supervisor/privilegiado**. Estos modos los tienen añadidos
   el hardware para indicar el modo actual (bit de modo): ```0 - kernel, 1 - user```
   Esto es útil para diferenciar entre una tarea ejecutada por
   usuario de una ejecutada por el SO.
   * En tiempo de arranque el Sistema está en Modo kernel.
   * Pueden haber más de dos modos.
     * Modo VMM (Virtual Machine Manager), se encuentra entre
      modo Kernel y usuario en cuanto a "poder" esto para ser capaz
      de cambiar el estado del CPU pero no exceder al poder del sistema
      como el Kernel.
6. **(1.5) ¿Cómo funciona la distinción entre modo núcleo(kernel) y modo usuario como forma rudimentaria de protección (seguridad)?**
7. **(1.9) Podrían utilizarse temporizadores para calcular la hora actual. Describa brevemente cómo podría hacerse.**
   Utilizando un contador que se decremente cada un segundo gracias al "timer". Cada un segundo se aumenta el número de segundos a una hora previamente establecida y así se va a ir moviendo el reloj.
8. **(1.11) Distinguir entre los modelos cliente-servidor y peer-to-peer de los sistemas distribuidos.**
9. **¿Qué es un API?**
10. **¿Qué métodos hay para introducir los parámetros de una función de un API en el SO para un syscall?**
    * Pasarlo por registro (usualmente para 5 o menos params).
    * Guardarlo en un bloque o tabla en mem. para luego traerlos por "partes" como params en los registros.
11. **¿Qué se hace tras una interrupción por dispositivo?**  
  Si la rutina de servicio de interrupción para un dispositivo ocupa cambiar el estado de algo en el Sistema, por ejemplo de un registro, entonces guardaría el estado anterior, lo modificaría y antes de retornar lo volvería a ese estado. **Volver como si nada hubiera ocurrido**.
  La CPU detecta las interrupciones a través de una **línea de solicitud de interrupción** y salta a una **rutina de gestión de interrupciones** basada en el número de interrupción para procesar la interrupción (en el **vector de interrupciones**). El manejador guarda el estado, procesa la interrupción, restaura el estado y devuelve la CPU a su estado anterior. En este proceso intervienen el controlador de dispositivo que señala la interrupción, la CPU que la gestiona y el manejador que da servicio al dispositivo para borrar la interrupción.

* Controlador de disp. *raises*, CPU *catches* and *dispatch*, Majeador *clears*

12. **Tipos de interrupción de dispositivo**
    * ``Enmascarable:`` puede ser anulado por la CPU antes de la ejecución de secuencias de instrucciones críticas que no deben ser interrumpidas.
    * ``No enmascarable:``que se reserva para eventos como errores de memoria irrecuperables. Osea que no deberían de ser postergados.

## Recursos 1

![F1.2](images/typicalPCSyst.jpg)
![F1.6](images/storDevc-hierarchy.jpg)
![F1.7](images/modernSysWork.jpg)
![F1.14](images/storageTypesCharacteritics.jpg)

# Cap. 2

## Conceptos 2

* **Shells**: Interpretadores de comandos (CLI - Command-line interface).
* **Interfaz de syscall**: Intercepta los llamados de las API y hace los syscall necesarios para cubrilos.

## Preguntas 2

1. **¿Qué servicios ofrece un SO?**
   Interfaz de Usuario (GUI, touch-screen, CLI), Seguridad, manipulación del Sistema de Archivos, ejecución de programas, operaciones de I/O, detección de errores, registros(log), comunicación,  Asignación de recursos, protección y seguridad.(10)

2. **¿Qué tipos de llamados al sistema existen?**
   Existen 6 grandes grupos: Control de procesos, manejo de archivos, manejo de dispositivos, mantenimiento de info., comunicación y protección.

3. **¿Cómo es el ciclo de un llamado al sistema por parte de una aplicación de usuario?**
  Se produce el llamado tras el uso de una función de algún lenguaje (API), este llamado en modo usuario hace que la app guarde en un Stack on un arreglo en memoria los parámetros que se introdujeron en la API. Luego el Sistema pasa a modo Kernel para hacer el verdadero Syscall el cual se elige en el vector syscall, el SO toma la dirección de los params. del registro donde la app de usuario lo puso, y con esto el syscall obtiene sus datos haciendo POP en el stack en mem. Este proceso se hizo con una Interrupción la cual termina al retornar del syscall.
4. **¿Qué tipo de servicios o utilidades ofrecen los SO?**
   * Manejo de archivos: Crear, borrar, copiar, renombrar, listar y en general manipular archivos y directorios.
   * Modificación de archivos: Crear y modificar archivos que están en almacenamiento.
   * Estado e información: Dar la hora, espacio libre en el disco, cantidad de mem., cantidad de usuarios, información de registro(logging) y depuración(debugging).
   * Soporte de lenguajes de progra.: Compiladores, linkers, ensambladores, depuradores, interpretadores.
   * Carga y ejecución de programas: Un programa se ensambla, se compila y se carga en memoria para poder ejecutarlo. Puede proveer loaders absolutos, reubicables. Editores de enlace.
   * Comunicación: Proveen mecanismos que permiten coexiones virtuales entre procesos, usuarios y sistemas de compus.
   * Servicios de fondo (background): Procesos de uso general que se inician en tiempo de arranque. ``daemons, servicios o subsistemas``. Además de programas de aplicación de uso común.

## Recursos 2

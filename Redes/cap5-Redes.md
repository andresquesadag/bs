# Cap 5: Capa de Red

1. ¿De que se encarga la capa de Red?
  Se encarga de llevar los paquetes desde el origen hasta el destino.
2. ¿La capa de red debe de conocer la topología de las redes?
  Sí, como en OSPF, pero tiene que conocer el de todos las redes que conecta entre sí.
3. ¿Qué servicios ofrece la capa de Red a la capa de transporte?
   1. **Sin conexión**: Paquetes se envían y se enrutan de manera independiente en la red.
      1. Paquetes == **Datagramas**
      2. Se le conoce por ende como **Red de datagramas**.
      3. Ej: **IP**. 32 bits (IPv4) y 128 bits (IPv6).
   2. **Orientado a la conexión**: 
      1. Se establece una ruta entre origen y destino antes de enviar cualquier paquete.
      2. **Circuito Virtual(VC)** -> **Red de circuitos virtuales**.
4. ¿Qué requisitos se deben cumplir para poder brindar esos servicios?
   1. Los servs. son **indep. de la tecnología** del enrutador.
   2. A la **capa de transporte no le importa nada** sobre la topología, tipo o cantidad de enrutadores presentes, debe de trabajar sin importar nada de eso.
   3. Las redes disponibles deben de tener una **numeración uniforme**.
5. ¿Para qué y dónde se utilizan las tablas de línea de destino?
   Estas tablas están presentes en los routers, tienen una col. de destino y otra col. de línea de salida. **Serv. Sin Conexión**.
   Para **Serv. Orientado a la Conexión** la tablas es más como: Hay "dos tablas", la primera tiene de qué host viene la conexión, la segunda col tiene el id de conexión, la segunda tabla tiene por dónde se envía el paquete de esa conexión y la segunda col tiene el identificador que se le dará a esa conexión. Se puede dar en un orden establecido el envío que se hizo

# Diseño de Software

## Juego del laberinto (24-25)

### La última implementación del proyecto está aun work in progress

---

Repositorio en el que estará mi implementación en **Python** del laberinto hecho en clase en **Smalltalk**.
El documento se irá actualizando para añadir, modificar, o eliminar, si fuese necesario, las explicaciones de cada elemento, además de también actualizar el diagrama UML.


### Características:

- **Laberinto** 🧩: Contenedor de habitaciones. Dispone de funciones para añadir o conectar elementos
- **ElementoMapa** 🗺️: Clase padre o base de los elementos de los que estará compuesto el mapa (pared, puerta, habitación...)
  - **Habitación** 🏠: Se conectan unas con otras gracias a la orientación (```norte```, ```sur```, ```este```, ```oeste```). Se les asigna un ```número``` para poder identificarlas.
  - **Pared** 🟫: Pues eso, paredes. Una habitación necesita paredes. Y te puedes [chocar](https://pbs.twimg.com/media/Ex4dJT1UcAIdwdU.jpg) con ellas.
    - **ParedBomba** 💣: Clase que hereda de *Pared*. Tiene una bomba que puede o no estar ```activa```.
  - **Puerta** 🚪: Una habitación necesita una puerta para poder entrar, o salir. Estas conectan habitaciones, pues una puerta tiene ```lado1``` y ```lado2```. Puede estar, o no, ```abierta```.

- **Creator** 🛠️: Con esta clase podemos fabricar el laberinto y sus elementos (fabricar pared, fabricar puerta, fabricar habitación...).
  - **CreatorB**: Subclase de *Creator* que fabrica paredes bomba.
- **Decorator**: Sirve para agregar responsabilidades nuevas (Bomba) a otros objetos (Pared, Puerta...). Hereda de ElementoMapa y crea Bombas.

- **Bicho** 🐛: Un bicho puede ser ```agresivo``` o ```perezoso```, depende del modo en el que se encuentren.
  - **Strategy**: Encapsula familias de algoritmos como objetos. En nuestro proyecto, lo hemos implementado para el modo de los bichos (Agresivo o Perezoso).

- **Composite**: Lo utilizamos para representar estructuras recursivas todo-parte. Simplifica a los clientes porque pueden tratar de manera uniforme a compuestos y hojas. En nuestro proyecto, el Composite lo forman ElementoMapa (Component), Contenedor (Composite) y Hoja (Leaf)
- **Iterator**: El iterador interno se implementa con la operación recorrer(unBloque). El parámetro unBloque es una función anónima. Es adecuado para estructuras tipo Composite.
- **Singleton**: Implementado en las Orientaciones.
- **Template Method**: EL método ```actua``` de Modo es un Template Method. Las operaciones primitivas son: dormir, caminar, y atacar.

---

## Diagrama UML pre-implementaciones

![Diagrama UML pre-caos](https://github.com/danreqmun/laberinto25/blob/main/imagenes/Main.png?raw=true)

## Modificaciones

Como no deja exportar (por ser versión gratuita, supongo) y hacer una captura de pantalla tan grande haría que no se pudiese leer bien, haré capturas de pantallas a las modificaciones.

### Template Method (TM) + Chain of Responsibility (CoR)
#### CoR
El método ```manejar()``` es el corazón del patrón CoR.
Una explicación sencilla del cómo funciona es:
Imagina una fila de objetos, como una cadena ⛓️, y tú haces una pregunta:
"¿Eres tú el objeto que quiero usar?"
Digamos que tengo el siguiente Inventario: < Tótem , Pócima , Bolsa > y hago ```inventario.usar(personaje, "Pócima")```. Esto hace lo siguiente:
1. Inventario lanza la cadena con ```cadena.manejar(personaje, "Pócima", self)```
2. El Totem recibe eso y hace: "¿Me llamo Pócima?" $\rightarrow$ ***No*** $\rightarrow$ pasa al siguiente.
3. Pócima recibe la petición: "¿Me llamo Pócima?" $\rightarrow$ ***Sí***
   - Aplica su efecto con ```usar(personaje)```
   - Se elimina del inventario (solo un uso por objeto) $\rightarrow$ ```inventario.objetosBolsa.remove(self)``` 
   - Devuelve True (se ha usado)
En este ejemplo, ```inventario.objetosBolsa``` porque las pócimas solo las uso en la Bolsa. Si fuese un Totem, haría ```inventario.eliminar(self)```

#### TM
Podemos observar cómo ObjetosMapa (abstracta) define ```usar()```, ```recoger()``` y ```devPeso()```, para que las subclases correspondienten las implementen.
Bolsa sí las implementa directamente, mientras que para *Tótem* y *Pócima*, implementando las dos útlimas operaciones mencionadas anteriormente en su clase padre, *HojaObjeto*, pues estas operaciones son las mismas para cada objeto. Pasa ```usar()``` a los objetos hijos.
Esta clase abstracta también define dos operaciones para que *Tótem* y *Pócima* implementen, ```es_usable``` y ```aplicarEfecto```, ya que cada objeto tiene su propia condición y efecto(s).

Cada objeto en esa cadena tiene su propio método manejar() para responder
![Diagrama UML final](https://github.com/danreqmun/laberinto25/blob/main/imagenes/CoR+TM.png?raw=true)

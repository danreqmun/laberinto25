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

### Diagrama UML

![Diagrama UML](https://github.com/danreqmun/laberinto25/blob/main/Main.png?raw=true)

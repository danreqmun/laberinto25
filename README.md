# Diseño de Software

## Juego del laberinto (24-25)

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

~~- **Creator** 🛠️: Con esta clase podemos fabricar el laberinto y fabricar paredes.~~
  ~~- **CreatorB**: Subclase de *Creator* que fabrica paredes bomba.~~
  - **Decorator**:

---

### Diagrama UML

![Diagrama UML](https://github.com/danreqmun/laberinto25/blob/main/Main.png?raw=true)

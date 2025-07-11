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

---

<br>

# Modificaciones

Como no deja exportar (por ser versión gratuita, supongo) y hacer una captura de pantalla tan grande haría que no se pudiese leer bien, haré capturas de pantallas a las modificaciones.

## Template Method (TM) + Chain of Responsibility (CoR)
### CoR
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

Una analogía De la vida real:
Imagínate estar en una tienda y pides ayuda a un empleado, y este te dice “eso no es lo mío, pregúntale al siguiente”. Finalmente uno dice "sí, eso lo llevo yo" y te ayuda.
Ese "pasar la petición" es lo que hace el ```manejar()```.

### TM
Podemos observar cómo ObjetosMapa (abstracta) define ```usar()```, ```recoger()``` y ```devPeso()```, para que las subclases correspondienten las implementen.
Bolsa sí las implementa directamente, mientras que para *Tótem* y *Pócima*, implementando las dos útlimas operaciones mencionadas anteriormente en su clase padre, *HojaObjeto*, pues estas operaciones son las mismas para cada objeto. Pasa ```usar()``` a los objetos hijos.
Esta clase abstracta también define dos operaciones para que *Tótem* y *Pócima* implementen ```es_usable``` y ```aplicarEfecto```, ya que cada objeto tiene su propia condición y efecto(s).

Cada objeto en esa cadena tiene su propio método manejar() para responder
![Diagrama CoR y TM](https://github.com/danreqmun/laberinto25/blob/main/imagenes/CoR+TM.png?raw=true)

<br>

## Flyweight
"Utiliza compartir para soportar un gran número de objetos pequeños".
Este patrón es perfecto para la idea de que un bicho "suelta" algo al morir (monedas de oro y plata).
Este patrón fabrica una sola copia de cada moneda y la "duplica", para ahorrar de manera eficiente memoria, sin tener que crear muchas monedas. Una manera de ver esto es al debuguear, se puede ver como en el inventario o en ```habitacion.hijos``` aparece Moneda varias veces, pero con la misma dirección de memoria.
Esencialmente, Flyweight dice "Oye, esas monedas son todas iguales, ¿por qué no usamos solo una y la compartimos?".

***Mal***: Esto crea 5 monedas de oro nuevas en memoria, aunque todas son iguales (mismo tipo, mismo peso) y se acabara con decenas (podrían ser miles) de monedas duplicadas en memoria.
```python
for _ in range(5):
    habitacion.agregarHijo(Moneda("oro", 0.1))
```

***Bien (ahora)***: Ahora solo se crea una Moneda de oro y todas las habitaciones la reutilizan por referencia.
```python
oro = MonedaFactory.getMoneda("oro")
o = random.randint(1, 4)
for _ in range(o):
    unAtacante.posicion.agregarHijo(oro)
```

![Diagrama Flyweight](https://github.com/danreqmun/laberinto25/blob/main/imagenes/Flyweight.png?raw=true)

<br>

## Decorator y Factory Method (FM)
### Decorator
Con este patrón, se puede "envolver" o "vestir" cualquier ElementoMapa, cosa que añade dinamismo. En este caso, Pared.
```python
Flecha(Pared())
```

### Factory Method
Si solo queremos una pared que haga algo y ya, sin mezclar, podemos usar este patrón.
```python
return ParedFlecha()
```

***Nota***: Es muy importante que se implemente la operación ```entrar()``` en ambas clases. Y en las clases Decorator (flecha y bomba), hay que añadir ```self.elemento.entrar(ente)```, para que se ejecute primero la lógica original del elemento decorado.

![Diagrama Decorator y Factory Method](https://github.com/danreqmun/laberinto25/blob/main/imagenes/Decorator+FM.png?raw=true)

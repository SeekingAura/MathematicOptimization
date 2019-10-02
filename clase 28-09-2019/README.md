# Programación no lineal

## Caracteristicas
* Procedimientos iterativos
* Se reuqiere de una condición inicial
* Tiene un aestrategia definida
* Criterios de parada
* Debe garantizar: robustez, eficiencia, precisión
	* Precisión: lo cerca que está de la solución real
	* Exactitud: es que el resultado sea de un valor estricto no necesariamente el respectivo al que deberia de ser
* Función objetivo y restricciones diferenciables
* Continuidad
* Problemas determinísticos
* Criterios de parada
* Función objetivo convexa (min)/cóncava (max)
* Espacio de solución convexo

# Métodos de búsqueda irrestricta
* Unidimensional
	* Métodos que no usan derivadas
		* Sección dicotómica
		* sección dorada
		* Método Fibonacci
	* Métodos que usan derivadas
		* Bisección
		* Newton

## Sección dicotómica
Una función que tiene forma de convexa (concava hacia abajo), como no tiene pendiente estable en una de las partes de la función si no que tiene un comportmaiento de tendencia se le denomina **cuaci-convexa**, y si logra estar a un valor constante de pendiente 0 seria **semi-convexa**.

![image](/images/clase&#32;28-09-2019&#32;1.jpeg)

se evalua la función en un punto lambda y un punto u, si la f(u) es mayor que f(lambda) se quita el area que está hacia el lado de u hacia b, caso contrario aplciaria con lambda hacia a asi como indica la imagen

La condición de parada es:  
Si la distancia del punto a al punto b es < 2epsilon

## Sección doarada
Utiliza un número dorado que es la distancia de *a* al *u* y de *b* a *lamda*, el cual es estas distancias al dividarlas deben ser iguales en su misma oepración para la siguiente oepración, el valor del número dorado va a tender a ser 0,628

![image](/images/clase&#32;28-09-2019&#32;2.jpeg)

## Método de Fibonacci
Se establece la cantidad de iteraciones de acuerdo a la serie de iteraciones de fibonacci el cual se aplica en el parametro alpha, la primera iteración seria el valor de fibonacci dado el cual divide al valor anterior de la serie

|1|2|3|4|5|6|7|8|9
|-|-|-|-|-|-|-|-|-|
1|1|2|3|5|8|13|21|34

Se establece desde cual valor enesimo de la serie de fibonacci se inicia y desde ese se calcula el lambda, para la iteración 1 con valor del noveno número de la serie fibonacci:  
alpha= 21/34  

Para la siguiente iteración es apartir del no usado que es el valor del septino número de la serie de fibonacci (ya que utilizó el noveno y el octavo en la iteración 1)
alpha=13/21

es decir que cada iteración utiliza los 2 parde números enesimos de la serie de fibonacci que no haya usado, para determinar el valor de **lambda** y el valor de **u** 

![image](/images/clase&#32;28-09-2019&#32;3.jpeg)


## Método de Bisección
Este obtiene evalucaciones de la función con la primera derivada, si esta derivada su pendiente es negativa quiere decir que a medida que va hacia la derecha se reduce, por tnato si este aplica en el valor de **lambda** el area que hay entre **lambda** y **a** es descartado, de la misma forma para el lado contrairo en sentido contrario; este método tiene una convergencia más rapida.

Este método encuentra el maximo global una vez que la pendiente sea cero, es decir encuentre un punto estacionario.

## Método de Newton
El método de newton utiliza la aproximación por medio de la serie de taylor, a traves de este trata de calcular el minimo local de su función representativa, tras cada iteración se aproximará hacia su representativa basandose en cada punto respecto al punto referente.

![image](/images/clase&#32;28-09-2019&#32;4.jpeg)

Parte de un valor **lambda k** hacia un valor de **lambda k+1** el cual lo obtiene por medio de la función evaluada con series de taylor en su punto estacionario

La función teta es la función del caso y la función q es la función roja que es el punto referente para **lambda k+1**

![image](/images/clase&#32;28-09-2019&#32;5.jpeg)

Este algoritmo aveces tiene el problema de que puede diverger.

Al evalular el valor de la función en la primera derivada y la segunda derivada el valor del siguiente punto de **lambda k+1** será la división de la primera derivada con la segunda derivada.

El algoritmo de newton se peude utilizar unicamente si se sabe de un punto si está cercano a la solución de resto puede diverger.

Dado a que busca puntos estacionarios no es necesario modificar el algoritmo para determinar la respuesta, sin embargo, puede fallar en ciertas funciones como una semi concava puede no converger a ningún lado, generando oscilaciones

![image](/images/clase&#32;28-09-2019&#32;6.jpeg).

# Busqueda irrestrictrica en multiples dimensiones
en un caso de multiples variables suele darse el problema del countering (contorno) que grafica funciones en multiple dimension permitiendo en el caso de 3d determinar la profundidad de un monton de puntos.

![image](/images/clase&#32;28-09-2019&#32;7.jpeg)

la imagen anterior es como de un vaso redondo que forma un elipsoide para el caso de minimizar entre mayor sea el valor será el radio del elipsoide mayor y contrario para el otro caso.

Para este problema se ubica en un punto del espacio de soluciones y se elige hacia cual lado ir para encontrar pro donde deciende o aumenta el resultado de la función según lo requerido.

Si es el caso de minimizar se busca dirección de busqueda que será hacia el lado que la función evaluda en esos valores de como cambiaron menor de donde estaba, se avanza hasta que el valor evaluado en la función sea mayor que el paso anterior, en ese momento la dirección debe de cambiar a algun otro lado que el valor disminuya.

## Métodos para busquedas de multiples dimensiones
* Métodos que no usan derivadas
	* Método coordenadas cíclicas
* Métodos que usan deriviadas
	* Método gradiente
	* Método newton
	* Métodos direcciones conjugadas

### Métodos coordenadas cíclicas
En este método se inciia desde un punto de partida y luego de puede avanzar en solo dos direcciones posibles *derecha* e *izquierda*, una iteración es avanzar en una de las direcciones evalua cada paso hasta que la evaluación de la función aumenta respecto al anterior, luego cambia de dirección hace el mismo proceso y para

![image](/images/clase&#32;28-09-2019&#32;8.jpeg)

efectua espacios de exploración en forma de circulo

![image](/images/clase&#32;28-09-2019&#32;9.jpeg)

![image](/images/clase&#32;28-09-2019&#32;10.jpeg)


### Método Gradiente Descendente
Se obtiene el gradiente de la función y aplica de maenra similar al del circulo (avanzar mientras sea menor respecto a la posición anterior)


### Método gradiente conjugado
..


# Especial de problema geometrico
![image](/images/clase&#32;28-09-2019&#32;11.jpeg)

El pertenece a la región factible (Condición de factibiilidad del primal)

Para problemas de Maximizar y restriccioens d emenor igual, el gradiente de la función objetivo pertenece al cono convexo formado por las condiciones activas (condiciones de fatibilidad del problema dual o optimal del primal).

El calculo de ese gradiente y el cono convexo es a razón de los puntos canditado se coloca los puntos obtenidos de la derivada de las restricciones implicadas en ese punto tomando como origen el punto candidato a analizar.
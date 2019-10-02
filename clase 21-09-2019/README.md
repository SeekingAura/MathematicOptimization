# programación no lineal
Son problemas en lso que las funciones ya **No** son rectas si no que son curvas, los problemas que se abarcarán en el curso son curvas "suaves" que sean convexas

Simplex no puede reoslver la mayoria de estos problemas, debido a que este busca es las intersecciones con el modelo y encontraria los verdaderos problemas

![image](/images/clase&#32;21-09-2019&#32;1.jpeg)

## Conjunto convexo
S es convexo si y solamente si existen valores x<sub>1</sub> y x<sub>2</sub> (par de puntos) tales que x<sub>1</sub>, x<sub>2</sub> Petenece a S (la región factible) para que sea convexa tiene que haber la posibilidad de formar conjuntos de combinaciones convexas que petenezcan al espacio de solución, si un punto está fuera dle conjunto convexo Ya **NO** es conjunto convexo.

Otra forma de determinar la convexidad que TODA pareja de puntos al trazar una linea recta todos los puntos que conforman dicha linea es parte de la región factible es convexo, de lo contrario no lo seria

### Ejemplos
* Los problemas de programación lineal siempre son convexos
* Una región con curvas puede llegar a tener regiones no convexas
* Los problemas de programación entera logran regiones no convexas

![image](/images/clase&#32;21-09-2019&#32;2.jpeg)

#### Mostrar que un conjunto es convexo
![image](/images/clase&#32;21-09-2019&#32;3.jpeg)

---

## Funciones convexas
Un conjunto convexo tambien ouede ser determinado a raxzón de funciones lo cual hay varios tipos.

* cóncava: Es una función la cual presenta cambios de minimo a maximo y vuelve a minimo(así como una parabola de la forma (x-h)^2=4p(y-k) con p<0) funciones del mismo estilo a la parabola tambien aplican
* diferenciable: es una función que en su grafica no tiene cambios *bruzcos* es decir que no presenta discontinuidades (puede tomar todos los valores en su espacio real y en sus derivadas)
* convexo: Es una función la cual presente cambios de máximo a minimo y vuelve a maximo ( asi como parabola de la forma (x-h)^2=4p(y-k) con p>0)

maximo - maximus
minimo - infimo

## Funciones convexas diferenciales
Sea un conjunto no vacío en R^n y sea *f*:s en los relaes. Se dice que *f* es diferenciable en xbarra Pertenece en el conjunto S si existe un vector de gradiente(xbarra), llamado vector gradiente y una función.

Una función curva puede formarse con funciones lineales que estén debajo de este con un error pequeño (rectas tangentes) sin que la superen es uan función convexa y dependiendo de la estructura de los puntos seria concava hacia arriba o hacia abajo

Por definición un Hiperplano es concavo y convexo de manera simultanea (un hiperplano es una recta tangente sola)


## minimos y maximos
Las funciones que son **convexas** pueden encontrar facilmente su minimo global, las funciones que son **concavas** tienen un maximo global, siendo un ideal para los problemas de minimizar y maximizar respectivamente

![image](/images/clase&#32;21-09-2019&#32;4.jpeg)

## Funciones convexas de segundo orden (doblemente diferenciables)

![image](/images/clase&#32;21-09-2019&#32;5.jpeg)

![image](/images/clase&#32;21-09-2019&#32;6.jpeg)

En la ecucación para doblemente diferenciales es la Hesiana la que define si es Convexa ">=0" o Concava "<=0" 

![image](/images/clase&#32;21-09-2019&#32;7.jpeg)

![image](/images/clase&#32;21-09-2019&#32;8.jpeg)

![image](/images/clase&#32;21-09-2019&#32;9.jpeg)

![image](/images/clase&#32;21-09-2019&#32;10.jpeg)

![image](/images/clase&#32;21-09-2019&#32;11.jpeg)

![image](/images/clase&#32;21-09-2019&#32;12.jpeg)

![image](/images/clase&#32;21-09-2019&#32;13.jpeg)

**autovalor:** Son todos los valores propios que tiene una matrix (H-lambdaI)

SDN: Semi-Definido Negativo
SDP: Semi-Definido Positivo

H(x) es SDN (cóncava) si -H(x) es SDP (convexa)

### Chequeo de convexidad caso nxn
Sea **H** una matriz simétrica con elementos hij.
1. Si h<sub>11</sub><=0 -> No es SDP
2. Si h<sub>ii</sub>=0 -> h<sub>ij</sub>=h<sub>ji</sub>, es decir es simetrico, de lo contrario no es SDP
3. Si n= 1 -> H es SDP ssi h<sub>ii</sub>>0.  
Si n>=2 -> H=\[\[ h<sub>ii</sub>, q^t\], \[q, G\]\]

Realizar operaciones elementales de Gauss-Jordan para tener

H=\[\[ h<sub>11</sub>, q^t\], \[q, G\]\]

```python
[
    [2, -1, 2],
    [-1, 2, -1],
    [2, -1, 5],
]

[
    [1, -1/2, 1],
    [0, 3/2, 0],
    [0, 0, 3],
]

[
    [3/2, 0],
    [0, 3],
]

[
    [1, 0],
    [0, 3],
]

[
    [3]
]

Es concava
```

## Condiciones de Optimalidad a problemas irrestrictos
Problemas irrestrictos aparecen raramente en aplicaciones prácticas. Sin embargo, una estrategia para resolver problemas restringidos considera la solución de una secuencia de problemas irrestrictos

![image](/images/clase&#32;21-09-2019&#32;14.jpeg)

![image](/images/clase&#32;21-09-2019&#32;15.jpeg)

### Derivadas en las funciones
Derivar puede indicar puntos de inflexión, puntos estacionarios e indicar si es un minimo o maximo global.

Si al derivar una función varias veces hasta que llegue al valor constante es mayor que cero y pertence a X y ademas de eso su derivada anterior es un punto estacionario




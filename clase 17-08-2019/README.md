# ¿Qué es optimizar?
Es buscar un objetivo generalmente es *mejorar* algo, dependiendo del problema será el modo. Según la perspectiva será el planteamiento o la estructuración del problema bien sea con:

* Maximizar o minimizar recursos o procesos
* Dado una cantidad de recursos ¿Como se pueden aprovechar al maximo? (mayor beneficio)
* Hacer lo mismo con menos recursos
* Cambiar recursos ineficientes por recursos eficientes
* Eliminar recursos existentes que afectan negativamente el sistema


## Estructura de un problema de optmimización
* Objetivo
    * Maximizar
    * Minimizar
* **Restricciones:** el uso de los recursos o *limitantes* del problema

Esta estructura el problema debe ser planteado por medio de un *mundo virtual* donde dependiendo de lo que se desea abarcar del problema se debe de:
* Determinar si maximizar / minimizar 
* Se pleantea una función *f(x)* que modela el problema
* Se plantean las restricciones que son dadas por *g_i(x) <= 0* *i=1, ..., n*
* *h_j (x)=0* *j=1, ..., ?*

Los problemas a abarcar son modelos de programación lineal (PL) los cuales son de polinomios de grado 1 y pueden tener n variables dados en:

*f(x), g_i(x), h_j(x) : R^n --> R*

Estas funciones son escalares y funciones lineales, la mayoria de los problemas los abarca la Programación no lineal (PNL).

# Ejemplo 1
Se dispone de determinadas piezas para la elaboración de dos productos finales. Se dispone de 8 *piezas pequeñas* y 6 *piezas grandes*, que son utilizadas para elaborar sillas (usando 2 piezas pequeñas y 1 pieza grande) y mesas (usando 2 piezas de cada tipo).

Interesa decidir cuántas sillas y mesas se debe fabricar de modo que permita obtener la máxima utilidad, dado un beneficio neto de 3 por cada silla y 4 por cada mesa fabricada.

## Solucionando algoritmo
La utilidad es dado por la cantidad de sillas y mesas vendidas, en este caso se quiere maximizar las sillas por lo cual es vender la mayor cantidad posible de estos.

### Variables
Las variables de este problema son la cantidad de sillas y mesas que se hagan, en este caso sería.

x_1 -> # Sillas ]
                ] X Pertenece a R^2
x_2 -> # Mesas  ]

n=2 (número de variables)

### Función
Hay que colocar las variables según al problema, en este caso es por cada silla es 3 dolares de ganancia neta y por cada mesa es de 4 dolares de ganancia neta, los corchetes contiene su "tipo de dato" o valor o unidades si queda bien el resultado de la función se da en terminos de lo que se quiere abarcar en este caso es ganancia neta que se puede **representar** en **dinero**.

Maximizar f(x) = 3[$/Silla]\*x_1[Silla] + 4[$/mesa]\*x_2[mesa]

al efectuar los operadores de simplificación se obtiene que:

Maximizar f(x) = 3[$]\*x_1 + 4[$]\*x_2

Mesa se va con mesa y silla con silla y resulta que los tipos de datos que se obtienen es en terminos de dinero.

### Restricciones
Las restricciones normalmente es dado por los limitantes que tiene, en este caso es solo por el uso de los recursos siendo:

* **Respetar el limite de piezas grandes** - Esta restricción según al problema es lo que necesita de piezas grandes cada una de las variables para crearse quedando asi:

1[pieza_grande/silla]\*x_1[silla] + 2[pieza_grande/mesa]\*x_2[mesa] <= 6 [piezas_grandes]

recordemos que los corchetes contienen los tipos de datos y en este caso las restricciones deben ser a ambos lados de la desigualdad del mismo tipo, lo cual al simplificar queda

1[pieza_grande]\*x_1 + 2[pieza_grande]\*x_2 <= 6 [piezas_grandes]

* **Respetar el limite de piezas pequeñas** - Esta restricción según al problema es lo que necesita de piezas pequeñas cada una de las variables para crearse, de manera similar ha de cumplir los mismos tipos de dato a ambos lados de la desigualdad, quedando asi directamente:

2[pieza_grande]\*x_1 + 2[pieza_grande]\*x_2 <= 8 [piezas_grandes]

* **No negatividad:** muchos de los problemas no pueden por terminos de fisica ocurrir ciertos valores, sin embargo, es bueno indicarlo por que hay otros casos que si ya que si no se indica se asume que abarca todos los valores quedando asi:

x_1 >= 0  
x_2 >= 0

* **Integralidad:** Asi como solo se abarcan los positivos en ocasiones y debe discriminarse tambien deberá indicarse el rango de valores que abarca asi

x_1, x_2 pertenece Z_+

Con eso se indica que abarca los enteros positivos.

# Ejemplo 2
Supongamos que un banco dispone de $250 millones para destinar a 4 tipo de créditos ofrecidos, los cuales tienne las siguientes tasas de crédito:
* Primer crédito corriente: 12%
* Segundo crédito corriente 16%
* Crédito para el hogar 16%
* Crédito personal 10%

La asignación de estos créditos, debe satisfacer la siguiente política utilizada por la institución:

El monto asignado a los PCC, debe ser al menos, el 55% del monto asignado a los créditos corrientes, y al menos un 25% del total del dinero prestado.

El SCC, no puede exceder el 30% del total del dinero prestado, por políticas tributarias el interés recibido por el banco no debe exceder a un retorno del 14% sobre el capital.

## La pregunta
¿Cuanto asignar a cada tipo de crédito, de la manera más eficiente, respetando la política del banco?

## Variables de decision
x_1 : Monto asignado al PCC (Primer credito corriente)
x_2 : Monto asignado SCC (segundo credito corriente)
x_3 : Monto asignado al crédito para el hogar
x_4 : Monto asignado al crédito personal

## Solucionando

Maximizar retornos
Variables
x_i -> % de dinero invertido en el credito i
i=1 : PCC  
i=2 : SCC  
i=3 : CH  
i=4 : CP  

Este problema puede plantearse tanto de forma de porcentjae o con las cantidades directamente

Max f(x) z = x1\*0.12 + x2\*0.16 + x3\*0.16 + x4\*0.14

restricciones

x1 + x2 + x3 + x4 <= 1  
x1 >= 0.55 * (x1+x2)
x1 >= 0.25 * (x1 + x2 + x3 + x4)
x2 >= 0.30 * (x1 + x2 + x3 + x4)
z  <= 0.14 * (x1 + x2 + x3 + x4)
0<=xi<=1 i=1 ... 4

Estas restricciones deben estar en terminos lineales por lo cual debe resolverse las factorizacione sy multiplicaciones o divisiones

x1 >= 0.55x1 + 0.55x2
x1 >= 0.25x1 + 0.25x2 + 0.25x3 + 0.25x4
x2 >= 0.30x1 + 0.30x2 + 0.30x3 + 0.30x4
z  <= 0.14x1 + 0.14x2 + 0.14x3 + 0.14x4

Luego deben ser llevadas las variables a la parte derecha de la igualdad, si es necesario se deja valor cero a la derecha quedando asi

x1 - 0.55x1 - 0.55x2 >= 0
x1 - 0.25x1 - 0.25x2 - 0.25x3 - 0.25x4 >= 0
x2 - 0.30x1 - 0.30x2 - 0.30x3 - 0.30x4 >= 0
z  - 0.14x1 - 0.14x2 - 0.14x3 - 0.14x4 <= 0

# Algoritmos de solución Programación entera

Es un problema donde se solicita o indica que la solución sea entera, este caso lo que busca son soluciones de tipo entero, una manera es utilizar el simplex conveciona, y redondear por valores que esten dentró del rango de valores solución

## Aproximación de variables
Se debe aproximar con cuidado ya que si se aproxima la solución a un vlaor entero puede que:
* Generar soluciones infactibles (que no satisfacen las restricciones)
* Generar soluciones factibles, pero no óptimas para el problema entero

La solución de la programación tienen un corte (una restricción aidicional) en el conjunto **S**.

# Algoritmos de generación de cortes

## Agregar restricciones
Se deben de agregar restricciones con caracteristicas especiales como:
* Deben eliminar la solución actual del problema relajado
* Se debe asegurar que no se eliminen soluciones enteras

Algunos algoritmos para generar corte sson
* Algoritmo de branch and bound
* Planos de corte de Gomory
* Branch and Cut
* Branch and Price

## Algoritmos de planos de corte
Parar generar un corte,
* Seleccionar una variable con **valor no entero** con restricción de integralidad. La estructura en el cuadro simplex siempre tiene la forma de

<img src="https://latex.codecogs.com/png.latex?\large&space;I*X_{B}&plus;(B^{-1}N)X_{N}=B^{-1}b" title="\large I*X_{B}+(B^{-1}N)X_{N}=B^{-1}b" />


<img src="https://latex.codecogs.com/png.latex?\large&space;X_{Bi}&plus;\sum_{j\epsilon&space;X_{N}}a_{ij}X_{j}=\bar{b}_{i}\rightarrow&space;No\&space;entero" title="\large X_{Bi}+\sum_{j\epsilon X_{N}}a_{ij}X_{j}=\bar{b}_{i}\rightarrow No\ entero" />

<img src="https://latex.codecogs.com/png.latex?\large&space;\rightarrow&space;\forall&space;a_{ij},\bar{b}_{i}" title="\large \rightarrow \forall a_{ij},\bar{b}_{i}" />

Descomponer en parte entera y parte fraccionaria

El resto del proceso se da en tablero  
![image](/images/clase&#32;opti&#32;14-09-2019&#32;1.jpeg)


# Ejemplo cortes de Gomory

Es en el excel

## Algoritmo Ramifiicación y acotamiento (Branch and bound)
Arbol de branch and bound

![image](/images/clase&#32;opti&#32;14-09-2019&#32;2.jpeg)

Programar el de branch and bound en python

Gap de dualidad  
(Duality Gap) -> Diferencia entre Mejor solución infactible (Dual)  
Mejor solución infactible (Dual)  
Mejor solución factible (Primal)  

https://github.com/he-chenchen/Integer-Linear-Programming/blob/master/ILP.pdf
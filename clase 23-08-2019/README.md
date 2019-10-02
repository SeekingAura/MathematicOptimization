# Método simplex

```
Max / Min < = c^t x  
s.a. Ax=b  
x>=0  
```

## Ejemplo con Wyndor Glass CO

### Función objetivo

Max z = 3x<sub>1</sub> + 5x<sub>2</sub>

### Evaluando con método grafico

<!---
https://www.codecogs.com/latex/eqneditor.php
--->

<!--- 
    x_{1} \leq 4 \rightarrow x_{1} = 4 \Rightarrow hiperplano
--->

<img src="https://latex.codecogs.com/png.latex?\large&space;x_{1}&space;\leq&space;4&space;\rightarrow&space;x_{1}&space;=&space;4&space;\Rightarrow&space;hiperplano" title="\large x_{1} \leq 4 \rightarrow x_{1} = 4 \Rightarrow hiperplano" />


Evaluando (x<sub>1</sub>=0, x<sub>2</sub>) -> ' <= 4

<!--- 
    \bar{v}g_{1}= \binom{\frac{\sigma g_{1}}{\sigma x_{1}}}{\frac{\sigma g_{2}}{\sigma x_{2}}} = \binom{1}{0} 
--->

![Ecuation](https://latex.codecogs.com/png.latex?\large&space;\bar{v}g_{1}=&space;\binom{\frac{\sigma&space;g_{1}}{\sigma&space;x_{1}}}{\frac{\sigma&space;g_{2}}{\sigma&space;x_{2}}}&space;=&space;\binom{1}{0})

El gradiente siempre apunta en la dirección de crecimiento

En el método grafico los vertices se forman por medio de las intersecciones de dos o más restricciones.

Las soluciones siempre se encuentran en los puntos ya sea maximizar o minimizar

2x<sub>2</sub><= 12 -> 2<sub>2</sub> = 12


El método simplex busca por medio de las intersecciones los puntos que sean factibles (que cumplan todas las restricciones) el mayor de todos de acuerdo a la función objetivo (reemplzando los valores obtenidos), cabe recordar que el método grafico es mas simple por meido de dos variables, ya que más variables se vuelve un problema complejo para resolver de dicho método.

Todas las posibles combinaciones de las restricciones son todas las soluciones posibles que tiene el modelo.



### Tratamiento de los datos para sistema de ecucaciones

Si la restricción tiene >= es multiplicado por menos 1, cada restriccion que tenga <= será agregado una variable de holgura.

Si la función es maximizar será multiplicada por -1

por ejemplo

z = 3X<sub>1</sub> + 5X<sub>2</sub>  
x<sub>1</sub><=4
2x<sub>2</sub> <= 12
3x<sub>1</sub> + 2x<sub>2</sub> <= 18

Convirtiendo

z -> -3x<sub>1</sub> - 5x<sub>2</sub> =0  
x<sub>1</sub>+x<sub>3</sub>=4  
2x<sub>2</sub>+<sub>4</sub>=12  
3<sub>1</sub>+2x<sub>2</sub>+x<sub>5</sub>=18


<img src="https://latex.codecogs.com/png.latex?\large&space;Max\&space;z&space;=&space;[c_{B}^{t}&space;c_{N}^{t}]\begin{bmatrix}&space;x_{B}\\x_{N}&space;\end{bmatrix}" title="\large Max\ z = [c_{B}^{t} c_{N}^{t}]\begin{bmatrix} x_{B}\\x_{N} \end{bmatrix}" />

**Método de dos fases**
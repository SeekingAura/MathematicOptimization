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

En el método grafico los vertices se forman por medio de las intersecciones por medio de la función y las restricciones.

Las soluciones siempre se encuentran en los puntos ya sea maximizar o minimizar
# Método de 2-Fases
el simplex requiere de una solucpon base la cual sea factible

|z|x<sub>B</sub>|x<sub>N</sub>|RHS|
|-|-            |-            |-  |
|1|0            |C<sub>B</sub>^(t)B^(-1)N-C<sub>N</sub>|C<sub>B</sub>^(t)B^(-1)b
|0|I            |B^(-1)N      |B^(-1)b|

En forma ideal -> X<sub>B</sub> iniciales tales que B=I. Se consigue al tener X<sub>B</sub> => Holguras

C<sub>B</sub>^t = 0 . . . 

```python
[ B^(-1)N = N
[ B^()b = b
```

Si no se consigue una matriz identidad "evidente", se construye artificialmente, agregando nuevas variables, las cuales serán retirados usando el criterio del cuadro simplex para tal efecto se agrega una función objetivo artificial

<img src="https://latex.codecogs.com/png.latex?\large&space;Min\&space;X_{0}=\sum_{i=1}^{m}x_{artificiales}" title="\large Min\ X_{0}=\sum_{i=1}^{m}x_{artificiales}" />

**Ejemplo:**

La estrategia que se aplica en este es muy similar a la de simplex visto anteriormente...

Solo que si los x_0 no llegan entonces debe borrarse

# Precio sombra
Son utilizados para resolver un problema dual... 

representa la tasa de cambio del valor óptimo ante una modificación marginal del lado derecho de una restricción. Se entiende por “marginal” aquella modificación que no cambia la geometría del problema, es decir, que la nueva solución óptima se puede encontrar a través de la resolución del sistema de ecuaciones al que da origen las restricciones activas originales (previa actualización del parámetro que estamos modificando).
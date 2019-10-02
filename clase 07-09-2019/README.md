* Considere el siguiente problema

```python
"""
Ejemplo 1
Minimize        z = 2x_1 +3x_2 + 2x_2

Subject to:     -x_1 -4x_2 -2x_3 = -8 -> Restriction 1
				-3x_1 -2x_2-2x_3+x_5=-6

				(360/3600)*(360/13)x_3 <= 620 -> Restriction 2
				
				x_1 >= 20	-> restriction 3
				x_2 >= 20	-> restriction 4
				x_3 >= 20	-> restriction 5

				Integrality
with              x_1 , x_2, x_3 >= 0
"""
```

El tema anterior de dos fases para un problema infactible y no optimo se puede aplicar un método de dos fases el cual utiliza variables de olgura adicional por cada <= que este tenga.

Si el problema inicial es infactible pero **óptimo** se puede implementar el método dual-Simplex

# Simplex dual
* La función objetivo es multiplicada por "-1" (en la matriz de inicio)
* Las restricciones se multiplican por "-1"
* Se escoje la variable que sale del problema es la que más afecta la factibilidad la cual parte del valor **RHS** para minimizar o maximizar el se elige de este el más negativo
* 


# Shadow price
https://stackoverflow.com/questions/50374255/efficiently-get-shadow-prices-in-scipy-linprog
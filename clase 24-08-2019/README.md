# Del ejercicio de la clase anterior
Max z = 16x<sub>1</sub> + 15x<sub>2</sub>  
s.a  40x<sub>1</sub>+31x<sub>2</sub>+**x<sub>3</sub>**=124  
-x<sub>1</sub>+x<sub>2</sub>+**x<sub>4</sub>**=1  
x<sub>1</sub>+**x<sub>5</sub>**=3

x<sub>1</sub>, x<sub>2</sub>, **x<sub>3</sub>**, **x<sub>4</sub>**, **x<sub>5</sub>** >=0
<!---
https://www.codecogs.com/latex/eqneditor.php
--->
Iteración 1:  
<img src="https://latex.codecogs.com/png.latex?\large&space;X_{B}=\{x_{3},&space;x_{4},&space;x_{5}\}&space;\&space;\&space;\&space;\&space;X_{N}=\{x_{1},&space;x_{2}\}" title="\large X_{B}=\{x_{3}, x_{4}, x_{5}\} \ \ \ \ X_{N}=\{x_{1}, x_{2}\}" />

---

<img src="https://latex.codecogs.com/png.latex?\large&space;B=\begin{bmatrix}&space;1&space;&&space;0&space;&&space;0\\&space;0&space;&&space;1&space;&&space;0\\&space;0&space;&&space;0&space;&&space;1&space;\end{bmatrix}&space;\&space;\&space;\&space;\&space;B^{-1}=\begin{bmatrix}&space;1&space;&&space;0&space;&&space;0\\&space;0&space;&&space;1&space;&&space;0\\&space;0&space;&&space;0&space;&&space;1&space;\end{bmatrix}" title="\large B=\begin{bmatrix} 1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1 \end{bmatrix} \ \ \ \ B^{-1}=\begin{bmatrix} 1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1 \end{bmatrix}" />

---

<img src="https://latex.codecogs.com/png.latex?\large&space;N=\begin{bmatrix}&space;40&space;&&space;31\\&space;-1&space;&&space;1\\&space;1&space;&&space;0&space;\end{bmatrix}&space;\&space;\&space;\&space;\&space;b=\begin{bmatrix}&space;124\\&space;1\\&space;3&space;\end{bmatrix}" title="\large N=\begin{bmatrix} 40 & 31\\ -1 & 1\\ 1 & 0 \end{bmatrix} \ \ \ \ b=\begin{bmatrix} 124\\ 1\\ 3 \end{bmatrix}" />

---

<img src="https://latex.codecogs.com/png.latex?\large&space;C_{B}=\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0&space;\end{bmatrix}&space;\&space;\&space;\&space;\&space;C_{N}=\begin{bmatrix}&space;16&space;&&space;15&space;\end{bmatrix}" title="\large C_{B}=\begin{bmatrix} 0 & 0 & 0 \end{bmatrix} \ \ \ \ C_{N}=\begin{bmatrix} 16 & 15 \end{bmatrix}" />

---

<img src="https://latex.codecogs.com/png.latex?\large&space;X_{N}=\begin{bmatrix}&space;x_{1}&space;\\&space;x_{2}&space;\end{bmatrix}&space;\&space;\&space;\&space;\&space;=\begin{bmatrix}&space;0&space;\\&space;0&space;\end{bmatrix}" title="\large X_{N}=\begin{bmatrix} x_{1} \\ x_{2} \end{bmatrix} \ \ \ \ =\begin{bmatrix} 0 \\ 0 \end{bmatrix}" />

---

<img src="https://latex.codecogs.com/png.latex?\large&space;X_{B}=B^{-1}b=\begin{bmatrix}&space;1&space;&&space;0&space;&&space;0\\&space;0&space;&&space;1&space;&&space;0\\&space;0&space;&&space;0&space;&&space;1&space;\end{bmatrix}&space;\begin{bmatrix}&space;124\\&space;1\\&space;3&space;\end{bmatrix}&space;=\begin{bmatrix}&space;124\\&space;1\\&space;3&space;\end{bmatrix}&space;\rightarrow&space;Factible" title="\large X_{B}=B^{-1}b=\begin{bmatrix} 1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 124\\ 1\\ 3 \end{bmatrix} =\begin{bmatrix} 124\\ 1\\ 3 \end{bmatrix} \rightarrow Factible" />

---

<img src="https://latex.codecogs.com/png.latex?\large&space;z_{0}=C_{B}^{t}B^{-1}b" title="\large z_{0}=C_{B}^{t}B^{-1}b" />

---
<img src="https://latex.codecogs.com/png.latex?\large&space;z=C_{B}^{t}B^{-1}b-\frac{C_{B}^{t}B^{-1}N-C_{N}^{t}}{C_{R}}X_{N}" title="\large z=C_{B}^{t}B^{-1}b-\frac{C_{B}^{t}B^{-1}N-C_{N}^{t}}{C_{R}}X_{N}" />

---

<img src="https://latex.codecogs.com/png.latex?\large&space;Z_{0}=\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0&space;\end{bmatrix}&space;\begin{bmatrix}&space;1&space;&&space;0&space;&&space;0\\&space;0&space;&&space;1&space;&&space;0\\&space;0&space;&&space;0&space;&&space;1&space;\end{bmatrix}&space;\begin{bmatrix}&space;124\\&space;1\\&space;3&space;\end{bmatrix}&space;=0" title="\large Z_{0}=\begin{bmatrix} 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 124\\ 1\\ 3 \end{bmatrix} =0" />

---

<img src="https://latex.codecogs.com/png.latex?\large&space;C_{R}^{t}=&space;\begin{pmatrix}&space;\begin{bmatrix}&space;0&space;&&space;0&space;&&space;0&space;\end{bmatrix}&space;\begin{bmatrix}&space;1&space;&&space;0&space;&&space;0\\&space;0&space;&&space;1&space;&&space;0\\&space;0&space;&&space;0&space;&&space;1&space;\end{bmatrix}&space;\begin{bmatrix}&space;40&space;&&space;31\\&space;-1&space;&&space;1\\&space;1&space;&&space;0&space;\end{bmatrix}&space;-&space;\begin{bmatrix}&space;16&space;&&space;15&space;\end{bmatrix}&space;\end{pmatrix}" title="\large C_{R}^{t}= \begin{pmatrix} \begin{bmatrix} 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 40 & 31\\ -1 & 1\\ 1 & 0 \end{bmatrix} - \begin{bmatrix} 16 & 15 \end{bmatrix} \end{pmatrix}" />

---

<img src="https://latex.codecogs.com/png.latex?\large&space;C_{t}^{R}=\begin{bmatrix}&space;-16&space;&&space;-15&space;\end{bmatrix}" title="\large C_{t}^{R}=\begin{bmatrix} -16 & -15 \end{bmatrix}" />

---

Se puede determinar cual variable es la más efectiva, se tienen varias formas una es evaluando por cada restricción obteniendo el valor de la variable teniendo en 0 las demas variables.

El resultado del proceos anterior CR_t es negativo ambos y eso indica que no es optimo y que debe hacerse cambio de ambos, el más negativo indica cual es la que más aporta (en este caso X_1)


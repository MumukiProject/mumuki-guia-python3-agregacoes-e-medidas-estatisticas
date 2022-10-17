Como quizás te estés imaginando, 0 y 1 son los valores más chicos y grandes que podemos pasarles a `quantile`, los cuales son también conocidos como <code>Q<sub>0</sub></code> y <code>Q<sub>4</sub></code> y se corresponden con el valor mínimo y máximo de una serie. 

Toda esta información de los 5 cuartiles puede ser condensada en un gráfico, llamado gráfico de caja :package:...

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-agregaciones-y-medidas-estadisticas/master/assets/boxplot_1665011408149.png" alt="boxplot_1665011408149.png" width="auto" height="auto">


... que nos muestra, justamente:

* <code>Q<sub>0</sub></code>: la primera línea a la izquierda, también llamada "bigote" 🥸
* <code>Q<sub>1</sub></code>: el extremo inferior de la caja  
* <code>Q<sub>2</sub></code>: el medio de la caja
* <code>Q<sub>3</sub></code>: el extremo superior de la caja
* <code>Q<sub>4</sub></code>: el último bigote, a la derecha

Por ejemplo, el gráfico anterior se corresponde con el diagrama de caja (o _boxplot_, en inglés) del siguiente `Series`...

```python
pd.Series([
  27, 30, 35, 35, 37, 37, 40, 41, 42, 43, 44, 45, 
  46, 46, 49, 49, 49, 49, 52, 53, 53, 53, 58, 62, 
  62
])
```

...cuyos 5 cuartiles son: 


* <code>Q<sub>0</sub></code>: 27
* <code>Q<sub>1</sub></code>: 40  
* <code>Q<sub>2</sub></code>: 46
* <code>Q<sub>3</sub></code>: 52
* <code>Q<sub>4</sub></code>: 62


> Teniendo esto en cuenta marcá cuáles de estas opciones son verdaderas.

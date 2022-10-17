Al hacer `describe` de nuestro `DataFrame` obtuvimos una tabla como esta:

||(..)|height|diameter|inclination|(..)|
|---|---|---|---|---|---|
|count|(..)|372699.000000|372699.000000|372699.000000|(..)|
|mean|(..)|8.473044|31.941234|3.069783|(..)|
|std|(..)|4.576818|20.207216|6.029910|(..)|
|min|(..)|0.000000|0.000000|0.000000|(..)|
|25%|(..)|5.000000|17.000000|0.000000|(..)|
|50%|(..)|8.000000|28.000000|0.000000|(..)|
|75%|(..)|11.000000|43.000000|5.000000|(..)|
|max|(..)|60.000000|426.000000|60.000000|(..)|

Expliquemos un poco de qué se trata cada una de estas filas:

* `count` es la cantidad de valores que tenemos dentro de esa columna;
* `mean` es el promedio de los valores de esa columna;
* `std` es el desvío estándar. En otras palabras, cuán lejos tienden a estar los valores del promedio;
* `min` es el menor valor que podemos encontrar en la columna;
* `25%` es el valor de Q1;
* `50%` es el valor de Q2;
* `75%` es el valor de Q3;
* `max` es el mayor valor que podemos encontrar en la columna.

También habrás notado que `describe` nos muestra sólo información sobre las columnas numéricas de nuestro lote de datos. Sin embargo, es importante notar que aunque la columna sea numérica no siempre tiene sentido obtener medidas estadísticas. Probablemente no nos interese el promedio de los códigos postales o la mediana de los ids. 

Otra herramienta que nos permite obtener otro tipo de información sobre nuestros datos es `info`. A diferencia de `describe`, con `info` podemos conocer sobre la estructura de nuestro `DataFrame` como por ejemplo la cantidad de columnas, de qué tipo de datos son, cuántos valores tenemos en cada una.

> Probá en tu cuaderno `arboles.info()` y acompañanos al siguiente ejercicio.

La _moda_ es otra medida estadística, sólo que no tan popular como las anteriores 😛. Ésta se calcula mediante `mode` y  representa cuál es el valor que más se repite dentro de un `Series`. Por ejemplo, si tuviéramos una columna con los valores `48 5 48 5 6 7 9 3 12 45 48 42 48`, su moda sería `48`, dado que es el valor más frecuente, con 4 apariciones.

Pero, ¿qué sucedería en una columna con los valores `1 1 4 8 9 1 4 8 9 8`? ¿Sería `1` u `8`? 🤔

> ¡Averigüémoslo! Creá en tu cuaderno un `Series` con los valores anteriores….
>
> ```python
> # así se puede convertir una lista en un Series
> unos_numeros = pd.Series([1, 1, 4, 8, 9, 1, 4, 8, 9, 8])
> ```
> 
> y calculá su moda haciendo `unos_numeros.mode()`. ¿Cuál es su moda?

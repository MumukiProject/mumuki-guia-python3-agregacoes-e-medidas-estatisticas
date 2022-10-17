Cómo podemos notar, `mode` no devuelve un valor _escalar_ (es decir, un valor único y sencillo como un número o un booleano) sino un `Series` 🙊. `

```python
ム type(unos_numeros)
pandas.core.series.Series
```

Esto sucede porque siempre podríamos tener más de un valor que sea el más frecuente: 

```python
ム pd.Series([1, 2, 3, 2, 4, 2]).mode()
0    2
dtype: int64
ム pd.Series(["kung", "fu", "pandas"]).mode()
0        fu
1      kung
2    pandas
dtype: object
```
 
 



También es importante destacar que un valor puede ser el más frecuente y aún así no ser el promedio ‼️. Por ejemplo, si tenemos una columna con los valores `1 1 1 1 2000 3000` su moda es `1` pero su promedio es `836`.

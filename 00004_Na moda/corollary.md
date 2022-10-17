Como podemos notar, `mode` não retorna um valor _escalar_ (ou seja, um valor único e simples como um número ou um booleano) mas retorna um `Series` 🙊. `

```python
ム type(uns_números)
pandas.core.series.Series
```

Isso acontece porque sempre poderíamos ter mais de um valor que seja o mais frequente:


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

Também é importante destacar que um valor pode ser o mais frequente e ainda não ser a média ‼️️. Por exemplo, se temos uma coluna com os valores `1 1 1 1 2000 3000` a moda dela é `1` mas a média é `836`.

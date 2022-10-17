Eh, ¡momento! Hasta ahora vimos como obtener los mayores y menores valores de una columna, pero ¿cómo obtenemos a la fila con ese mayor o menor valor?

Para eso existe `idxmax` e `idxmin`, que nos dirán el _índice_ de la fila que cumpla esa condición: 

```python
# nos devuelve el índice de la (primera) fila que hace máxima a "columna" 
tabla["columna"].idxmax()
```

¿Qué operación que vimos anteriormente podremos utilizar ahora para obtener esa fila y sus valores? :thinking: Recordá que por defecto el índice (la primera columna, sin título) coincide con la posición de cada fila :wink: 

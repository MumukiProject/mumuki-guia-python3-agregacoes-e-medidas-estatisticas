Al trabajar con columnas numéricas muchas veces nos interesa saber cuál es el menor o mayor valor que puede tomar. 

Por ejemplo, si tuviésemos un dataset `personas` y quisiéramos obtener la edad de la persona más joven podríamos hacer `personas["edad"].min()`. Si en cambio, buscamos el valor más alto podríamos hacer `personas["edad"].max()`. 

> ¡Probémoslo! [Acá](https://github.com/MumukiProject/datasets/raw/master/arbolado-publico-lineal.csv) vas a encontrar un lote de datos con los árboles de la Ciudad de Buenos Aires 🌳. Cargalo en un nuevo cuaderno y usando lo visto hasta ahora, respondé: ¿cuál es la altura del árbol más grande?
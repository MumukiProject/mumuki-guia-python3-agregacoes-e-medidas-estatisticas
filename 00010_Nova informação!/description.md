:newspaper: Fazendo `describe` do nosso `DataFrame` obtivemos uma tabela assim:

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

Vamos explicar um pouco do que se trata cada uma dessas linhas:

* `count` é o número de valores que temos dentro dessa coluna;
* `mean` é a média dos valores dessa coluna;
* `std` é o desvio padrão. Em outras palavras, até que ponto os valores tendem a estar da média;
* `min` é o menor valor que podemos encontrar na coluna;
* `25%` é o valor de Q1;
* `50%` é o valor de Q2;
* `75%` é o valor de Q3;
* `max` é o maior valor que podemos encontrar na coluna.

Você também deve ter notado que `describe` mostra apenas informações sobre as colunas numéricas do nosso lote de dados. No entanto, é importante notar que mesmo que a coluna seja numérica, nem sempre faz sentido obter medidas estatísticas. Provavelmente não daremos importância para a média dos códigos postais ou a mediana dos ids’s. 

Outra ferramenta para obter outros tipos de informações sobre nossos dados é `info`. Ao contrário do `describe`, com `info` podemos conhecer sobre a estrutura do nosso `DataFrame`, como por exemplo a quantidade de colunas, que tipo de dados são, quantos valores temos em cada uma.


> Tente no seu caderno `arvores.info()`.

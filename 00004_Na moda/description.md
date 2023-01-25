A _moda_ é outra medida estatística, mas não tão popular quanto as anteriores 😛. Ela é calculada por `mode` e representa qual é o valor que mais se repete dentro de uma `Series`. Por exemplo, se tivéssemos uma coluna com os valores `48 5 48 5 6 7 9 3 12 45 48 42 48`, a moda dela seria `48`, pois é o valor mais frequente, com 4 ocorrências.

Mas o que aconteceria com uma coluna com os valores `1 1 4 8 9 1 4 8 9 8`? Seria 1 ou 8? 🤔

> Vamos investigar! Crie no seu caderno uma `Series` com os valores anteriores….
>
> ```python
> # assim é possível transformar uma lista em uma Series
> uns_numeros = pd.Series([1, 1, 4, 8, 9, 1, 4, 8, 9, 8])
> ```
> 
> e calcule a moda fazendo `uns_números.mode()`. Qual é a moda?

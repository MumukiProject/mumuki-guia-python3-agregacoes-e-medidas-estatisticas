Ao trabalhar com colunas numéricas, muitas vezes estamos interessados em saber qual é o menor ou o maior valor que ela pode assumir.

Por exemplo, se tivéssemos um dataset `pessoas` e quiséssemos obter a idade da pessoa mais jovem, poderíamos fazer `pessoas["idade"].min()`. Se, em vez disso, procurarmos o valor mais alto, poderíamos fazer  `pessoas["idade"].max()`. 

> Vamos testar! [Aqui](https://github.com/MumukiProject/datasets/raw/master/arbolado-publico-lineal.csv) você vai encontrar um lote de dados com as árvores da Cidade de Buenos Aires 🌳. Carregue em um novo caderno e usando o que vimos até agora, responda: qual é a altura (`height`) da árvore maior?
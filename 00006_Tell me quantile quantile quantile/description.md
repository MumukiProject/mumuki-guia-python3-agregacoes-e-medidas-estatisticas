No exercício anterior aprendemos sobre a mediana, que nos permite saber o valor do meio de uma coluna levando em consideração os elementos ordenados. Esse conceito pode ser extrapolado para a ideia de quantis. 😮

O quantil me diz qual é o maior elemento de um subconjunto de elementos menores. Vamos explicar com um exemplo para melhor compreensão!

Se fizéssemos...

```python
ム arvores["diameter"].quantile(0.95)
71.0
```

... obteríamos o maior diâmetro dentro de um 95% das menores. Dito de outra forma, se removermos os 5% "maiores diâmeros" das árvores, o maior diâmetro que nos resta é 71.0.
 

> Experimente! Obtenha a altura da árvore mais alta dentro dos 80% mais baixos.

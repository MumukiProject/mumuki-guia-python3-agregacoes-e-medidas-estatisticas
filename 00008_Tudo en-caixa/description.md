Como você deve estar imaginando, 0 e 1 são os menores e maiores valores que podemos passar para `quantil`, que também são conhecidos como <code>Q<sub>0</sub></code> e <code>Q<sub>4</sub></code>e correspondem ao valor mínimo e máximo de uma série.

Todas essas informações dos 5 quartis podem ser condensadas em um gráfico, chamado de gráfico de caixa...

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-agregaciones-y-medidas-estadisticas/master/assets/boxplot_1665011408149.png" alt="boxplot_1665011408149.png" width="auto" height="auto">


... que nos mostra exatamente:

* <code>Q<sub>0</sub></code>: a primeira linha à esquerda, também chamada de "bigode" 🥸
* <code>Q<sub>1</sub></code>: a extremidade inferior da caixa  
* <code>Q<sub>2</sub></code>: o meio da caixa
* <code>Q<sub>3</sub></code>: a extremidade superior da caixa
* <code>Q<sub>4</sub></code>: o último bigode, à direita

Por exemplo, o gráfico anterior corresponde ao diagrama de caixa (ou _boxplot_, em inglês) do seguinte `Series`...

```python
pd.Series([
  27, 30, 35, 35, 37, 37, 40, 41, 42, 43, 44, 45,
  46, 46, 49, 49, 49, 49, 52, 53, 53, 53, 58, 62,
  62
])
```

...cujos 5 quartis são:


* <code>Q<sub>0</sub></code>: 27
* <code>Q<sub>1</sub></code>: 40  
* <code>Q<sub>2</sub></code>: 46
* <code>Q<sub>3</sub></code>: 52
* <code>Q<sub>4</sub></code>: 62


> Tendo isso em mente, marque quais dessas opções são verdadeiras.

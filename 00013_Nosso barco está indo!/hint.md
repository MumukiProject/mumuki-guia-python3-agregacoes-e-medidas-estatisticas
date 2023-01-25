Um momento! Até agora vimos como obter os maiores e menores valores de uma coluna, mas como obtemos a linha com esse maior e menor valor?

Para isso existe `idxmax` e `idxmin`, que nos informarão o _index_ da linha que atenda a essa condição:

```python
# retorna o índice da (primeira) linha com o valor máximo da "coluna".
tabela["coluna"].idxmax()
```

Qual a operação que vimos anteriormente podemos usar agora para obter essa linha e seus valores?  :thinking: Lembre-se que por padrão, o índice (a primeira coluna, sem título) coincide com a posição de cada linha :wink:

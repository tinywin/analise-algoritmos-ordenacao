# Análise de Algoritmos de Ordenação

Este projeto foi desenvolvido para a disciplina de Projeto e Análise de Algoritmos (PAA) do curso de Ciência da Computação. O objetivo é comparar diferentes algoritmos de ordenação quanto ao tempo de execução, número de comparações e número de trocas.

## Algoritmos Implementados

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort

## Métricas Avaliadas

Para cada algoritmo e tipo de entrada, são avaliadas:

- **Tempo de execução (ms)**
- **Número de comparações**
- **Número de trocas**

## Tipos de Entrada

Os algoritmos são testados com vetores de tamanho 100.000 nas seguintes condições:

- **Ordenado (`sorted`)**
- **Reverso (`reversed`)**
- **Aleatório (`random`)**

## Como Executar

1. Certifique-se de ter Python 3 instalado.
2. Baixe o arquivo [`testes_ordenacao.py`](testes_ordenacao.py).
3. Execute o script em um terminal com o comando:

```bash
python testes_ordenacao.py
```
O programa imprimirá os resultados no terminal para cada combinação de algoritmo e tipo de entrada.

## Observações

O Quick Sort usa partição aleatória.

O Merge Sort retorna uma nova lista ordenada, enquanto os demais ordenam in-place.

O limite de recursão foi aumentado para evitar RecursionError em entradas grandes.

## Autor

Projeto acadêmico da disciplina de Projeto e Análise de Algoritmos – Ciência da Computação por Laura Barbosa Henrique.

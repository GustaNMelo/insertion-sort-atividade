# Insertion Sort em Python — Versão Original e Otimizada

Este repositório contém a implementação do algoritmo de ordenação **Insertion Sort**, com:

- ✅ Versão original do algoritmo  
- 🚀 Versão otimizada que interrompe a execução se nenhuma troca for realizada em uma iteração  
- 📊 Comparação de desempenho entre ambas as versões  
- 🧪 Testes com listas ordenadas, invertidas e aleatórias  
- ⏱️ Medição de tempo e número de iterações usando a biblioteca `time`  

---

## 📌 Objetivo

Implementar o algoritmo **Insertion Sort** para ordenar listas de inteiros em ordem crescente, exibindo o estado da lista a cada iteração, destacando as trocas realizadas e comparando a eficiência entre a versão padrão e uma versão otimizada.

---

## 🧠 Como funciona o Insertion Sort

O algoritmo percorre a lista da esquerda para a direita, inserindo cada elemento na posição correta em relação aos elementos anteriores.

### Exemplo de comportamento (versão original):

```
Entrada:
4 3 2 1

Saída:
Versão original do Insertion Sort:
Iteração 1: [3, 4, 2, 1] (Inseriu 3)
Iteração 2: [2, 3, 4, 1] (Inseriu 2)
Iteração 3: [1, 2, 3, 4] (Inseriu 1)
Lista ordenada (original): [1, 2, 3, 4]

==================================================

Versão otimizada do Insertion Sort:
Iteração 1: [3, 4, 2, 1] (Inseriu 3)
Iteração 2: [2, 3, 4, 1] (Inseriu 2)
Iteração 3: [1, 2, 3, 4] (Inseriu 1)
Lista ordenada (otimizada): [1, 2, 3, 4]

Comparação de desempenho:
Versão original - Iterações: 3, Tempo: 0.000012 segundos
Versão otimizada - Iterações: 3, Tempo: 0.000009 segundos
```

---

## ⚙️ Execução

### 🔹 Requisitos

- Python 3.x

### 🔹 Como rodar

```bash
python insertion_sort.py
```

Digite uma lista de números inteiros separados por espaço quando solicitado.

---

## 📄 Estrutura do Código

### Funções principais:

- `insertion_sort(lista)`: versão tradicional  
- `insertion_sort_otimizado(lista)`: interrompe se não houver trocas na iteração  
- `medir_tempo(funcao, lista)`: mede tempo de execução e número de iterações  
- `main()`: executa o programa com entrada do usuário e exibe os resultados  

---

## 🚀 Otimização

Na versão otimizada, o algoritmo interrompe a ordenação caso perceba que a lista já está ordenada antes do final do processo. Isso reduz o número de iterações e melhora o desempenho em listas já ordenadas.

---

## 📊 Testes e Resultados

Foram realizados testes com listas de diferentes tipos:

### 1. Lista já ordenada (`[1, 2, 3, 4, 5]`)

| Versão         | Iterações | Tempo (s)        |
|----------------|-----------|------------------|
| Original       | 4         | 0.000010         |
| Otimizada      | 1         | 0.000006 (💡)    |

### 2. Lista invertida (`[5, 4, 3, 2, 1]`)

| Versão         | Iterações | Tempo (s)        |
|----------------|-----------|------------------|
| Original       | 4         | 0.000012         |
| Otimizada      | 4         | 0.000011         |

### 3. Lista aleatória (`[3, 1, 4, 2, 5]`)

| Versão         | Iterações | Tempo (s)        |
|----------------|-----------|------------------|
| Original       | 4         | 0.000013         |
| Otimizada      | 4         | 0.000011         |

💡 *Em listas ordenadas, a otimização evita iterações desnecessárias, melhorando o desempenho.*

---

## 🧪 Sugestão de Testes

Você pode também gerar listas automaticamente para testes maiores:

```python
def gerar_lista_ordenada(tamanho):
    return list(range(tamanho))

def gerar_lista_invertida(tamanho):
    return list(range(tamanho, 0, -1))

def gerar_lista_aleatoria(tamanho):
    import random
    return random.sample(range(tamanho * 2), tamanho)
```

---

## 📁 Arquivos

- `insertion_sort.py`: código principal  
- `README.md`: este documento  
- (Opcional) Prints de execução salvos em `/prints/`  

---

## 📝 Conclusão

A versão otimizada do Insertion Sort oferece ganhos reais de desempenho para listas já ordenadas, diminuindo o número de iterações e o tempo de execução. A modularização e a análise prática ajudam a compreender como otimizações simples podem trazer resultados significativos.

---

## 🧑‍💻 Autor

Gustavo Nunes Melo

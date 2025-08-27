import time
import random

def insertion_sort(lista):
    print("Versão original do Insertion Sort:")
    iteracoes = 0
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        trocou = False
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
            trocou = True
        lista[j + 1] = chave
        iteracoes += 1
        if trocou:
            print(f'Iteração {iteracoes}: {lista} (Inseriu {chave})')
        else:
            print(f'Iteração {iteracoes}: {lista} (Sem troca)')
    return iteracoes

def insertion_sort_otimizado(lista):
    print("Versão otimizada do Insertion Sort:")
    iteracoes = 0
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        trocou = False
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
            trocou = True
        lista[j + 1] = chave
        iteracoes += 1
        if trocou:
            print(f'Iteração {iteracoes}: {lista} (Inseriu {chave})')
        else:
            print(f'Iteração {iteracoes}: {lista} (Sem troca - parada antecipada)')
            break  # Otimização: interrompe se nenhuma troca foi feita
    return iteracoes

def medir_tempo(funcao, lista):
    inicio = time.time()
    iteracoes = funcao(lista)
    fim = time.time()
    return iteracoes, fim - inicio

def main():
    entrada = input("Digite uma lista de números separados por espaço: ")
    original = list(map(int, entrada.split()))
    print("Lista original: ", original)

    lista1 = original.copy()
    iter1, tempo1 = medir_tempo(insertion_sort, lista1)
    print("Lista ordenada (original):", lista1)

    print("\n" + "="*50 + "\n")

    lista2 = original.copy()
    iter2, tempo2 = medir_tempo(insertion_sort_otimizado, lista2)
    print("Lista ordenada (otimizada):", lista2)

    print("\nComparação de desempenho:")
    print(f"Versão original - Iterações: {iter1}, Tempo: {tempo1:.6f} segundos")
    print(f"Versão otimizada - Iterações: {iter2}, Tempo: {tempo2:.6f} segundos")

if __name__ == "__main__":
    main()

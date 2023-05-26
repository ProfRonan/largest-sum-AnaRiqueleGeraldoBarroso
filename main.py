"""Module with functions."""

import heapq
def largest_sum(numbers: list[int]) -> tuple[int, int]:
    """Encontra e retorna os dois números que somados dão o maior valor."""
    if len(numbers) < 2:
        return None
    
    primeiro =max(numbers)  # o primeiro número da soma
    segundo = heapq.nlargest(2, numbers)[-1]  # o segundo número da soma
    return segundo, primeiro

if __name__ == "__main__":
    lista = largest_sum([-10, -5, -2, -1])
    print(lista)
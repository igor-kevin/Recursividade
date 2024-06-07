def fibonnachi_recursivo(numero: int):
    if numero == 1:
        return 1
    if numero == 0:
        return 1
    return (fibonnachi_recursivo(numero-2) + fibonnachi_recursivo(numero-1))


if __name__ == "__main__":
    for i in range(30):
        print("O fibonnachi de ", i, "é: ", fibonnachi_recursivo(i))

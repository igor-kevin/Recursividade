def fatorial(numero: int):
    if numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)


if __name__ == "__main__":
    print(fatorial(30))

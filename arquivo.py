# informe o número que deseja verificar
num = int(input("Informe um número: "))

# inicializa as duas primeiras posições da sequência
fib1 = 0
fib2 = 1
i = 0

# calcula a sequência de Fibonacci
while fib2 < num:
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    i += 1

# verifica se o número informado pertence à sequência
if fib2 == num:
    print(f"{num} pertence à sequência de Fibonacci na posição {i+3}")
else:
    print(f"{num} não pertence à sequência de Fibonacci")
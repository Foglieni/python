# informe a string que deseja inverter
string = "Exemplo de string"

# converte a string em uma lista de caracteres
lista_caracteres = list(string)

# inverte a lista de caracteres
for i in range(len(lista_caracteres) // 2):
    lista_caracteres[i], lista_caracteres[-i-1] = lista_caracteres[-i-1]
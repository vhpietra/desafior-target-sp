def transforma_em_string(palavra):
    lista = []
    lista[:0]=palavra
    lista_inversa = lista[::-1]
    print(lista_inversa)

palavra = str(input("Digite uma palavra: "))
transforma_em_string(palavra)

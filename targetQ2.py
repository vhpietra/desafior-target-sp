numero = int(input("Digite o número que deseja consultar: "))

lista = []
def sequencia_de_fibonacci(n):
    a=0
    b=1
    lista.append(a)
    for i in range(n-3):
        total = a + b
        b=a
        a= total
        lista.append(total)

    if numero in lista:
        print("O número digitado pertence a sequência de fibonacci")
    else:
        print("O número digitado não pertence a sequência de fibonacci")
         
sequencia_de_fibonacci(100)
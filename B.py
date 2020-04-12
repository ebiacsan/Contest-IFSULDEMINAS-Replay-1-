qtdRepeticoes = int(input())
for i in range(qtdRepeticoes):
    listaCaracteres = list(input())
    vet = ['Q','J','K','A']
    try:
        for i in vet:
            index = listaCaracteres.index(i)
            listaCaracteres = listaCaracteres[index:]
        print("Agora vai")
    except ValueError:
        print("Agora apertou sem abracar")

equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("equipamentos:"))
    valores.append(float(input("valor: ")))
    seriais.append(int(input("Número serial:")))
    departamentos.append(input("Departamento:"))
    resposta= input("Digite \"s\" para continuar:  ").upper()


for indice in range(0, len(equipamentos)):
    print("\nEquipamentos...:", (indice + 1))
    print("nome.............:", equipamentos[indice])
    print("valor............:", valores[indice])
    print("serial...........:", seriais[indice])
    print("departamento.....:", departamentos[indice])

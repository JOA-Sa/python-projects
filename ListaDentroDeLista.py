from typing import Tuple
inventario=[]
resposta = "S"
while == "S"
    equipamento=(input("equipam  to:"),
                 float(input("Valor:")),
                 int(input("numero serial:")),
               input("Departamento:"))
    inventario.append(equipamento)
    resposta=input("Digite\"s\" para continuar:").upper()

for elemento in inventario:
    print("Nome.........:",elemento[0])
    print("Valor........:",elemento[1])
    print("Serial.......:",elemento[2])
    print("Departamento.:",elemento[3])

busca=input("\nDigite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca==elemento[0]:
        print("valor..:", elemento[1])
        print("Serial.:",elemento[1])

depreciacao=input("\nDigite o nome do equipamento que será depereciado:")
for elemento in inventario:
    if depreciacao==elemento[0]:
        print("Valor antigo:", elemento [1])
        elemento[1] = elemento[1]  * 0.9
        print("Novo Valor:", elemento[1])

serial=int(input("\nDigite o Serial do equipamento que será excluido:"))
for elemento in inventario:
      Valores.append(elemento[1])
if len (valores)>0:
    print("O equipamento mais caro custa:", max(valores))
    print("O equipamento mais barato custa:",min(Valores))
    print("O total de equipamentos é de:",sum(valores))

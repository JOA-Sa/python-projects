equipment = []
values = []
serials = []
department = []
answers = "y"
while resposta == "y":
    equipment.append(input("Equipment:"))
    values.append(float(input("Value:")))
    serials.append(int(input("Number serial:")))
    department.append(input("Department:"))
    answers = input("Type \"Y\" to continue:").upper()

search = input("\nEnter the name of the equpment you want to search:")
for indice in range(0, len(equipment)):
    if search == equipment[indice]:
        print("Value..:", values[indice])
        print("Serials.:", serials[indice])

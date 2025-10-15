n1=()
n2=()
n3=()
n1 = int (input("Introduza um numero: "))
n2 = int (input("Introduza um numero: "))
n3 = int (input("Introduza um numero: "))
#----------------------------------------
if n1>n2>n3:
    print("Maior numero:",n1)
    #----------------------------------------
    if n2>n3:
        print("Numero do meio:",n2)
        print("Menor numero:",n3)
    else:
        print("Numero do meio:",n3)
        print("Menor numero:",n2)
    #----------------------------------------
#----------------------------------------
elif n2>n1>n3:
    print("Maior numero:",n2)
    #----------------------------------------
    if n1>n3:
        print("Numero do meio:",n1)
        print("Menor numero:",n3)
    else:
        print("Numero do meio:",n3)
        print("Menor numero:",n1)
    #----------------------------------------
#----------------------------------------
else:
    print("Maior numero:",n3)
    #----------------------------------------
    if n2>n1:
        print("Numero do meio:",n2)
        print("Menor numero:",n1)
    else:
        print("Numero do meio:",n1)
        print("Menor numero:",n2)
    #----------------------------------------
#----------------------------------------
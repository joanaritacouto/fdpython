#MAIN:

# The list of contacts (it's actually a dictionary!):
contactos = {"234370200": "Universidade de Aveiro",
    "727392822": "Cristiano Aveiro",
    "387719992": "Maria Matos",
    "887555987": "Marta Maia",
    "876111333": "Carlos Martins",
    "433162999": "Ana Bacalhau"
    }


def AdicionarContacto(contactos):

    contactos[num]= nome

    return contactos

def RemoverContacto(contactos):

    del contactos[num]
    return contactos
    
def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def numberToName(contactos):
    if num in contactos:
        print (contactos[num])
    else:
        print (num)    

    

def filterPartName(contactos, PartName):
    d={}
    for num in contactos.keys():
        nome = contactos[num]

        if PartName in nome:
      
            d[num]=nome

    print (d)

 

op = ""
def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op

while op != "T":
    op = menu()
    if op == "T":
        print("Fim")

    elif op == "L":
        print("Contactos:")
        listContacts(contactos)

    elif op == "A":
        nome = input('Nome do novo contacto: ')
        num = input ('Núemro do contacto: ')
        AdicionarContacto(contactos)

    elif op == "R":
        num = input('Número a remover: ')
        RemoverContacto(contactos)

    elif op == "N":
        num = input ('Número: ')
        numberToName(contactos)

    elif op == "P":
        PartNome = input ('Parte do nome: ')
        filterPartName(contactos, PartNome)  

                 
           
    else:
        print("Não implementado!")













    

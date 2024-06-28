def menu ():
    menu = """1)Registrar Alumno
2)Listado de alumnos
3)Buscar alumnos por nivel
4)Calcular nota del promedio de alumnos
5)salir
""" 
    print(menu, end ="")


notas = []
nota = 0
cant_notas=0

def op_selec():
    while True:
        try:
            opc = int(input())
            return opc

            if opc>0 or opc<6:
                return opc
            else:
                print("Ingrese una opción valida")
        except ValueError:
            print("Ingrese un valor correspondiente")

def agregar_alumno():
    rut = input("Ingrese el rut del alumno")
    nom = input("Ingrese el nombre del alumno")
    ape = input("Ingrese el apellido del alumno")
    curso = input("Ingrese el curso del alumno")
    
    nota = float(input("Ingrese las notas"))
    cant_notas = 0
    while cant_notas == 5:
        cant_notas +=1
        notas.append(notas)
    
            

    libro = {"rut":rut,"nombre":nom,"apellido":ape,"curso":curso}
    return libro

def promedio():
    sum(notas)

    
            

def lista_alumnos(lista):
    for i in range(len(lista)):
        print(f"Alumno{i+1}: ")
        print(f"Nombre{lista[i]["nombre"]}")
        print(f"Apellido{lista[i]["apellido"]}")
        print(f"Curso{lista[i]["curso"]}")
        print(f"Promedio Final {sum(notas)}")
        print("---------------------------------------------")

def encontrar_alumno(lista):
    alu = input("Ingrese el Rut del alumno: ")
    encontrado = False

    for i in range(len(lista)):
        alu == lista[i]["rut"]
        libro = lista[i]
        encontrado = True

    if encontrado:
        print(f"Alumno{i+1}: ")
        print(f"Nombre{libro["nombre"]}")
        print(f"Apellido{libro["apellido"]}")
        print(f"Curso{libro["curso"]}")
    else:
        print("Alumno no encontrado")

def archivo(lista):
    with open("archi.txt","w")as archivo:
        for i in range(lista):
            libro = i["alumno"]+", "+i["nombre"]+", "+ i["apellido"]+", "+i["curso"]+"\n"
        archivo.write(libro)








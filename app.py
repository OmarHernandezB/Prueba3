import func

op = 0
alumnos = []

while op != 5:

    func.menu()
    op = func.op_selec()
    
    if op == 1:
        alumnos.append(func.agregar_alumno())
    elif op == 2:
        func.lista_alumnos(alumnos)
    elif op == 3:
        func.encontrar_alumno(alumnos)
    elif op == 4:
        func.promedio()

func.archivo(alumnos)
      


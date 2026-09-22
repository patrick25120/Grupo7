from paciente import Paciente 
from medico import Medico 
from buscarcodigo import Buscar_codigo 
from cita import Progama_cita 
from registro import Atencion 

def main():

    print("=== REGISTRO DE PACIENTE ===")

    codigo_paciente = input("Ingrese el código del paciente: ")
    nombre_paciente = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad: "))
    dni = input("Ingrese el DNI: ")

    paciente = Paciente(
        codigo_paciente,
        nombre_paciente,
        edad
    )

    print("\nPaciente registrado:")
    print(paciente.resumen())


    print("\n=== REGISTRO DE MÉDICO ===")

    print("1. Sebastian Quispe - Pediatria")
    print("2. Renata Valdez - Clinico")
    print("3. Carlos Ruiz - Nutricion")
    print("4. Maria Torres - Dentista")
    print("5. Luis Garcia - Obstetricia")

    opcion = int(input("Ingrese el número del médico: "))

    match opcion:
        case 1:
            medico = Medico("M001", "Sebastian Quispe", "Pediatria")
        case 2:
            medico = Medico("M002", "Renata Valdez", "Clinico")
        case 3:
            medico = Medico("M003", "Carlos Ruiz", "Nutricion")
        case 4:
            medico = Medico("M004", "Maria Torres", "Dentista")
        case 5:
            medico = Medico("M005", "Luis Garcia", "Obstetricia")
        case _:
            print("Opción no válida.")
            return

    print("\nMédico registrado:")
    print(medico.resumen())


    print("\n=== BUSCAR POR CÓDIGO ===")

    buscar = Buscar_codigo(
        medico.codigo,
        medico
    )

    codigo_buscar = input("Ingrese el código del médico a buscar: ")

    resultado = buscar.buscar(codigo_buscar)

    if resultado != None:
        print("Médico encontrado:")
        print(resultado.resumen())
    else:
        print("Código no encontrado.")


    print("\n=== PROGRAMAR CITA ===")

    codigo_cita = input("Ingrese el código de la cita: ")
    fecha = input("Ingrese la fecha de la cita: ")

    cita = Progama_cita(
        codigo_cita,
        paciente.nombre,
        medico.nombre,
        fecha
    )

    print("\nCita registrada:")
    print(cita.resumen())


    print("\n=== REGISTRAR ATENCIÓN ===")

    atencion = Atencion(
        paciente.nombre,
        dni,
        paciente.codigo,
        medico.especialidad,
        medico.codigo
    )

    historial = []
    historial.append(atencion)

    print("Atención añadida al historial.")


    print("\n===================================")
    print("          CITA REGISTRADA")
    print("===================================")
    print("Código de cita:", cita.codigo)
    print("Paciente:", paciente.nombre)
    print("DNI:", dni)
    print("Edad:", paciente.edad)
    print("Médico:", medico.nombre)
    print("Código médico:", medico.codigo)
    print("Especialidad:", medico.especialidad)
    print("Fecha:", cita.fecha)
    print("===================================")


if __name__ == "__main__":
    main()
    
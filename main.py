from paciente import Paciente
from medico import Medico
from buscarcodigo import Buscar_codigo
from cita import Progama_cita
from registro import Atencion


def main():

    pacientes = []
    medicos = []
    citas = []
    historial = []

    print("\n===================================")
    print("       SISTEMA DE ATENCIÓN")
    print("===================================")
    print("1. Registrar paciente")
    print("2. Registrar médico")
    print("3. Buscar médico por código")
    print("4. Programar cita")
    print("5. Registrar atención")
    print("6. Salir")
    print("===================================")

    opcion_menu = input("Seleccione una opción: ")

    
    if opcion_menu == "1":

        while True:

            print("\n=== REGISTRO DE PACIENTE ===")

            codigo_paciente = input(
                "Ingrese el código del paciente: "
            )

            duplicado = False

            for p in pacientes:
                if p.codigo == codigo_paciente:
                    duplicado = True

            if duplicado:
                print("Error: el código ya está registrado.")
                nuevamente = input(
                    "¿Desea ingresar nuevamente el código? (s/n): "
                )

                if nuevamente.lower() == "s":
                    continue
                else:
                    break

            nombre_paciente = input(
                "Ingrese el nombre del paciente: "
            )

            edad_texto = input(
                "Ingrese la edad: "
            )

            if not edad_texto.isdigit():
                print("Error: la edad debe ser numérica.")
                nuevamente = input(
                    "¿Desea ingresar nuevamente los datos? (s/n): "
                )

                if nuevamente.lower() == "s":
                    continue
                else:
                    break

            edad = int(edad_texto)

            if edad < 0 or edad > 120:
                print("Error: la edad debe estar entre 0 y 120.")
                nuevamente = input(
                    "¿Desea ingresar nuevamente los datos? (s/n): "
                )

                if nuevamente.lower() == "s":
                    continue
                else:
                    break

            paciente = Paciente(
                codigo_paciente,
                nombre_paciente,
                edad
            )

            pacientes.append(paciente)

            print("\nPaciente registrado correctamente.")
            print(paciente.resumen())
            break

    
    elif opcion_menu == "2":

        while True:

            print("\n=== REGISTRO DE MÉDICO ===")
            print("1. Sebastian Quispe - Pediatria")
            print("2. Renata Valdez - Clinico")
            print("3. Carlos Ruiz - Nutricion")
            print("4. Maria Torres - Dentista")
            print("5. Luis Garcia - Obstetricia")

            opcion = input(
                "Ingrese el número del médico: "
            )

            if opcion == "1":
                codigo = "M001"
                nombre = "Sebastian Quispe"
                especialidad = "Pediatria"

            elif opcion == "2":
                codigo = "M002"
                nombre = "Renata Valdez"
                especialidad = "Clinico"

            elif opcion == "3":
                codigo = "M003"
                nombre = "Carlos Ruiz"
                especialidad = "Nutricion"

            elif opcion == "4":
                codigo = "M004"
                nombre = "Maria Torres"
                especialidad = "Dentista"

            elif opcion == "5":
                codigo = "M005"
                nombre = "Luis Garcia"
                especialidad = "Obstetricia"

            else:
                print("Error: opción no válida.")

                nuevamente = input(
                    "¿Desea ingresar nuevamente la opción? (s/n): "
                )

                if nuevamente.lower() == "s":
                    continue
                else:
                    break

            duplicado = False

            for m in medicos:
                if m.codigo == codigo:
                    duplicado = True

            if duplicado:
                print("Error: este médico ya está registrado.")

                nuevamente = input(
                    "¿Desea seleccionar nuevamente? (s/n): "
                )

                if nuevamente.lower() == "s":
                    continue
                else:
                    break

            medico = Medico(
                codigo,
                nombre,
                especialidad
            )

            medicos.append(medico)

            print("\nMédico registrado correctamente.")
            print(medico.resumen())
            break

    
    elif opcion_menu == "3":

        while True:

            print("\n=== BUSCAR MÉDICO POR CÓDIGO ===")

            print("M001 - Sebastian Quispe - Pediatria")
            print("M002 - Renata Valdez - Clinico")
            print("M003 - Carlos Ruiz - Nutricion")
            print("M004 - Maria Torres - Dentista")
            print("M005 - Luis Garcia - Obstetricia")

            codigo_buscar = input(
                "\nIngrese el código del médico: "
            )

            if codigo_buscar == "M001":
                medico = Medico(
                    "M001",
                    "Sebastian Quispe",
                    "Pediatria"
                )

            elif codigo_buscar == "M002":
                medico = Medico(
                    "M002",
                    "Renata Valdez",
                    "Clinico"
                )

            elif codigo_buscar == "M003":
                medico = Medico(
                    "M003",
                    "Carlos Ruiz",
                    "Nutricion"
                )

            elif codigo_buscar == "M004":
                medico = Medico(
                    "M004",
                    "Maria Torres",
                    "Dentista"
                )

            elif codigo_buscar == "M005":
                medico = Medico(
                    "M005",
                    "Luis Garcia",
                    "Obstetricia"
                )

            else:
                print("Error: código no encontrado.")

                nuevamente = input(
                    "¿Desea ingresar nuevamente el código? (s/n): "
                )

                if nuevamente.lower() == "s":
                    continue
                else:
                    break

            buscar = Buscar_codigo(
                medico.codigo,
                medico
            )

            resultado = buscar.buscar(codigo_buscar)

            if resultado != None:
                print("\nMédico encontrado:")
                print(resultado.resumen())
            else:
                print("Código no encontrado.")

            break

    
    elif opcion_menu == "4":

        while True:

            print("\n=== PROGRAMAR CITA ===")

            codigo_cita = input(
                "Ingrese el código de la cita: "
            )

            codigo_paciente = input(
                "Ingrese el código del paciente: "
            )

            nombre_paciente = input(
                "Ingrese el nombre del paciente: "
            )

            edad_texto = input(
                "Ingrese la edad del paciente: "
            )

            if not edad_texto.isdigit():
                print("Error: la edad debe ser numérica.")

                nuevamente = input(
                    "¿Desea ingresar nuevamente los datos? (s/n): "
                )

                if nuevamente.lower() == "s":
                    continue
                else:
                    break

            edad = int(edad_texto)

            if edad < 0 or edad > 120:
                print("Error: la edad debe estar entre 0 y 120.")

                nuevamente = input(
                    "¿Desea ingresar nuevamente los datos? (s/n): "
                )

                if nuevamente.lower() == "s":
                    continue
                else:
                    break

            paciente = Paciente(
                codigo_paciente,
                nombre_paciente,
                edad
            )

            print("\nMédicos disponibles:")
            print("M001 - Sebastian Quispe - Pediatria")
            print("M002 - Renata Valdez - Clinico")
            print("M003 - Carlos Ruiz - Nutricion")
            print("M004 - Maria Torres - Dentista")
            print("M005 - Luis Garcia - Obstetricia")

            codigo_medico = input(
                "\nIngrese el código del médico: "
            )

            if codigo_medico == "M001":
                medico = Medico(
                    "M001",
                    "Sebastian Quispe",
                    "Pediatria"
                )

            elif codigo_medico == "M002":
                medico = Medico(
                    "M002",
                    "Renata Valdez",
                    "Clinico"
                )

            elif codigo_medico == "M003":
                medico = Medico(
                    "M003",
                    "Carlos Ruiz",
                    "Nutricion"
                )

            elif codigo_medico == "M004":
                medico = Medico(
                    "M004",
                    "Maria Torres",
                    "Dentista"
                )

            elif codigo_medico == "M005":
                medico = Medico(
                    "M005",
                    "Luis Garcia",
                    "Obstetricia"
                )

            else:
                print("Error: código de médico no válido.")

                nuevamente = input(
                    "¿Desea ingresar nuevamente el código? (s/n): "
                )

                if nuevamente.lower() == "s":
                    continue
                else:
                    break

            fecha = input(
                "Ingrese la fecha de la cita: dd/mm/aaaa "
            )

            cita = Progama_cita(
                codigo_cita,
                paciente.nombre,
                medico.nombre,
                fecha
            )

            citas.append(cita)

            print("\nCita registrada correctamente.")
            print(cita.resumen())
            break

    
    elif opcion_menu == "5":

        while True:

            print("\n=== REGISTRAR ATENCIÓN ===")

            codigo_paciente = input(
                "Ingrese el código del paciente: "
            )

            nombre_paciente = input(
                "Ingrese el nombre del paciente: "
            )

            edad_texto = input(
                "Ingrese la edad del paciente: "
            )

            if not edad_texto.isdigit():
                print("Error: la edad debe ser numérica.")

                nuevamente = input(
                    "¿Desea ingresar nuevamente los datos? (s/n): "
                )

                if nuevamente.lower() == "s":
                    continue
                else:
                    break

            edad = int(edad_texto)

            if edad < 0 or edad > 120:
                print("Error: la edad debe estar entre 0 y 120.")

                nuevamente = input(
                    "¿Desea ingresar nuevamente los datos? (s/n): "
                )

                if nuevamente.lower() == "s":
                    continue
                else:
                    break

            paciente = Paciente(
                codigo_paciente,
                nombre_paciente,
                edad
            )

            dni = input(
                "Ingrese el DNI: "
            )

            print("\nMédicos disponibles:")
            print("M001 - Sebastian Quispe - Pediatria")
            print("M002 - Renata Valdez - Clinico")
            print("M003 - Carlos Ruiz - Nutricion")
            print("M004 - Maria Torres - Dentista")
            print("M005 - Luis Garcia - Obstetricia")

            codigo_medico = input(
                "\nIngrese el código del médico: "
            )

            if codigo_medico == "M001":
                medico = Medico(
                    "M001",
                    "Sebastian Quispe",
                    "Pediatria"
                )

            elif codigo_medico == "M002":
                medico = Medico(
                    "M002",
                    "Renata Valdez",
                    "Clinico"
                )

            elif codigo_medico == "M003":
                medico = Medico(
                    "M003",
                    "Carlos Ruiz",
                    "Nutricion"
                )

            elif codigo_medico == "M004":
                medico = Medico(
                    "M004",
                    "Maria Torres",
                    "Dentista"
                )

            elif codigo_medico == "M005":
                medico = Medico(
                    "M005",
                    "Luis Garcia",
                    "Obstetricia"
                )

            else:
                print("Error: código de médico no válido.")

                nuevamente = input(
                    "¿Desea ingresar nuevamente el código? (s/n): "
                )

                if nuevamente.lower() == "s":
                    continue
                else:
                    break

            atencion = Atencion(
                paciente.nombre,
                dni,
                paciente.codigo,
                medico.especialidad,
                medico.codigo
            )

            historial.append(atencion)

            print("\nAtención registrada correctamente.")

            print("\n===================================")
            print("       ATENCIÓN REGISTRADA")
            print("===================================")
            print("Paciente:", paciente.nombre)
            print("DNI:", dni)
            print("Edad:", paciente.edad)
            print("Médico:", medico.nombre)
            print("Código médico:", medico.codigo)
            print("Especialidad:", medico.especialidad)
            print("===================================")

            break


    elif opcion_menu == "6":

        print("\nGracias por utilizar el sistema.")

    else:

        print("\nError: opción no válida.")


if __name__ == "__main__":
    main()

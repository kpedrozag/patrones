from depts_ft import *
from gen_code import generador
# import sys

def data_request():
    print("A continuacion ingrese los datos del empleado.")

    v1 = input("NOMBRE DEL EMPLEADO: ")
    v2 = input("APELLIDO DEL EMPLEADO: ")

    deptos = ["FINANZAS", "RECURSOS HUMANOS", "ADMINISTRACIÓN", "OFICIOS VARIOS"]
    while True:
        print("\nA continuacion seleccione el número del departamento del empleado:")
        for i in range(len(deptos)):
            print(str(i + 1) + ".\t" + "DEPARTAMENTO DE " + deptos[i])
        v3 = int(input("\nDigite el numero del departamento correspondiente: "))

        if v3 == 1:
            v3 = 'fz'
            break
        elif v3 == 2:
            v3 = 'rh'
            break
        elif v3 == 3:
            v3 = 'ad'
            break
        elif v3 == 4:
            v3 = 'ov'
            break
        else:
            print("ERROR. OPCION NO VALIDA.")
    return v1, v2, v3

def insercion(emp):  # objeto factory

    
if __name__ == '__main__':
    print("SISTEMA DE INSERCION DE EMPLEADOS\n\n")
    input("Digite cualquier tecla para continuar.")
    fc = Factory()
    while True:
        nombre, apellido, cod_dp = data_request()
        fc.get_emp(idd=generador(cod_dp), nm=nombre, ap=apellido, dpt=cod_dp)

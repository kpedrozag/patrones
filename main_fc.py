from depts_ft import *
from gen_code import generador
from database_file_sg import DB


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
    enlace = DB()
    nm = emp.get_nom()
    ap = emp.get_apell()
    cd = emp.get_cod()
    dpt = emp.get_dept()

    query = "INSERT INTO empleados (codigo, nombre, apellido, departamento) VALUES (" + str(cd) + ",\'" + nm + "\',\'" + ap + "\',\'" + dpt + "\');"

    enlace.cur.execute(query)
    enlace.conn.commit()


if __name__ == '__main__':
    print("SISTEMA DE INSERCION DE EMPLEADOS\n\n")
    input("Digite cualquier tecla para continuar.")
    fc = Factory()
    while True:
        nombre, apellido, cod_dp = data_request()
        emp = fc.get_emp(idd=generador(cod_dp), nm=nombre, ap=apellido, dpt=cod_dp)
        insercion(emp)
        res = input("Desea añadir otro empleado?\n's' -> sí\n'n' -> no\n\nOpcion:\t")
        if res == 's' or res == 'S':
            pass
        elif res == 'n' or res == 'N':
            break
        else:
            print("ERROR.")
    l = DB()
    print(l.cur.execute('SELECT * FROM empelados').fetchall())

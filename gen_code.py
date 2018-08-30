import random
from database_file_sg import DB


def generador(d):
    enlace = DB()
    val = None
    while True:
        if d == 'fz':
            val = random.randint(1000, 1999)
        elif d == 'rh':
            val = random.randint(2000, 2999)
        elif d == 'ad':
            val = random.randint(3000, 3999)
        elif d == 'ov':
            val = random.randint(4000, 4999)
        query = "SELECT codigo FROM empleados"
        results = enlace.cur.execute(query).fetchall()
        if val not in results:
            break
    return val

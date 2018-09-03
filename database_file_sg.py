import sqlite3 as sql


class DB:
    ins = None
    cur = None
    conn = None

    def __new__(cls, *args, **kwargs): # crea el objeto pero no lo iniicaliza
        if DB.ins is None:
            DB.ins = object.__new__(cls)
        return DB.ins

    def __init__(self):  # crea el objeto
        if DB.conn is None:
            DB.conn = sql.connect('mydb.db')
            DB.cur = DB.conn.cursor()
            query = """
			CREATE TABLE IF NOT EXISTS empleados(
				codigo NUMERIC NOT NULL,
				nombre TEXT NOT NULL,
				apellido TEXT NOT NULL,
				departamento TEXT NOT NULL,
			);
		"""
            DB.cur.execute(query)
            DB.conn.commit()

def prueba():
    primero = DB()
    query = 		"""
		INSERT INTO libros
		(codigo, nombre, apellido, departamento)
		VALUES
		('Stephen King', 'Terror', 115,'Cementerio de animales');
		"""
    primero.cur.execute(query)
    primero.conn.commit()

    segundo = DB()
    query = """
		INSERT INTO libros
		(autor, genero, precio, titulo)
		VALUES
		('Alfred Bester', 'Ciencia ficción', 200,'Las estrellas, mi destino');
		"""
    segundo.cur.execute(query)

    tercero = DB()
    query = 'SELECT * FROM libros'
    print(tercero.cur.execute(query).fetchall())

import oracledb

con = oracledb.connect(user="escolar", password="ClaveEscolar_123",
                       dsn="192.168.56.10:1521/FREEPDB1")
cur = con.cursor()

alumnos = [
    (105, "Sofía Hernández", "Ingeniería en Sistemas"),
    (106, "Diego Ramírez",   "Ingeniería en Sistemas"),
    (107, "Valeria Torres",  "Ingeniería en Sistemas"),
    (108, "Jorge Castillo",  "Ingeniería en Sistemas"),
    (109, "Fernanda Ortiz",  "Ingeniería en Sistemas"),
    (110, "Pablo Mendoza",   "Ingeniería en Sistemas"),
    (111, "Camila Flores",   "Ingeniería en Sistemas"),
    (112, "Andrés Vargas",   "Ingeniería en Sistemas"),
    (113, "Daniela Ríos",    "Ingeniería en Sistemas"),
    (114, "Ricardo Navarro", "Ingeniería en Sistemas"),
]
cur.executemany(
    "INSERT INTO ALUMNOS (ID_ALUMNO, NOMBRE, CARRERA) VALUES (:1, :2, :3)",
    alumnos
)
con.commit()

cur.execute("SELECT COUNT(*) FROM ALUMNOS")
print("Total de alumnos:", cur.fetchone()[0])

con.close()
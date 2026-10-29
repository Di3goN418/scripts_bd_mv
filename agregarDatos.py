import oracledb

con = oracledb.connect(user="escolar", password="ClaveEscolar_123",
                       dsn="192.168.56.10:1521/FREEPDB1")
cur = con.cursor()

alumnos = [
    (115, "Sofía Perez", "Ingeniería en "),
    (116, "Diego juan",   "Ingeniería en tics"),
]
cur.executemany(
    "INSERT INTO ALUMNOS (ID_ALUMNO, NOMBRE, CARRERA) VALUES (:1, :2, :3)",
    alumnos
)
con.commit()

# Verificar
cur.execute("SELECT * FROM ALUMNOS ORDER BY ID_ALUMNO")
for fila in cur:
    print(fila)

cur.execute("SELECT COUNT(*) FROM ALUMNOS")
print("Total de alumnos:", cur.fetchone()[0])

con.close()
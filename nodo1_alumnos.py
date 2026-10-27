import oracledb

con = oracledb.connect(user="escolar", password="ClaveEscolar_123",
                       dsn="192.168.56.10:1521/FREEPDB1")
cur = con.cursor()

# Crear tabla
cur.execute("""
    CREATE TABLE ALUMNOS (
        ID_ALUMNO NUMBER PRIMARY KEY,
        NOMBRE    VARCHAR2(100) NOT NULL,
        CARRERA   VARCHAR2(100)
    )
""")

# Insertar datos
alumnos = [
    (101, "Ana López",    "Ingeniería en Sistemas"),
    (102, "Luis Pérez",   "Ingeniería en Sistemas"),
    (103, "María Gómez",  "Ingeniería en Sistemas"),
    (104, "Carlos Ruiz",  "Ingeniería en Sistemas"),
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

con.close()
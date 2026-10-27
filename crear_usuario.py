import oracledb

con = oracledb.connect(user="system", password="Diegon24", dsn="192.168.56.10/FREEPDB1")

cur = con.cursor()
cur.execute('CREATE USER escolar IDENTIFIED BY "ClaveEscolar_123"')
cur.execute("GRANT CREATE SESSION, CREATE TABLE, CREATE DATABASE LINK TO escolar")
cur.execute("ALTER USER escolar QUOTA 100M ON USERS")
con.close()

print("Usuario creado exitosamente.") 
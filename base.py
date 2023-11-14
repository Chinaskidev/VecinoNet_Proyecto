import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine
import pandas as pd

# Conectar a la base de datos MariaDB/MySQL
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    database='telecomunicaciones'
)

# Crear una conexión de SQLAlchemy
engine = create_engine('mysql+mysqlconnector://root:123456@127.0.0.1/telecomunicaciones')

cursor = conn.cursor()

# Crear la segunda tabla en la base de datos si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS datos_procesados2 (
        Año INTEGER,
        Trimestre INTEGER,
        Provincia TEXT,
        `Mbps (Media de bajada)` FLOAT,
        Localidad VARCHAR(50),
        NUEVOACCESO REAL
    )
''')
# Leer tu segundo DataFrame desde un archivo o de alguna otra fuente
df1_1 = pd.read_csv('.\datos_EDA\interbajada_localprovincia_EDA.csv')

# Insertar los datos en la segunda tabla
df1_1.to_sql('datos_procesados2', con=engine, if_exists='replace', index=False, chunksize=1000)

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

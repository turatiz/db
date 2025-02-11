import pandas as pd
from sqlalchemy import create_engine
import time

# Esperar a que la base de datos esté lista
time.sleep(10)

# Configuración de conexión a PostgreSQL
DB_USER = "ash"
DB_PASSWORD = "password"
DB_HOST = "db"  # Nombre del servicio en docker-compose
DB_PORT = "5432"
DB_NAME = "pokemon_db"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# Descargar y cargar los datos
csv_url = "https://raw.githubusercontent.com/veekun/pokedex/master/pokedex/data/csv/pokemon.csv"
df = pd.read_csv(csv_url)

# Guardar en la base de datos
df.to_sql('pokemon', engine, if_exists='replace', index=False)

print("✅ Datos cargados en la base de datos")

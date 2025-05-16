from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Reemplaza estos valores con los de tu Supabase o tu base local
DATABASE_URL = "postgresql://postgres:25072016TrosDan*#*@db.qbygulpdspuamfuzhecm.supabase.co:5432/postgres"

# Crea el motor de conexión
engine = create_engine(DATABASE_URL)

# Crea una sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear las tablas si no existen
def init_db():
    Base.metadata.create_all(bind=engine)

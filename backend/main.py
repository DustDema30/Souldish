from fastapi import FastAPI
from database import init_db
from models import Receta
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import init_db, SessionLocal
from models import Receta
from schemas import RecetaCreate
from typing import List
from schemas import RecetaOut
from fastapi import HTTPException
from schemas import RecetaUpdate  # Solo si la creaste, si no, puedes usar RecetaCreate




app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API SoulDish funcionando ✅"}

@app.on_event("startup")
def startup_event():
    init_db()

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta POST para crear una receta
@app.post("/recetas")
def crear_receta(receta: RecetaCreate, db: Session = Depends(get_db)):
    nueva_receta = Receta(nombre=receta.nombre, estado_animo=receta.estado_animo)
    db.add(nueva_receta)
    db.commit()
    db.refresh(nueva_receta)
    return nueva_receta

@app.get("/recetas", response_model=List[RecetaOut])
def listar_recetas(db: Session = Depends(get_db)):
    recetas = db.query(Receta).all()
    return recetas

@app.put("/recetas/{id}", response_model=RecetaOut)
def actualizar_receta(id: int, receta: RecetaCreate, db: Session = Depends(get_db)):
    receta_db = db.query(Receta).filter(Receta.id == id).first()
    if receta_db is None:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    
    receta_db.nombre = receta.nombre
    receta_db.estado_animo = receta.estado_animo
    db.commit()
    db.refresh(receta_db)
    return receta_db

@app.delete("/recetas/{id}", status_code=204)
def eliminar_receta(id: int, db: Session = Depends(get_db)):
    receta_db = db.query(Receta).filter(Receta.id == id).first()
    if receta_db is None:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    
    db.delete(receta_db)
    db.commit()
    return



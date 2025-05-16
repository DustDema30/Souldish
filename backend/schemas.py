from pydantic import BaseModel

class RecetaCreate(BaseModel):
    nombre: str
    estado_animo: str

class RecetaOut(RecetaCreate):
    id: int

    class Config:
        orm_mode = True
        
class RecetaUpdate(BaseModel):
    nombre: str
    estado_animo: str

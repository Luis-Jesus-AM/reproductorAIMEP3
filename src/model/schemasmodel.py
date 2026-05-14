from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UsuarioSchema(BaseModel):
    id_usuario: Optional[int] = None
    nombre: str = Field(..., min_length=3, max_length=100, description="Nombre del usuario")
    apellido: str = Field(..., min_length=3, max_length=100, description="Apellido del usuario")
    email: EmailStr = Field(..., description="Correo electrónico válido")
    password: str = Field(..., min_length=6, description="Contraseña con mínimo 6 caracteres")
    fecha_registro: Optional[datetime] = None
    ultimo_acceso: Optional[datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Dana",
                "apellido": "Martínez",
                "email": "dana@example.com",
                "password": "supersegura123"
            }
        }

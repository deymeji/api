from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Libro(BaseModel):
    titulo:str
    autor: str
    pagina: int
    editor: Optional [str]

#http://127.0.0.1:8000/

@app.get("/")
def index():
    return { "message" : "Hola, Pythonianos"}

@app.get("/libros/{id}")
def mostrar_libro(id: int):
    return {"data": id}



@app.post("/libros")
def insertar_libros(libro: Libro):
    return{"message" : f"libro {libro.titulo} insertado"}

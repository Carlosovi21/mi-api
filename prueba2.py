from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. Definimos la estructura de los datos que van a llegar desde Power Automate
class DatosEntrada(BaseModel):
    numero1: float
    numero2: float
    texto: str

@app.post("/ejecutar")
def ejecutar(datos: DatosEntrada):
    # 2. Hacemos la suma de los dos números
    resultado_suma = datos.numero1 + datos.numero2
    
    # 3. Devolvemos la suma y el mismo texto que recibimos
    return {
        "resultado_suma": resultado_suma,
        "texto_recibido": datos.texto
    }
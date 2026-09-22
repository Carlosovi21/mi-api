from fastapi import FastAPI

app = FastAPI()

@app.post("/ejecutar")
def ejecutar():
    return {"mensaje": "Uribe es un para..... hijue....."}
from fastapi import FastAPI

app = FastAPI()

@app.post("/ejecutar")
def ejecutar():
    return "Uribe es un para..... hijue....."
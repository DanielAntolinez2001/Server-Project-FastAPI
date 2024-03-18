from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return "Hola, bienvenido a mi API!"
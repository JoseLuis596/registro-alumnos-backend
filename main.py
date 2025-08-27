from fastapi import FastAPI

app = FastAPI()  # <--- Esta línea es crucial

@app.get("/")
def read_root():
    return {"message": "Backend funcionando"}

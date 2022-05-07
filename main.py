from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/api")
def hello():
  return { "message": "Hello, world!" }

app.mount("/", StaticFiles(directory="client/build", html=True), name="client")
import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# -----------------------------------------------------------------------------
app = FastAPI()
# -----------------------------------------------------------------------------
origins = ["http://localhost", "http://127.0.0.1"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


@app.get("/")
def home():
    return {"You've Got": "Py"}


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    config = uvicorn.Config(
        "main:app",
        host="0.0.0.0",
        port=(8000),
        reload=False if os.getenv("ENVIROMENT") != "dev" else True,
    )
    server = uvicorn.Server(config)
    server.run()

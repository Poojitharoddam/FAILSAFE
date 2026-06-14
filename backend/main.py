from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.predict import router as predict_router
from routes.auth import router as auth_router
from routes.students import router as students_router

app = FastAPI(
    title="FAILSAFE API",
    version="1.0"
)

# ==========================
# CORS FIX
# ==========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# Routes
# ==========================

app.include_router(auth_router)
app.include_router(students_router)
app.include_router(predict_router)

@app.get("/")
def home():
    return {
        "project": "FAILSAFE",
        "status": "Running"
    }
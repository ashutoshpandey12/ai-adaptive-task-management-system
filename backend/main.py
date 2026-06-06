from fastapi import FastAPI

app = FastAPI(
    title="AI Adaptive Task Management System",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "AI Adaptive Task Management System Running"
    }

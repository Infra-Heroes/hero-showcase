from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.get("/")
async def root():
    log_level = os.environ.get("LOG_LEVEL", "info")
    return {
        "message": "Hello from FastAPI!",
        "log_level": log_level,
        "framework": "FastAPI"
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
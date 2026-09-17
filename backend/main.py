from fastapi import FastAPI

app = FastAPI(title="AI Revenue Recovery")

@app.get("/health")
def health():
    return {"status": "ok"}
from fastapi import FastAPI
from random import choice
import uvicorn

app = FastAPI(title="Random Downtime Excuse API", version="1.0.0")
try:
    with open("excuses.txt", encoding="utf-8") as f:
        DOWNTIME_EXCUSES = [
            line.strip() 
            for line in f 
            if line.strip() and not line.strip().startswith("#")
        ]
except FileNotFoundError:
    DOWNTIME_EXCUSES = ["No excuses left. The excuse server is also down."]
    print("excuses.txt not found – using fallback")
print(f"Loaded {len(DOWNTIME_EXCUSES)} excuses")

@app.get("/")
async def root():
    return {"message": "Welcome to the Downtime Excuse API! Call /downtime for chaos."}

@app.get("/downtime")
async def get_downtime_reason():
    reason = choice(DOWNTIME_EXCUSES)
    return {
        "status": "down",
        "reason": reason,
        "timestamp": "Just now",
        "suggestion": "Try again later… or don't. Your call."
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
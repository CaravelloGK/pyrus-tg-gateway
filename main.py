from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "ok"}

@app.post("/tg/webhook")
async def tg_webhook(request: Request):
    update = await request.json()
    print("Got update:", update)
    return {"ok": True}
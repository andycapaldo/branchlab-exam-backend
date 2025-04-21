from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

drugs = [{"name": "Atorvastatin", "brand": "Lipitor", "class": "Statin", "NDC": "0071-0155-23", "indications": "Hyperlipidemia, prevention of CV events", "warnings": "May cause liver enzyme abnormalities"}]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/drug/{item_id}")
def get_drug(item_id: int):
    if item_id < len(drugs):
        return drugs[item_id]
    else:
        raise HTTPException(status_code=404, detail="Drug not found")
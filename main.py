from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

drugs = [{"Name": "Atorvastatin", "Brand Name": "Lipitor", "Drug Class": "Statin", "NDC": "0071-0155-23", "Indications": "Hyperlipidemia, prevention of CV events", "Warnings": "May cause liver enzyme abnormalities"}]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/api/drug")
def get_drug():
    if drugs:
        return drugs
    else:
        raise HTTPException(status_code=404, detail="Drug not found")
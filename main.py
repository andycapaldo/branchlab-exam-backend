from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

class Drug(BaseModel):
    Name: str
    Brand_Name: str
    Drug_Class: str
    NDC: str
    Indications: str
    Warnings: str

drugs = [{"Name": "Atorvastatin", "Brand_Name": "Lipitor", "Drug_Class": "Statin", "NDC": "0071-0155-23", "Indications": "Hyperlipidemia, prevention of CV events", "Warnings": "May cause liver enzyme abnormalities"}]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/api/drug", response_model=list[Drug])
def get_drugs():
    if drugs:
        return drugs
    raise HTTPException(status_code=404, detail="Drug list is empty")


@app.get("/api/drug/{drug_name}", response_model=Drug)
def get_drug_by_name(drug_name: str):
    for drug in drugs:
        if drug['Name'].lower() == drug_name.lower():
            return drug 
        raise HTTPException(status_code=404, detail=f"{drug_name} not found")
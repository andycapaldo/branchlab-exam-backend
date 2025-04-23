from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

class Drug(BaseModel):
    name: str
    brand_name: str
    drug_class: str
    ndc: str
    indications: str
    warnings: str

# Sample data for demonstration purposes
atorvastatin = Drug(
    name="Atorvastatin",
    brand_name="Lipitor",
    drug_class="Statin",
    ndc="0071-0155-23",
    indications="Hyperlipidemia, prevention of CV events",
    warnings="May cause liver enzyme abnormalities"
)

# Data serialized into a dictionary as this translates perfectly into JSON 
serialized = atorvastatin.model_dump()

drugs = [serialized, serialized, serialized]

# CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://branchlab-exam-frontend.onrender.com"], # Ensures only the frontend can access the API (both test and production envs)
    allow_methods=["*"],
    allow_headers=["*"],
)

# Placeholder root endpoint
@app.get("/")
def root():
    return {"Hello": "World"}

# Returns a list of all drugs
@app.get("/api/drug", response_model=list[Drug])
def get_drugs():
    if drugs:
        return drugs
    raise HTTPException(status_code=404, detail="Drug list is empty")

# Returns a specific drug object by name - e.g. can be attached to a user input component
@app.get("/api/drug/{drug_name}", response_model=Drug)
def get_drug_by_name(drug_name: str):
    for drug in drugs:
        if drug['Name'].lower() == drug_name.lower():
            return drug 
    raise HTTPException(status_code=404, detail=f"{drug_name} not found")
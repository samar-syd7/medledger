from fastapi import FastAPI
from core.hashing import sha256_file, sha256_text
from api.blockchain import store_hash
from core.verify import verify_text_against_hash
from core.access_proof import generate_access_proof
from fhir.fhir_adapter import audit_fhir_resource
from api.blockchain import get_record, contract
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI(title="MedLedger")

templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def serve_dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/audit/dicom")
def audit_dicom(path: str):
    hash_val = sha256_file(path)
    receipt = store_hash(hash_val, "DICOM")
    return {
        "hash": hash_val,
        "tx": receipt.transactionHash.hex()
    }

@app.post("/audit/hl7")
def audit_hl7(message: str):
    hash_val = sha256_text(message)
    receipt = store_hash(hash_val, "HL7")
    return {
        "hash": hash_val,
        "tx": receipt.transactionHash.hex()
    }

@app.post("/access")
def log_access(patient_id: str, user_id: str, action: str):
    proof = generate_access_proof(patient_id, user_id, action)

    receipt = store_hash(proof["proof_hash"], "ACCESS")

    return {
        "proof_hash": proof["proof_hash"],
        "tx": receipt.transactionHash.hex()
    }

@app.post("/audit/fhir")
def audit_fhir(resource: dict):
    result = audit_fhir_resource(resource)
    receipt = store_hash(result["hash"], "FHIR")

    return {
        "hash": result["hash"],
        "tx": receipt.transactionHash.hex()
    }
    
@app.get("/records/count")
def get_record_count():
    return {"count": contract.functions.getRecordCount().call()}


@app.get("/records/{index}")
def get_record_api(index: int):
    return get_record(index)
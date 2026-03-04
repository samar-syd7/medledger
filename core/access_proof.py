import hashlib
import time

def generate_access_proof(patient_id: str, user_id: str, action: str):
    timestamp = str(int(time.time()))
    raw = f"{patient_id}:{user_id}:{action}:{timestamp}"
    proof_hash = hashlib.sha256(raw.encode()).hexdigest()

    return {
        "proof_hash": proof_hash,
        "timestamp": timestamp,
        "patient_id": patient_id,
        "user_id": user_id,
        "action": action
    }
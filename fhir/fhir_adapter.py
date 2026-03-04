import json
from core.hashing import sha256_text

def audit_fhir_resource(resource: dict):
    canonical = json.dumps(resource, sort_keys=True)
    hash_val = sha256_text(canonical)

    return {
        "hash": hash_val,
        "resourceType": resource.get("resourceType", "Unknown")
    }
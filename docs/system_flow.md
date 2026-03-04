# System Workflow

MedLedger anchors healthcare data integrity on blockchain using cryptographic hashing.

The workflow is identical for HL7 messages, DICOM files, and FHIR resources.

---

## Data Integrity Flow

Healthcare Data (HL7 / DICOM / FHIR)
        ↓
FastAPI API Endpoint
        ↓
Canonicalization (FHIR JSON sorting if applicable)
        ↓
SHA-256 Hash Generation
        ↓
Ethereum Smart Contract Anchoring
        ↓
Immutable Audit Record
        ↓
Dashboard Monitoring

---

## Data Type Handling

### HL7

HL7 messages are hashed as raw message strings.

Example:

MSH|^~\&|LAB|...

---

### DICOM

DICOM files are hashed using binary file hashing.

The system anchors the SHA-256 hash of the file.

---

### FHIR

FHIR resources are canonicalized JSON objects.

Steps:

1. JSON sorted deterministically
2. Canonical string produced
3. SHA-256 hash generated

---

## Verification Flow

Verification recomputes the hash of the current data and compares it with the stored blockchain hash.

If hashes match:

- Data integrity confirmed

If hashes differ:

- Data has been modified

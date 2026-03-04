# MedLedger Architecture

## 1. System Overview

MedLedger is a blockchain-anchored healthcare data integrity platform
designed to provide immutable audit logging and cryptographic tamper
detection for healthcare workflows.

The system follows an **off-chain storage + on-chain integrity
anchoring** architecture.

Healthcare data is never stored on-chain.\
Only cryptographic fingerprints (SHA-256 hashes) are recorded on
Ethereum.

------------------------------------------------------------------------

## 2. High-Level Flow

1.  Healthcare data received (HL7 message, DICOM file, or FHIR resource)
2.  Data canonicalized (if structured JSON)
3.  SHA-256 hash generated off-chain
4.  Hash submitted to Ethereum smart contract
5.  Blockchain stores:
    -   `bytes32 hash`
    -   `dataType`
    -   `timestamp`
6.  Verification endpoint recomputes hash and compares with stored value

------------------------------------------------------------------------

## 3. On-Chain Layer

### Smart Contract (Solidity)

The contract stores:

-   `bytes32 hash`
-   `string dataType`
-   `uint256 timestamp`

Properties:

-   Immutable once written
-   Publicly verifiable
-   No PHI exposure
-   Tamper-evident by design

Development environment uses:

-   Hardhat (v2)
-   Local Ethereum node
-   Ignition deployment module

------------------------------------------------------------------------

## 4. Off-Chain Layer

### Backend (FastAPI)

Responsibilities:

-   Accept healthcare data
-   Perform SHA-256 hashing
-   Submit hash to blockchain
-   Provide verification endpoints
-   Serve SaaS monitoring dashboard

Core modules:

-   `core/hashing.py` --- cryptographic hashing engine
-   `core/verify.py` --- tamper detection logic
-   `core/access_proof.py` --- access event proof generation
-   `api/blockchain.py` --- Web3 integration layer

------------------------------------------------------------------------

## 5. Healthcare Standard Integration

### HL7

Raw message hashing after normalization.

### DICOM

File-level hashing to anchor imaging integrity.

### FHIR

Canonical JSON serialization (sorted keys) prior to hashing to ensure
deterministic fingerprints.

------------------------------------------------------------------------

## 6. Dashboard Layer

Frontend served via FastAPI using Jinja templates.

Features:

-   Real-time metrics
-   Record distribution chart (Chart.js)
-   Audit record table
-   Access log table
-   Integrity verification tool
-   Blockchain connection status indicator

------------------------------------------------------------------------

## 7. Security Model

-   SHA-256 collision-resistant hashing
-   Immutable blockchain storage
-   Deterministic verification
-   Zero PHI stored on-chain
-   Clear separation of storage and integrity layers

------------------------------------------------------------------------

## 8. Design Rationale

Blockchain is used for:

-   Immutability
-   Public verifiability
-   Audit anchoring

Blockchain is not used for:

-   Data storage
-   PHI handling
-   Business logic execution

This separation ensures scalability and regulatory safety.

------------------------------------------------------------------------

## 9. Intended Use Case

MedLedger is a proof-of-concept demonstrating how healthcare systems can
integrate blockchain for integrity verification while maintaining
compliance constraints.

Not production-ready without:

-   Authentication
-   Multi-tenant support
-   Secure key management
-   Production blockchain network configuration
-   Regulatory review

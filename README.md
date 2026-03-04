# MedLedger

Blockchain-Anchored Healthcare Data Integrity Platform

MedLedger is a compliance-oriented backend system designed to
cryptographically anchor healthcare data integrity using Ethereum smart
contracts.

The platform integrates HL7, DICOM, and FHIR workflows with immutable
on-chain audit logging while preserving PHI off-chain.

------------------------------------------------------------------------

## Overview

Healthcare systems generate high-value data (imaging, admissions,
clinical records) that must be tamper-resistant and auditable.

MedLedger provides:

-   SHA-256 hashing of medical data
-   Ethereum smart contract anchoring
-   Immutable audit trail
-   Tamper verification engine
-   Access proof logging
-   SaaS-style monitoring dashboard

This system demonstrates an off-chain storage + on-chain integrity
anchoring architecture suitable for compliance-focused environments.

------------------------------------------------------------------------

## Architecture

Off-chain data → SHA-256 hash → Smart Contract (Ethereum) → Immutable
record

Medical data is never stored on-chain.

Only cryptographic fingerprints are anchored.

See `/docs/architecture.md` for detailed flow.

------------------------------------------------------------------------

## Tech Stack

Backend: - FastAPI - Web3.py - SHA-256 cryptographic hashing

Blockchain: - Solidity - Hardhat (local development network) - Ethereum
smart contract

Frontend: - Tailwind-based SaaS dashboard - Chart.js visualization

------------------------------------------------------------------------

## Features

-   HL7 message anchoring
-   DICOM file hash anchoring
-   FHIR resource canonical hashing
-   Immutable audit logging
-   Access event proof generation
-   Tamper verification endpoint
-   Real-time dashboard monitoring

------------------------------------------------------------------------

## Local Setup

### 1. Clone Repository

``` bash
git clone <repo-url>
cd medledger
```

------------------------------------------------------------------------

### 2. Install Python Dependencies

``` bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

------------------------------------------------------------------------

### 3. Start Local Blockchain (Hardhat)

Inside `/blockchain`:

``` bash
npm install
npx hardhat node
```

Important: - Hardhat v2 is recommended. - Node.js versions above 20 may
produce compatibility warnings.

------------------------------------------------------------------------

### 4. Deploy Smart Contract

In `/blockchain`:

``` bash
npx hardhat ignition deploy ./ignition/modules/Lock.js --network localhost
```

Copy the deployed contract address and update it in:

`api/blockchain.py`

------------------------------------------------------------------------

### 5. Run Backend

From project root:

``` bash
uvicorn api.main:app --reload
```

Access:

http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## Common Setup Issues

### Hardhat Version Conflicts

If dependency errors occur:

-   Ensure Hardhat v2.x is installed
-   Avoid mixing Hardhat v3 packages with v2 toolbox
-   Use compatible `@nomiclabs/hardhat-ethers` with ethers v5

### Node.js Compatibility Warning

Hardhat may warn about Node v24. Use Node 18--20 for stable
compatibility.

### CORS Errors

The dashboard is served directly by FastAPI to avoid cross-origin
issues.

------------------------------------------------------------------------

## Design Principles

-   No PHI stored on blockchain
-   Cryptographic tamper detection
-   Deterministic hash comparison
-   Immutable audit trail
-   Clear separation of on-chain vs off-chain data

------------------------------------------------------------------------

## Disclaimer

This is a proof-of-concept architecture demonstrating healthcare
integrity anchoring. It is not a production-ready medical system.

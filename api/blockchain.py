from web3 import Web3
import json
import os

# Connect to local Hardhat node
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Replace with your deployed contract address
CONTRACT_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3"

# Load ABI from Hardhat artifacts
with open("blockchain/artifacts/contracts/AuditRegistry.sol/AuditRegistry.json") as f:
    contract_json = json.load(f)
    ABI = contract_json["abi"]

contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

def store_hash(hash_hex: str, data_type: str):
    tx_hash = contract.functions.addRecord(
        bytes.fromhex(hash_hex),
        data_type
    ).transact({
        "from": w3.eth.accounts[0]
    })

    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt

def get_record(index: int):
    record = contract.functions.getRecord(index).call()
    return {
        "hash": record[0].hex(),
        "dataType": record[1],
        "timestamp": record[2]
    }
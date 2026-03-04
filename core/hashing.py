import hashlib

def sha256_file(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def sha256_text(text: str) -> str:
    return hashlib.sha256(text.strip().encode()).hexdigest()
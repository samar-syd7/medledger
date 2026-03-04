from core.hashing import sha256_file, sha256_text

def verify_text_against_hash(text: str, stored_hash: str) -> bool:
    new_hash = sha256_text(text)
    return new_hash == stored_hash

def verify_file_against_hash(path: str, stored_hash: str) -> bool:
    new_hash = sha256_file(path)
    return new_hash == stored_hash
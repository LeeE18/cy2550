import bcrypt

def hash_password(plaintext_password: str) -> str:

    password_bytes = plaintext_password.encode('utf-8')

    salt = bcrypt.gensalt(rounds=12)

    hashed = bcrypt.hashpw(password_bytes, salt)

    return hashed.decode('utf-8')


def verify_password(plaintext_password: str, stored_hash: str) -> bool:
    password_bytes = plaintext_password.encode('utf-8')
    stored_hash_bytes = stored_hash.encode('utf-8')

    return bcrypt.checkpw(password_bytes, stored_hash_bytes)

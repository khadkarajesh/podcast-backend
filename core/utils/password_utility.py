from werkzeug.security import generate_password_hash, check_password_hash


def hash_password(password):
    return generate_password_hash(password=password, salt_length=10)


def compare_password(hashed_password, password):
    return check_password_hash(hashed_password, password)

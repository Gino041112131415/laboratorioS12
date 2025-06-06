import re

def is_valid_address(address):
    if not isinstance(address, str):
        return False
    # Acepta letras (con acentos), puntos, espacios y número al final
    pattern = r'^[A-Za-zÁÉÍÓÚáéíóúÜüÑñ.\s]+\s\d+$'
    return bool(re.match(pattern, address.strip()))

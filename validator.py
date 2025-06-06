import re

def is_valid_address(address):
    if not isinstance(address, str):
        return False
    # Simple check: must contain a street name and number
    pattern = r'^[A-Za-z\s]+\s\d+$'
    return bool(re.match(pattern, address.strip()))

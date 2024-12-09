import re

def remove_special_characters(phone_number: str):
    """Remove caracteres especiais de um número de telefone."""
    clean_number = re.sub(r'\D', '', phone_number)
    return clean_number


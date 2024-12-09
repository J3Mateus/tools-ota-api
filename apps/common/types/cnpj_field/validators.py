import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def cnpj_generator(value):
    value = re.sub(r'\D', '', str(value)).zfill(12)[:12]
    v1, v2 = last_digits_cnpj(value)

    new = value + str(v1) + str(v2)

    if not is_valid_cnpj(new):
        new = None

    return new

def cnpj_random_generator():
    import random

    candidate = str(random.randint(1, 999999999998))
    while not cnpj_generator(candidate):
        candidate = str(random.randint(1, 999999999998))

    return cnpj_generator(candidate)

def last_digits_cnpj(value):
    cnpj = tuple(map(int, value))

    v1 = 5 * cnpj[0] + 4 * cnpj[1] + 3 * cnpj[2] + 2 * cnpj[3]
    v1 += 9 * cnpj[4] + 8 * cnpj[5] + 7 * cnpj[6] + 6 * cnpj[7]
    v1 += 5 * cnpj[8] + 4 * cnpj[9] + 3 * cnpj[10] + 2 * cnpj[11]
    v1 = v1 % 11
    v1 = 0 if v1 < 2 else 11 - v1

    v2 = 6 * cnpj[0] + 5 * cnpj[1] + 4 * cnpj[2] + 3 * cnpj[3]
    v2 += 2 * cnpj[4] + 9 * cnpj[5] + 8 * cnpj[6] + 7 * cnpj[7]
    v2 += 6 * cnpj[8] + 5 * cnpj[9] + 4 * cnpj[10] + 3 * cnpj[11]
    v2 += 2 * v1

    v2 = v2 % 11
    v2 = 0 if v2 < 2 else 11 - v2

    return v1, v2

def is_valid_cnpj(value):
    if not isinstance(value, str) and not isinstance(value, int):
        return False

    value = re.sub(r'\D', '', str(value)).zfill(14)
    if len(re.sub(r'([0-9])\1+', r'\1', value)) == 1 or len(value) != 14:
        return False

    v1, v2 = last_digits_cnpj(value)

    if v1 != int(value[-2]) or v2 != int(value[-1]):
        return False

    return True

def validate_cnpj(value):
    if not is_valid_cnpj(value):
        raise ValidationError(
            _(f'({value}) não é um cnpj válidos.')
        )

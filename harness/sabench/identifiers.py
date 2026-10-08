"""Generate and validate well-formed (but fictional) security and entity identifiers.

ISIN  : ISO 6166, Luhn over letter-expanded digits
CUSIP : 8 chars + mod-10 "double-add-double" check digit
LEI   : ISO 17442, 18 chars + 2 check digits (ISO 7064 MOD 97-10)
SEDOL : 6 chars + weighted mod-10 check digit
"""
from __future__ import annotations

import hashlib
import string

_ALNUM = string.digits + string.ascii_uppercase


def _char_val(c: str) -> int:
    return int(c) if c.isdigit() else ord(c) - 55


def cusip_check_digit(base8: str) -> str:
    total = 0
    for i, c in enumerate(base8.upper()):
        if c.isdigit():
            v = int(c)
        elif c.isalpha():
            v = ord(c) - 55
        else:
            v = {"*": 36, "@": 37, "#": 38}[c]
        if i % 2 == 1:
            v *= 2
        total += v // 10 + v % 10
    return str((10 - total % 10) % 10)


def isin_check_digit(base11: str) -> str:
    digits = "".join(str(_char_val(c)) for c in base11.upper())
    total = 0
    for i, d in enumerate(reversed(digits)):
        v = int(d)
        if i % 2 == 0:
            v *= 2
        total += v // 10 + v % 10
    return str((10 - total % 10) % 10)


def lei_check_digits(base18: str) -> str:
    n = int("".join(str(_char_val(c)) for c in base18.upper() + "00"))
    return f"{98 - n % 97:02d}"


def sedol_check_digit(base6: str) -> str:
    w = [1, 3, 1, 7, 3, 9]
    total = sum(_char_val(c) * w[i] for i, c in enumerate(base6.upper()))
    return str((10 - total % 10) % 10)


def is_valid_isin(s: str) -> bool:
    return len(s) == 12 and s[:2].isalpha() and isin_check_digit(s[:11]) == s[11]


def is_valid_cusip(s: str) -> bool:
    return len(s) == 9 and cusip_check_digit(s[:8]) == s[8]


def is_valid_lei(s: str) -> bool:
    return len(s) == 20 and int("".join(str(_char_val(c)) for c in s.upper())) % 97 == 1


def _seeded(seed: str, n: int, alphabet: str) -> str:
    h = hashlib.sha256(seed.encode()).hexdigest()
    out, i = [], 0
    while len(out) < n:
        out.append(alphabet[int(h[i % len(h)] + h[(i + 1) % len(h)], 16) % len(alphabet)])
        i += 2
        if i >= len(h):
            h = hashlib.sha256(h.encode()).hexdigest()
            i = 0
    return "".join(out)


def make_cusip(seed: str) -> str:
    base = _seeded("cusip" + seed, 6, _ALNUM) + _seeded("cusip2" + seed, 2, string.digits)
    return base + cusip_check_digit(base)


def make_isin(seed: str, country: str = "US") -> str:
    """For US/CA, embeds a valid CUSIP as the NSIN, as real ISINs do."""
    nsin = make_cusip(seed) if country in ("US", "CA") else _seeded("isin" + seed, 9, _ALNUM)
    base = country + nsin
    return base + isin_check_digit(base)


def make_lei(seed: str, lou_prefix: str = "5493") -> str:
    base = lou_prefix + "00" + _seeded("lei" + seed, 12, _ALNUM)
    return base + lei_check_digits(base)


def make_sedol(seed: str) -> str:
    consonants = "BCDFGHJKLMNPQRSTVWXYZ" + string.digits
    base = _seeded("sedol" + seed, 6, consonants)
    return base + sedol_check_digit(base)


if __name__ == "__main__":  # pragma: no cover
    import sys
    for s in sys.argv[1:] or ["example"]:
        print(s, make_isin(s), make_isin(s, "LU"), make_cusip(s), make_lei(s), make_sedol(s))

import random
import string

NUMBERS = ["0","1","2","3","4","5","6","7","8","9"]
LETTERS = list(string.ascii_lowercase)

def build_short_link(long_link: str) -> str:
    random_out = random.choices(NUMBERS + LETTERS, k=5)
    generated_url = "".join(random_out)
    return generated_url
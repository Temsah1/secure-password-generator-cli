import random
import string


MIN_PASSWORD_LENGTH = 4
MAX_PASSWORD_LENGTH = 128


def read_number(prompt, minimum, maximum):
    while True:
        value = input(prompt).strip()

        if not value.isdigit():
            print("Please enter numbers only.")
            continue

        value = int(value)
        if value < minimum or value > maximum:
            print(f"Please choose a number from {minimum} to {maximum}.")
            continue

        return value


def read_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False

        print("Please answer with y or n.")


def get_password_groups(include_symbols):
    groups = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
    ]

    if include_symbols:
        groups.append("!@#$%&*?")

    return groups


def generate_password(length, include_symbols=True):
    groups = get_password_groups(include_symbols)

    if length < len(groups):
        raise ValueError(f"Password length must be at least {len(groups)} characters.")

    randomizer = random.SystemRandom()
    password_chars = [randomizer.choice(group) for group in groups]

    all_characters = "".join(groups)
    remaining_length = length - len(password_chars)

    for _ in range(remaining_length):
        password_chars.append(randomizer.choice(all_characters))

    randomizer.shuffle(password_chars)
    return "".join(password_chars)


def show_strength(password):
    score = 0

    if any(char.islower() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1
    if len(password) >= 12:
        score += 1

    if score >= 5:
        return "Very strong"
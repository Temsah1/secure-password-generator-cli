import random
import string


MIN_PASSWORD_LENGTH = 4
MAX_PASSWORD_LENGTH = 128

SYMBOLS = "!@#$%&*?"

STRENGTH_LABELS = {
    5: "Very Strong",
    4: "Strong",
    3: "Moderate",
    2: "Weak",
    1: "Very Weak",
}


def read_number(prompt: str, minimum: int, maximum: int) -> int:
    """Read a valid integer from the user within the given range."""
    while True:
        value = input(prompt).strip()

        if not value.isdigit():
            print("Please enter numbers only.")
            continue

        value = int(value)
        if not (minimum <= value <= maximum):
            print(f"Please choose a number between {minimum} and {maximum}.")
            continue

        return value


def read_yes_no(prompt: str) -> bool:
    """Read a yes/no answer from the user."""
    while True:
        answer = input(prompt).strip().lower()

        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False

        print("Please answer with y or n.")


def get_character_groups(include_symbols: bool) -> list[str]:
    """Return the character groups used for password generation."""
    groups = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
    ]
    if include_symbols:
        groups.append(SYMBOLS)
    return groups


def generate_password(length: int, include_symbols: bool = True) -> str:
    """
    Generate a random password of the given length.
    Guarantees at least one character from each group.
    """
    groups = get_character_groups(include_symbols)

    if length < len(groups):
        raise ValueError(
            f"Password length must be at least {len(groups)} characters."
        )

    rng = random.SystemRandom()

    # Guarantee one character from each group
    password_chars = [rng.choice(group) for group in groups]

    # Fill the remaining length from the full character pool
    all_characters = "".join(groups)
    password_chars += [rng.choice(all_characters) for _ in range(length - len(password_chars))]

    rng.shuffle(password_chars)
    return "".join(password_chars)


def get_strength_label(password: str) -> str:
    """Evaluate and return a strength label for the given password."""
    score = sum([
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in string.punctuation for c in password),
        len(password) >= 12,
    ])
    return STRENGTH_LABELS.get(score, STRENGTH_LABELS[1])


def main():
    print("=" * 40)
    print("       Password Generator")
    print("=" * 40)

    while True:
        length = read_number(
            f"\nPassword length ({MIN_PASSWORD_LENGTH}-{MAX_PASSWORD_LENGTH}): ",
            MIN_PASSWORD_LENGTH,
            MAX_PASSWORD_LENGTH,
        )
        include_symbols = read_yes_no("Include symbols like !@#$%? (y/n): ")

        try:
            password = generate_password(length, include_symbols)
        except ValueError as e:
            print(f"Error: {e}")
            continue

        strength = get_strength_label(password)

        print("\n" + "-" * 40)
        print(f"Password : {password}")
        print(f"Strength : {strength}")
        print("-" * 40)

        if not read_yes_no("\nGenerate another password? (y/n): "):
            print("\nGoodbye.")
            break


if __name__ == "__main__":
    main()

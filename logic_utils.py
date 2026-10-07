
"""Shared game logic for Game Glitch Investigator."""


def get_range_for_difficulty(difficulty: str) -> tuple[int, int]:
    """Return the inclusive number range for the selected difficulty."""
    ranges = {
        "Easy": (1, 20),
        "Normal": (1, 100),
        "Hard": (1, 50),
    }

    return ranges.get(difficulty, (1, 100))


def parse_guess(raw: str) -> tuple[bool, int | None, str | None]:
    """Validate input and convert a whole-number string to an integer."""
    if raw is None or not isinstance(raw, str) or not raw.strip():
        return False, None, "Enter a guess."

    try:
        guess = int(raw.strip())
    except ValueError:
        return False, None, "Please enter a valid whole number."

    return True, guess, None


def check_guess(guess: int, secret: int) -> tuple[str, str]:
    """Compare a guess with the secret and return an outcome and hint."""
    if not isinstance(guess, int) or not isinstance(secret, int):
        raise TypeError("Guess and secret must be integers.")

    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIX: AI-assisted refactor; high and low hints are no longer reversed.
    if guess > secret:
        return "Too High", "📉 Go LOWER!"

    return "Too Low", "📈 Go HIGHER!"


def update_score(
    current_score: int,
    outcome: str,
    attempt_number: int,
) -> int:
    """Update the game score using consistent scoring rules."""
    if outcome == "Win":
        points = max(10, 100 - 10 * attempt_number)
        return current_score + points

    # FIX: Incorrect guesses always receive the same penalty.
    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score

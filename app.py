
"""Streamlit interface for Game Glitch Investigator."""

import random

import streamlit as st

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


st.set_page_config(
    page_title="Game Glitch Investigator",
    page_icon="🎮",
    layout="centered",
)


ATTEMPT_LIMITS = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}


def reset_game(difficulty: str) -> None:
    """Reset all game values for the selected difficulty."""
    low, high = get_range_for_difficulty(difficulty)

    # FIX: New games use the correct difficulty range.
    st.session_state.secret = random.randint(low, high)

    # FIX: Every new game starts with zero attempts.
    st.session_state.attempts = 0
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.feedback = ""
    st.session_state.result = ""
    st.session_state.game_difficulty = difficulty


def submit_guess(raw_guess: str, difficulty: str) -> None:
    """Validate and process one submitted guess."""
    if st.session_state.status != "playing":
        return

    low, high = get_range_for_difficulty(difficulty)

    ok, guess, error = parse_guess(raw_guess)

    # FIX: Invalid input does not consume an attempt.
    if not ok:
        st.session_state.feedback = error
        st.session_state.result = "error"
        return

    if not low <= guess <= high:
        st.session_state.feedback = (
            f"Enter a number between {low} and {high}."
        )
        st.session_state.result = "error"
        return

    # Count a valid guess exactly once.
    st.session_state.attempts += 1
    st.session_state.history.append(guess)

    # FIX: Always compare integers, never convert secret to a string.
    outcome, message = check_guess(
        guess,
        st.session_state.secret,
    )

    st.session_state.score = update_score(
        current_score=st.session_state.score,
        outcome=outcome,
        attempt_number=st.session_state.attempts,
    )

    st.session_state.feedback = message

    if outcome == "Win":
        st.session_state.status = "won"
        st.session_state.result = "success"

    elif st.session_state.attempts >= ATTEMPT_LIMITS[difficulty]:
        st.session_state.status = "lost"
        st.session_state.result = "lost"

    else:
        st.session_state.result = "hint"


# ---------------------------------
# Sidebar settings
# ---------------------------------

st.sidebar.header("Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

low, high = get_range_for_difficulty(difficulty)
attempt_limit = ATTEMPT_LIMITS[difficulty]

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")


# ---------------------------------
# Initialize or reset game state
# ---------------------------------

if (
    "game_difficulty" not in st.session_state
    or st.session_state.game_difficulty != difficulty
):
    reset_game(difficulty)


# ---------------------------------
# Game interface
# ---------------------------------

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated game, debugged and repaired.")

st.subheader("Make a guess")

raw_guess = st.text_input(
    "Enter your guess:",
    key="guess_input",
    disabled=st.session_state.status != "playing",
)

col1, col2, col3 = st.columns(3)

with col1:
    submit = st.button(
        "Submit Guess 🚀",
        disabled=st.session_state.status != "playing",
    )

with col2:
    new_game = st.button("New Game 🔁")

with col3:
    show_hint = st.checkbox(
        "Show hint",
        value=True,
    )


# ---------------------------------
# Button actions
# ---------------------------------

if new_game:
    reset_game(difficulty)
    st.rerun()

if submit:
    submit_guess(raw_guess, difficulty)

    # FIX: Rerun so the displayed state uses updated values.
    st.rerun()


# ---------------------------------
# Updated status and feedback
# ---------------------------------

attempts_left = max(
    0,
    attempt_limit - st.session_state.attempts,
)

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempts_left}"
)

if st.session_state.result == "error":
    st.error(st.session_state.feedback)

elif st.session_state.status == "won":
    st.success(st.session_state.feedback)
    st.success(
        f"You won! The secret was {st.session_state.secret}. "
        f"Final score: {st.session_state.score}"
    )

elif st.session_state.status == "lost":
    st.error(
        f"Out of attempts! "
        f"The secret was {st.session_state.secret}. "
        f"Final score: {st.session_state.score}"
    )

elif show_hint and st.session_state.result == "hint":
    st.warning(st.session_state.feedback)


# ---------------------------------
# Developer information
# ---------------------------------

with st.expander("Developer Debug Info"):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("Status:", st.session_state.status)
    st.write("History:", st.session_state.history)


# ---------------------------------
# Session summary
# ---------------------------------

if st.session_state.history:
    st.subheader("Guess History")

    for number, guess in enumerate(
        st.session_state.history,
        start=1,
    ):
        st.write(f"Attempt {number}: {guess}")

st.divider()
st.caption("AI-assisted debugging with human verification.")

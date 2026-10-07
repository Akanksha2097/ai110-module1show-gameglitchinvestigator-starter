
"""Automated tests for Game Glitch Investigator."""

import pytest

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


# ---------------------------------
# Difficulty tests
# ---------------------------------

def test_easy_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_normal_difficulty():
    assert get_range_for_difficulty("Normal") == (1, 100)


def test_hard_difficulty():
    assert get_range_for_difficulty("Hard") == (1, 50)


# ---------------------------------
# Guess and hint tests
# ---------------------------------

def test_correct_guess():
    outcome, message = check_guess(98, 98)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_low():
    outcome, message = check_guess(50, 98)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_guess_too_high():
    outcome, message = check_guess(90, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_with_invalid_secret_type():
    with pytest.raises(TypeError):
        check_guess(50, "98")


# ---------------------------------
# Input parsing tests
# ---------------------------------

def test_valid_integer():
    ok, guess, error = parse_guess("50")
    assert ok is True
    assert guess == 50
    assert error is None


def test_empty_input():
    ok, guess, error = parse_guess("")
    assert ok is False
    assert guess is None
    assert error is not None


def test_whitespace_input():
    ok, guess, error = parse_guess("   ")
    assert ok is False
    assert guess is None


def test_decimal_input():
    ok, guess, error = parse_guess("10.5")
    assert ok is False
    assert guess is None


def test_text_input():
    ok, guess, error = parse_guess("hello")
    assert ok is False
    assert guess is None


def test_none_input():
    ok, guess, error = parse_guess(None)
    assert ok is False
    assert guess is None


def test_negative_integer_parsing():
    ok, guess, error = parse_guess("-5")
    assert ok is True
    assert guess == -5
    assert error is None


def test_large_number_parsing():
    ok, guess, error = parse_guess("999999")
    assert ok is True
    assert guess == 999999
    assert error is None


# ---------------------------------
# Scoring tests
# ---------------------------------

def test_score_too_low():
    assert update_score(0, "Too Low", 1) == -5


def test_score_too_high():
    assert update_score(0, "Too High", 1) == -5


def test_score_win():
    assert update_score(0, "Win", 2) == 80


def test_score_minimum_win_bonus():
    assert update_score(0, "Win", 20) == 10


def test_score_unknown_outcome():
    assert update_score(10, "Unknown", 1) == 10

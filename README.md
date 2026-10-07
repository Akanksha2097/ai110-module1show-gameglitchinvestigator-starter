# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

### Test Results

I executed the automated test suite using:

```bash
python -m pytest -v
```

The test suite collected 20 tests and all 20 passed successfully.

```text
platform darwin -- Python 3.13.15, pytest-9.1.1
collected 20 items

test_easy_difficulty PASSED
test_normal_difficulty PASSED
test_hard_difficulty PASSED
test_correct_guess PASSED
test_guess_too_low PASSED
test_guess_too_high PASSED
test_guess_with_invalid_secret_type PASSED
test_valid_integer PASSED
test_empty_input PASSED
test_whitespace_input PASSED
test_decimal_input PASSED
test_text_input PASSED
test_none_input PASSED
test_negative_integer_parsing PASSED
test_large_number_parsing PASSED
test_score_too_low PASSED
test_score_too_high PASSED
test_score_win PASSED
test_score_minimum_win_bonus PASSED
test_score_unknown_outcome PASSED

20 passed in 0.03s
```

The tests verify the game logic, input parsing, difficulty ranges, and scoring rules.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

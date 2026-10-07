# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran Game Glitch Investigator in Streamlit, the application displayed a guessing game with difficulty settings, a score, an attempt counter, and a developer debugging panel. I noticed that the hints were incorrect: when the secret number was 98 and I entered 50, the game told me to go lower instead of higher. I also found that Normal difficulty started with only 7 attempts remaining, even though the settings allowed 8. After inspecting the source code, I identified another reset issue: the New Game handler did not reset the score, history, or game status.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location |
|---|---|---|---|---|
| Secret = 98, guess = 50 | Show "Go HIGHER!" | Displayed "Go LOWER!" | Incorrect hint displayed; no terminal error confirmed | `app.py`, `check_guess()` |
| Start Normal difficulty | 8 attempts remaining and 0 attempts used | 7 remaining and 1 recorded before a valid guess | No terminal error | `app.py`, attempts initialization |
| Make a guess, then click New Game | Reset attempts, score, history, and game status | Original code resets only attempts and secret; verify the retained values in the game | Record actual UI/debug output after testing | `app.py`, New Game handler |

These issues showed me that an application can load successfully while containing logical errors. Using the developer debugging panel helped me compare what appeared on the screen with the game's internal values.


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

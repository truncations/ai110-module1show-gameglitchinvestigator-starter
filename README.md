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

- [X] Describe the game's purpose.
    The game's purpose is a simple number guessing game ranging in 3 difficulties which either change the range for the number to be guessed or change the number of attempts you can have for the game. When you begin the game, the game will roll for a secret number that the user must guess. The user guesses a number and if it's incorrect, the game will give you a "GO HIGHER" or "GO LOWER" hint to help you figure out the correct value. Once you run out of attempts or you have successfully guessed the secret number, the game is over and you can choose to start a new game. 
- [X] Detail which bugs you found.
    Some bugs that have been found have included:
        - The game ending when the number of attempts left reaches 1.
        - User interface displaying error on the number of attempts and range of guess which misled the user.
        - User interface displaying error on the hints of "GO LOWER" or "GO HIGHER"; felt random on what hints were given at times.
        - The secret number going out of the valid range of numbers that can be guessed if a different difficulty was chosen. For example, if the user chose easy, the range of numbers is 1 to 20, but sometimes the game would end up choosing a number like 68.
        - If you submitted an invalid guess, the number of attempts would decrease which shouldn't occur because the user may have made an input mistake.
        - If the game was completed and you pressed "Start New Game", the game wouldn't actually restart and you would be stuck.
        - Sometimes you were actually increasing in score.
- [X] Explain what fixes you applied.
    The fixes that I applied were assisted in companion with AI, specifically with GitHub Copilot and Claude Code. We initialized new variables to store states more accurately for user interface elements, as well as modified the initialization of some variables to allow for consistent gameplay. We then modified the strings, often turning them into format strings and using the variables like 'low' and 'high' to display the correct values to the user. The hints logic was rewritten, by converting the secret to an integer which could then be compared properly with our guess using inequality comparisons to then give the user correct feedback. We made sure that within any invalid guess, the number of attempts left wouldn't decrement by moving the increment of attempts to a different scope in the program. Finally, we fixed the program logic when restarting the game by changing the values of other variables that were meant to be changed, but weren't included.

    Overall, these fixes helped to create a simple gameplay loop that any user can experience without any issues.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

Assuming the Secret is 45,
1. User enters a guess of 40.
2. Game returns "Too Low".
3. User enters a guess of 50.
4. Game returns "Too High".
5. Score updates correctly after each guess.
6. Game ends after the correct guess or user runs out of attempts.
7. During the middle or end of the game, the user can choose a difficulty, then click new game.
8. If new game is pressed, a new secret value is rolled.
9. Game loop repeating steps 1 through 8 until the user decides to quit the game.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

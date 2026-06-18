# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
- If the number of attempts left reaches 1, the game is over, even though the attempts left counter when the game is over should display 0.
- Upon launch, if you switch difficultuies of the game to anything but Normal Difficulty, the 'Range' on the side bar would be correctly displayed, but the main text, "Guess a number between 1 and 100. Attempts left: 5" wouldn't update/show the correct range/number of attempts. Additionally, the Attempts allowed on the side bar does not match the attempts left displayed on the main page.
- When I completed one game whether guessing correctly or using all of my attempts and not correctly guessing the number, pressing the "Restart" button would not do anything, no restart of the game occurred.
- The number of attempts go down when you submit an invalid guess, which shouldn't be the case if the user made a mistake inputting an invalid value like text, or inputting nothing.

**Bug Reproduction Log**
- When you switch difficulties, the attempts counter does not 
Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess of 0 | "Go LOWER!" hint shows  | "Go HIGHER!" hint should show | "none" |
| Guess of -41 | "Go LOWER!" hint shows | "Go HIGHER!" hint should show | "none" |
| Guess of 25551.322 | "Go HIGHER!" hint shows | "Go LOWER!" hint should show | "none" |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
    I utilized GitHub Copilot and Claude Code (as a last resort) for this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

CORRECT AI EXAMPLE
An AI suggestion that was correct was when I finished refactoring the codebase from app.py (by splitting the logic and UI code into 2 separate files) was when I needed to fix an error in the function check_guess in logic_utils.py. The secret value was being improperly checked because the secret value was being parsed as a string, and so I noted this error to the AI by stating that the secret value was being parsed as a string initially as well as the checks for comparing the guess and secret value would be improper if we compared using strings. The AI suggested a result where it removed the initial try/catch statement and added a local variable to parse the secret value into an integer. Once the secret value was parsed into an integer we could use number inequality comparisons to compare if the value was exact or too high or too low. Then, we reversed the hint messages of "GO LOWER" and "GO HIGHER" to properly display the user the correct hint that they should follow. I verified this result of proper gameplay by testing the streamlit app directly. Since I had a devlog that I can work with, I looked at the secret value and inputted lower and higher values intentionally to make sure the "GO HIGHER" and "GO LOWER" respectively would show up.

INCORRECT AI EXAMPLE
An Incorrect AI Example that I faced was when I needed to fix the Attempts Left counter. The bug was that the attempts left counter would show 1 rather than 0 for when the game was over. Even though I prompted GitHub Copilot to make changes to fix this dilemma, the AI would constantly bounce between 2 solutions that didn't resolve the problem, by adding st.rerun() or trying to fix the conditional logic with the number of attempts. I continuously struggled with this despite providing results of my issues and validating the code written. The way I verified the results was by testing the app with the streamlit package since this was based on the user's experience. I tested incorrect attempts until the number of attempts left was low enough to warrant the game to end. At one point, GitHub Copilot rewrote code that already existed in the program and I denied that solution and ended up switching AI models to Claude Code to see if I could get a difference. After prompting what program i'm looking for AND the results I have already received, Claude Code explained the reasoning behind some of the errors of the code and the logic, and also fixed the issue with this display error by creating a variable to store the UI element rather than creating it on the spot.
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

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
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

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

# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->
I have a visual error in my app. When the attempts left counter reaches 1, the game ends even though the attempts left counter should reach 0 to end the game. I have attached the context of the files and their line numbers where the error could be occuring. Once you have made the fixes, can you explain what was your thought process for the solution you wrote?

|                          |    Model A     |   Model B   |
|--------------------------|----------------|-------------|
| **Model name**           | GitHub Copilot | Claude Code |
| **Response summary**     | Unsuccessful; looped between 2 solutions that didn't work; changed conditionals and used st.rerun() improperly. | Successful; explained reasons for issues with st.rerun() and created variables and functions to store and update streamlit UI elements. |
| **More Pythonic?**       | NO; Added lines to program. | YES; Modularized program which allowed for improved maintainability. |
| **Clearer explanation?** | NO; looped between 2 solutions with no clear explanation of past errors. | YES; explained reasons for errors with st.rerun(), the behavior of streamlit with this bug, and then wrote a proper solution. |

**Which did you prefer and why?**

<!-- Your conclusion -->
I preferred Claude Code for its ability to assess the packages utilized for the app and then explain why the code written resulted in glitches and bugs by describing the behavior that streamlit expresses while the program ran. It seemed to be much smarter in determining the core cause of the glitches over GitHub Copilot who got stuck between 2 solutions pretending as if those 2 solutions would resolve other problems. Additionally, although the modification of code was small in comparison to GitHub Copilot and Claude Code, Claude Code wrote a more pythonic solution by modularizing the program; it wrote variables to store the user interface elements and then created functions to update their visuals when needed, which allowed me to then be able to use the functions when I wanted to use them if I return to this project.
 
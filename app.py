import random
import streamlit as st
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("Settings")

attempts_box = st.empty()
debug_box = st.empty()

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

# FIX: Incorrectly displayed the number of attempts at the start of a new game, notified AI of such error by providing context
# of the issue to which it directed itself here and changed the value from 1 -> 0.
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("Make a guess")

# FIX (FIXME_1): Reserve the slot with st.empty() and fill it via render_attempts() so the
# "Attempts left" count can be redrawn after the guess is processed, without an st.rerun()
# (which would discard the hint/win/loss messages below).
def render_attempts():
    attempts_box.info(
        # FIX: Converted the text into a formatted string, where we inputted the variables low and high.
        f"Guess a number between {low} and {high}. "
        f"Attempts left: {attempt_limit - st.session_state.attempts}"
    )

# FIX: Same placeholder pattern as render_attempts() — reserve the expander slot and fill it
# via render_debug() so the debug readout reflects post-guess state instead of lagging a turn.
def render_debug():
    with debug_box.expander("Developer Debug Info"):
        st.write("Secret:", st.session_state.secret)
        st.write("Attempts:", st.session_state.attempts)
        st.write("Score:", st.session_state.score)
        st.write("Difficulty:", difficulty)
        st.write("History:", st.session_state.history)

render_attempts()
render_debug()

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    st.session_state.attempts = 0
    # FIX: Allows user to now restart the game and have a game loop going. No AI was needed.
    # Score was also reset since a new game means a full refreshed state.
    st.session_state.status = "playing"
    st.session_state.score = 0
    st.session_state.secret = random.randint(low, high)
    st.success("New game started.")
    st.rerun()

if submit:
    if st.session_state.status != "playing":
        if st.session_state.status == "won":
            st.success("You already won. Start a new game to play again.")
        else:
            st.error("Game over. Start a new game to try again.")
        st.stop()
    else:
        ok, guess_int, err = parse_guess(raw_guess)

        if not ok:
            st.session_state.history.append(raw_guess)
            st.error(err)
        else:
            # Only increment attempts for valid guesses
            st.session_state.attempts += 1
            st.session_state.history.append(guess_int)

            # FIX: Fixed redundancy that would parse the secret number as a string if the attempts left were even.
            secret = st.session_state.secret

            outcome, message = check_guess(guess_int, secret)

            if show_hint:
                st.warning(message)

            st.session_state.score = update_score(
                current_score=st.session_state.score,
                outcome=outcome,
                attempt_number=st.session_state.attempts,
            )

            if outcome == "Win":
                st.balloons()
                st.session_state.status = "won"
                st.success(
                    f"You won! The secret was {st.session_state.secret}. "
                    f"Final score: {st.session_state.score}"
                )
            elif st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

        # FIX: Redraw the reserved slots with the post-increment state instead of st.rerun(),
        # so the count + debug info update immediately while the messages above stay on screen.
        render_attempts()
        render_debug()

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")

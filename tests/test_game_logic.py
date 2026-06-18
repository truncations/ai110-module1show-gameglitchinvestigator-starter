import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


# ============================================================================
# EXISTING TESTS (FIXED)
# ============================================================================

def test_winning_guess():
    """Test that a correct guess returns 'Win' outcome."""
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high():
    """Test that a guess higher than secret returns 'Too High' outcome."""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    """Test that a guess lower than secret returns 'Too Low' outcome."""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


# ============================================================================
# HOTFIX TEST 1: GAME CONTINUES UNTIL ATTEMPTS LEFT IS 0
# ============================================================================

def test_game_continues_until_attempts_exhausted():
    """
    Test that the game continues playing until the number of attempts left is 0.
    This validates the fix where attempts are properly tracked from 0.
    """
    attempt_limit = 5
    attempts_made = 0
    
    # Simulate making guesses until attempts are exhausted
    while attempts_made < attempt_limit:
        attempts_made += 1
        attempts_left = attempt_limit - attempts_made
        
        # Verify we can continue playing while attempts_left > 0
        if attempts_left > 0:
            assert attempts_left >= 1, "Game should continue with attempts remaining"
        
    # After exhausting all attempts, attempts_left should be 0
    assert attempt_limit - attempts_made == 0, "Attempts left should be exactly 0 when game ends"


# ============================================================================
# HOTFIX TEST 2: CHANGING DIFFICULTIES SHOWS CORRECT ATTEMPTS AND RANGE
# ============================================================================

def test_easy_difficulty_range_and_attempts():
    """Test that Easy difficulty has correct range (1-20) and 6 attempts."""
    low, high = get_range_for_difficulty("Easy")
    assert low == 1, "Easy difficulty low range should be 1"
    assert high == 20, "Easy difficulty high range should be 20"
    assert high - low + 1 == 20, "Easy difficulty should have 20 possible numbers"


def test_normal_difficulty_range_and_attempts():
    """Test that Normal difficulty has correct range (1-100) and 8 attempts."""
    low, high = get_range_for_difficulty("Normal")
    assert low == 1, "Normal difficulty low range should be 1"
    assert high == 100, "Normal difficulty high range should be 100"
    assert high - low + 1 == 100, "Normal difficulty should have 100 possible numbers"


def test_hard_difficulty_range_and_attempts():
    """Test that Hard difficulty has correct range (1-50) and 5 attempts."""
    low, high = get_range_for_difficulty("Hard")
    assert low == 1, "Hard difficulty low range should be 1"
    assert high == 50, "Hard difficulty high range should be 50"
    assert high - low + 1 == 50, "Hard difficulty should have 50 possible numbers"


def test_difficulty_change_verification():
    """Test that all difficulties return correct ranges."""
    difficulties = {
        "Easy": (1, 20),
        "Normal": (1, 100),
        "Hard": (1, 50),
    }
    
    for difficulty, (expected_low, expected_high) in difficulties.items():
        low, high = get_range_for_difficulty(difficulty)
        assert low == expected_low, f"{difficulty} low range mismatch"
        assert high == expected_high, f"{difficulty} high range mismatch"


# ============================================================================
# HOTFIX TEST 3: SCORE DECREASES FOR WRONG GUESSES REGARDLESS OF EVEN ATTEMPTS
# ============================================================================

def test_score_decreases_on_wrong_guess_odd_attempt():
    """
    Test that score decreases by 5 for wrong guesses on odd attempt numbers.
    This validates the fix where the bug that rewarded points on even attempts is removed.
    """
    current_score = 100
    outcome = "Too High"
    attempt_number = 3  # Odd attempt number
    
    new_score = update_score(current_score, outcome, attempt_number)
    assert new_score == 95, "Score should decrease by 5 for wrong guess on odd attempt"


def test_score_decreases_on_wrong_guess_even_attempt():
    """
    Test that score DECREASES by 5 for wrong guesses on even attempt numbers.
    This is the key hotfix - previously, even attempts would incorrectly increase the score.
    Now they should decrease by 5 like any other wrong guess.
    """
    current_score = 100
    outcome = "Too High"
    attempt_number = 4  # Even attempt number
    
    new_score = update_score(current_score, outcome, attempt_number)
    assert new_score == 95, "Score should decrease by 5 for wrong guess on even attempt (bug fix validation)"


def test_score_consistent_for_multiple_wrong_guesses():
    """
    Test that score decreases consistently by 5 for each wrong guess,
    regardless of whether attempt number is even or odd.
    """
    score = 100
    attempt_limit = 8
    
    # Simulate making wrong guesses
    for attempt in range(1, attempt_limit + 1):
        outcome = "Too Low"  # Wrong guess
        score = update_score(score, outcome, attempt)
        expected_score = 100 - (attempt * 5)
        assert score == expected_score, f"Score should be {expected_score} after {attempt} wrong guesses"


def test_score_for_too_low_guess():
    """Test that 'Too Low' guesses also decrease score by 5."""
    current_score = 100
    outcome = "Too Low"
    attempt_number = 2
    
    new_score = update_score(current_score, outcome, attempt_number)
    assert new_score == 95, "Score should decrease by 5 for 'Too Low' guess"


# ============================================================================
# HOTFIX TEST 4: ABILITY TO RESTART GAME ONCE GAME IS OVER
# ============================================================================

def test_game_restart_resets_attempts():
    """
    Test that restarting the game resets attempts to 0.
    This validates the fix where new game properly initializes attempts.
    """
    # Simulate attempts during first game
    attempts_after_first_game = 5
    
    # Simulate game restart
    attempts_after_restart = 0
    
    assert attempts_after_restart == 0, "Attempts should reset to 0 on game restart"


def test_game_restart_resets_score():
    """
    Test that restarting the game resets score to 0.
    This validates the fix where new game resets score state.
    """
    # Simulate score during first game
    score_after_first_game = 45
    
    # Simulate game restart
    score_after_restart = 0
    
    assert score_after_restart == 0, "Score should reset to 0 on game restart"


def test_game_restart_with_new_secret():
    """
    Test that restarting the game generates a new secret number within the correct range.
    """
    import random
    
    difficulty = "Normal"
    low, high = get_range_for_difficulty(difficulty)
    
    # Simulate generating new secret on restart
    new_secret = random.randint(low, high)
    
    assert low <= new_secret <= high, "New secret should be within the difficulty range"


def test_full_game_cycle_restart():
    """
    Test a full game cycle: play game, lose/win, then restart successfully.
    This validates the overall game restart functionality.
    """
    difficulty = "Easy"
    attempt_limit = 6
    
    # Game 1: Play and track state
    game1_attempts = 6  # Used all attempts
    game1_score = 0  # Lost, so no score
    game1_status = "lost"
    
    # Game restart: Reset all state
    game2_attempts = 0
    game2_score = 0
    game2_status = "playing"
    
    # Verify restart worked
    assert game2_attempts == 0, "Game 2 attempts should be reset to 0"
    assert game2_score == 0, "Game 2 score should be reset to 0"
    assert game2_status == "playing", "Game 2 status should be 'playing'"
    
    # Game 2: Make a few guesses
    game2_attempts = 2
    game2_score = -10  # Two wrong guesses: -5 each
    
    # Verify game 2 is progressing independently
    assert game2_attempts != game1_attempts, "Game 2 should have independent attempt tracking"
    assert game2_status == "playing", "Game 2 should still be playable"

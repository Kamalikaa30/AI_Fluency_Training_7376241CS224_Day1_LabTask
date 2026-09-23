"""Day 2, Part B: print the agent's real ReAct trace to compare with the paper trace."""

import sys
import os

# Find the project root and Day1 folder
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

DAY1_FOLDER = os.path.join(PROJECT_ROOT, "Day1")

# Allow Day2 to import the existing Day1 agent and config
sys.path.insert(0, DAY1_FOLDER)

from agent import agent


QUESTION = (
    "Which is cheaper: CS101 and AI202 with a 10% scholarship, "
    "or all three courses with a 25% scholarship? By how much?"
)


print("QUESTION:", QUESTION)
print("\n--- the agent's actions and observations ---")

answer = agent(QUESTION, max_steps=8)

print("\nFINAL ANSWER:", answer)
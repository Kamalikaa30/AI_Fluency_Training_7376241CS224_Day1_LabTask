import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from collections import Counter
from Day1.config import client, MODEL, banner
from cot_compare import COT_PROMPT, QUESTIONS

RUNS = 5
TEMPERATURE = 1.2
      # deliberately NOT 0, so each run can differ

def final_answer(text):
    """Extract a clean final answer from the model response."""
    for line in reversed(text.splitlines()):
        line = line.strip()

        if line.lower().startswith("final answer:"):
            return line.split(":", 1)[1].strip()

    # If the model did not follow the format, return the full response
    # instead of incorrectly treating a random calculation line as the answer.
    return "(no clear final answer)"

def run_many(question, runs=RUNS, temperature=TEMPERATURE):
    answers = []
    for attempt in range(1, runs + 1):
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "system", "content": COT_PROMPT},
                      {"role": "user", "content": question}],
            temperature=temperature,
            max_tokens=400,
        )
        answer = final_answer(response.choices[0].message.content)
        print(f"   run {attempt}: {answer}")
        answers.append(answer)
    return answers

if __name__ == "__main__":
    banner("SELF-CONSISTENCY")
    question = QUESTIONS[0]
    print("QUESTION:", question, "\n")
    answers = run_many(question)
    winner, count = Counter(answers).most_common(1)[0]
    print(f"\nMajority answer ({count} of {len(answers)} runs): {winner}")
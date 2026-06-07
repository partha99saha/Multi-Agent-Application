import json
from datetime import datetime

FEEDBACK_FILE = "feedback.jsonl"


def save_feedback(question, answer, rating):

    record = {
        "time": str(datetime.now()),
        "question": question,
        "answer": str(answer),
        "rating": rating,  # +1 or -1
    }

    with open(FEEDBACK_FILE, "a") as f:
        f.write(json.dumps(record) + "\n")

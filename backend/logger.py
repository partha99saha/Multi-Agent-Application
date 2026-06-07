import json
from datetime import datetime

LOG_FILE = "logs.jsonl"


def log_interaction(question, answer, plan):

    record = {
        "timestamp": str(datetime.now()),
        "question": question,
        "answer": str(answer),
        "plan": plan,
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(record) + "\n")

import uuid
import time

SESSIONS = {}


def create_session():
    session_id = str(uuid.uuid4())

    SESSIONS[session_id] = {
        "history": [],
        "created_at": time.time(),
        "active_task": None,
        "cancel_tasks": set(),
    }

    return session_id


def get_session(session_id: str):
    return SESSIONS.get(session_id)


def set_active_task(session_id: str, task_id: str):
    if session_id in SESSIONS:
        SESSIONS[session_id]["active_task"] = task_id


def get_active_task(session_id: str):
    return SESSIONS.get(session_id, {}).get("active_task")


def cancel_task(session_id: str, task_id: str):
    if session_id in SESSIONS:
        SESSIONS[session_id]["cancel_tasks"].add(task_id)


def is_cancelled(session_id: str, task_id: str) -> bool:
    session = SESSIONS.get(session_id)

    if not session:
        return False

    return task_id in session["cancel_tasks"]
